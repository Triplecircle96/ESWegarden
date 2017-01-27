BOT_NAME = 'raspibot'
SLACK_BOT_TOKEN = 'xoxb-111989275299-XF8mdgF7aOkubdrxe22wIhDt'

import time
import threading
from slackclient import SlackClient

slack_client = SlackClient(SLACK_BOT_TOKEN)

class slack:
    def __init__(self):
        print("Starting to Create Slack Bot")
        # ESW Slackbot's ID Values

        self.BOT_ID = self.botIDfinder()
        print type(self.BOT_ID)
        print('bot id for debug')
        print self.BOT_ID
        # self.BOT_ID = 'U39V3838T'
        self.SLACK_BOT_TOKEN = SLACK_BOT_TOKEN

        # constants
        self.AT_BOT = "<@" + self.BOT_ID + ">"
        self.EXAMPLE_COMMAND = "do"

        # instantiate Slack Client
        self.slack_client = SlackClient(self.SLACK_BOT_TOKEN)

        l = threading.Thread(target=self.instantiateSlack)
        l.start()

    def botIDfinder(self):
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                    return user.get('id')
        else:
            print("could not find bot user with the name " + BOT_NAME)

    def handle_command(command, channel, self):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        response = "Not sure what you mean. Use the *" + self.EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."
        if command.startswith('status'):
            response = "I will get the status of the systems for you!"

        self.slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)


    def parse_slack_output(slack_rtm_output, self):
        """
            The Slack Real Time Messaging API is an events firehose.
            this parsing function returns None unless a message is
            directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and self.AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(self.AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None

    def instantiateSlack(self):
        READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
        if self.slack_client.rtm_connect():
            print("Raspibot connected and running!")
            while True:
                command, channel = self.parse_slack_output(self.slack_client.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")