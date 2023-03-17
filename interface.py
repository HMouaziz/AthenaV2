import pyperclip
from printy import printy
from functions import Utils
from pyfiglet import Figlet
from InquirerPy import inquirer, get_style


class Interface:
    style = get_style({"questionmark": "#ea6500",
                       "answermark": "#e5c07b",
                       "answer": "#ffffff",
                       "input": "#ea6500",
                       "question": "",
                       "answered_question": "",
                       "instruction": "#abb2bf",
                       "long_instruction": "#abb2bf",
                       "pointer": "#ea6500",
                       "checkbox": "#f06800",
                       "separator": "",
                       "skipped": "#5c6370",
                       "validator": "",
                       "marker": "#f06800",
                       "fuzzy_prompt": "#c678dd",
                       "fuzzy_info": "#abb2bf",
                       "fuzzy_border": "#ea6500",
                       "fuzzy_match": "#c678dd",
                       "spinner_pattern": "#e5c07b",
                       "spinner_text": ""}, style_override=True)

    @classmethod
    def display_start_message(cls, message):
        width = Utils.get_terminal_width()
        m = Figlet(font='slant', width=width)
        printy(m.renderText("Athena AI"), 'm')
        print(message.center(width))

    @classmethod
    def get_input(cls):
        query = inquirer.text(message="", style=cls.style, qmark="≻≻", amark="≻≻").execute()
        return query

    @classmethod
    def display_response(cls, response):
        pyperclip.copy(response["choices"][0]["text"])
        print(response["choices"][0]["text"],
              "\n",
              f"Total Tokens Used: ",
              response["usage"]["total_tokens"])

    @classmethod
    def settings_ui(cls):
        pass

