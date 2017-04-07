BOT_NAME = 'raspibot'

import time
import threading
import os
from slackclient import SlackClient
from systemTypes import nft
from systemTypes import drip
from systemTypes import ebbnflow

class slack:
    def __init__(self):
        self.systemThreads = []

        print("Starting to Create Slack Bot")
        # ESW Slackbot's ID Values
        
        self.BOT_ID = os.environ.get("BOT_ID")
        print type(self.BOT_ID)
        print('bot id for debug')
        print self.BOT_ID

        # self.SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
        self.output_list = 0
        # constants
        self.AT_BOT = "<@" + self.BOT_ID + ">"
        self.EXAMPLE_COMMAND = "do"
        l = threading.Thread(target=self.instantiateSlack)
        l.start()

    def botIDfinder(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                    return user.get('id')
        else:
            print("could not find bot user with the name " + BOT_NAME)


    def updateSystemThreads(self, threadsList):
        self.systemThreads = threadsList
        print("Thread Manager Thread List Updated")
        
    def getStatus(self):
        statuses = ""
        for sys in self.systemThreads:
            statuses = statuses + sys.diagnostic() + '\n'
        return statuses
        #print("example of status")
    
    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        response = "Not sure what you mean. Use the *" + self.EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."
        command = command.lower()
        if command.startswith('status'):
            response = ("I will get the status of the systems for you!:\n" +
                        self.getStatus())
        
        elif command.startswith('nutrients'):
            response = "The last time compost tea was added was..." #eventually we could record when compost tea is added/needed

        elif command.startswith('take a picture'):
            image_url = "http://zdnet4.cbsistatic.com/hub/i/2015/02/15/854dfd8d-bee3-41c1-a68b-d8554efcef85/0dc5a553715e4f5f620505bd62228155/raspi-logo.png"
            attachments = [{"title": "testImage", "image_url": image_url}]
            self.slack_client.api_call("chat.postMessage", channel=channel, text='postMessage test',
                        attachments = attachments)
            response = "Here is the image"

        self.slack_client.api_call("chat.postMessage", channel=channel,
                        text=response, as_user=True)

    def parse_slack_output(self, slack_rtm_output):
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
        READ_WEBSOCKET_DELAY = 1
        if self.slack_client.rtm_connect():
            print("Raspibot connected and running!")
            while True:
                command, channel = self.parse_slack_output(self.slack_client.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")
