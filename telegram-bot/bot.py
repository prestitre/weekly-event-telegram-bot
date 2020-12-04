import requests
import json
import configparser as cfg
import urllib



class telegram_chatbot():

    def __init__(self, config):
        """ gets keys from config and sets base format for requests """
        self.token = self.read_token_from_config_file(config)
        self.url = self.read_url_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        

    def get_updates(self, offset=None):
        """ Get messages to bot from server """
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):

        """ Sends a compiled message using a query string, with debug content printed to console """

        url = self.base + "sendMessage?parse_mode={}&chat_id={}&text={}".format("MarkdownV2", chat_id, urllib.parse.quote((msg)))

        print("--------------")
        print("THE MESSAGE IS")
        print("--------------")
        print(msg)

        print("-------------------")
        print("THE QUERY STRING IS")
        print("-------------------")
        print(url)
        
        print("--------------------")
        print("THE HTTP RESPONSE IS")
        print("--------------------")
        if msg is not None:
            r = requests.get(url)
            print(r.status_code)
            print(r.content)
        

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

    def read_url_fin_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('urls', 'calendar')
