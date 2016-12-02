import time
from slackclient import SlackClient

class slack:
    def __init__(self):
        print("Starting to Create Slack Bot")
        # ESW Slackbot's ID Values
        self.BOT_ID = 'U39V3838T'
        self.SLACK_BOT_TOKEN = 'xoxb-111989275299-TC0QD7cfqaOBWunvexHqLt3u'

        # constants
        self.AT_BOT = "<@" + self.BOT_ID + ">"
        self.EXAMPLE_COMMAND = "do"

        # instantiate Slack Client
        self.slack_client = SlackClient(self.SLACK_BOT_TOKEN)

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
            print("StarterBot connected and running!")
            while True:
                command, channel = self.parse_slack_output(self.slack_client.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")