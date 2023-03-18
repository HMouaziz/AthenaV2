import sys

import openai as openai

from functions import Settings
from interface import Interface


class Athena:
    exit_conditions = ("/q", "quit", "exit", "-q")
    settings_conditions = ("settings", "open settings")
    start_sequence = "\nAthena:"
    restart_sequence = "\n\nUser:"
    session_prompt = "You are talking to Athena, GPT3 bot modelled after Athena an ancient Greek goddess associated " \
                     "with wisdom, warfare, and handicraft. Athena loves being helpful and tries to answer your " \
                     "questions as best she can. She is very curious and enjoys learning about new things as well as " \
                     "improving her existing knowledge base.\n\nUser: Hello, who are you?\nAthena: I am Athena. " \
                     "collector and guardian of knowledge. How can I help you?"
    request = {}
    chat_log = None

    def __init__(self):
        openai.api_key = "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"
        self.request = Settings.get()

    def run(self, startup=False):
        if startup is True:
            Interface.display_start_message(message="[  Athena AI v1.0.1, Halim Mouaziz  ]")

        while True:
            query = Interface.get_input()
            if query in self.exit_conditions:
                print("Exiting...")
                sys.exit(1)
            elif query in self.settings_conditions:
                Interface.settings_ui()
            else:
                self.create_request(query)
                response = self.run_request()
                self.append_chat_log(query, response['choices'][0]['text'])
                Interface.display_response(response)
    
    def create_request(self, query):
        prompt = f'{self.chat_log}{self.restart_sequence}: {query}{self.start_sequence}:'
        self.request["prompt"] = prompt

    def run_request(self):
        response = openai.Completion.create(
            model=self.request['model'],
            prompt=self.request['prompt'],
            max_tokens=self.request['max_tokens'],
            temperature=self.request['temperature'],
            top_p=self.request['top_p'],
            n=self.request['n'],
            stream=self.request['stream'],
            logprobs=self.request['logprobs'],
            echo=self.request['echo'],
            stop=self.request['stop'],
            presence_penalty=self.request['presence_penalty'],
            frequency_penalty=self.request['frequency_penalty'],
            best_of=self.request['best_of'],
            user=self.request['user']
        )
        return response

    def append_chat_log(self, query, answer):
        if self.chat_log is None:
            self.chat_log = self.session_prompt
        self.chat_log = f'{self.chat_log}{self.restart_sequence} {query}{self.start_sequence}{answer}'
