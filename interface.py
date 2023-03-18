import pyperclip
from InquirerPy.base import Choice
from InquirerPy.validator import EmptyInputValidator
from printy import printy

from functions import Utils, Settings
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
        from core import Athena
        settings = Settings.get()
        select = inquirer.select(
            message='Request settings \n'
                    'Visit the OpenAI API Documentation for details.',
            choices=[
                Choice(value=1, name=f"Model             [{settings['create_completion']['model']}]"),
                Choice(value=2, name=f"Maximum Tokens    [{settings['create_completion']['max_tokens']}]"),
                Choice(value=3, name=f"Temperature       [{settings['create_completion']['temperature']}]"),
                Choice(value=4, name=f"Top_P             [{settings['create_completion']['top_p']}]"),
                Choice(value=5, name=f"Number            [{settings['create_completion']['n']}]"),
                Choice(value=6, name=f"Stream            [{settings['create_completion']['stream']}]"),
                Choice(value=7, name=f"Log Probabilities [{settings['create_completion']['logprobs']}]"),
                Choice(value=8, name=f"Echo              [{settings['create_completion']['echo']}]"),
                Choice(value=9, name=f"Stop              [{settings['create_completion']['stop']}]"),
                Choice(value=10, name=f"Presence Penalty  [{settings['create_completion']['presence_penalty']}]"),
                Choice(value=11, name=f"Frequency Penalty [{settings['create_completion']['frequency_penalty']}]"),
                Choice(value=12, name=f"Best of           [{settings['create_completion']['best_of']}]"),
                Choice(value=13, name=f"User              [{settings['create_completion']['user']}]"),
                Choice(value=None, name="Back")
            ],
            style=cls.style,
            qmark="≻≻",
            amark="≻≻",
            default=None
        ).execute()
        if select == 1:
            model = inquirer.select(
                message='Select model:',
                choices=[
                    Choice(value='ada', name="Ada"),
                    Choice(value='babbage', name="Babbage"),
                    Choice(value='curie', name="Curie"),
                    Choice(value='curie-instruct-beta', name="Curie-instruct-beta"),
                    Choice(value='davinci', name="Davinci"),
                    Choice(value='davinci-instruct-beta', name="Davinci-instruct-beta"),
                    Choice(value='code-crushman-001', name="Code-crushman-001"),
                    Choice(value='code-davinci-002', name="Code-davinci-002"),
                    Choice(value='text-ada-001', name="Text-ada-001"),
                    Choice(value='text-babbage-001', name="Text-babbage-001"),
                    Choice(value='text-curie-001', name="Text-curie-001"),
                    Choice(value='text-davinci-001', name="Text-davinci-001"),
                    Choice(value='text-davinci-002', name="Text-davinci-002"),
                    Choice(value='text-davinci-003', name="Text-davinci-003"),
                ],
                style=cls.style,
                qmark="≻≻",
                amark="≻≻",
                default=1
            ).execute()
            settings["create_completion"]['model'] = model
            Settings.update(settings)
            cls.settings_ui()
        elif select == 2:
            max_tokens = inquirer.number(message="Enter max token value:",
                                         min_allowed=0,
                                         max_allowed=4096,
                                         validate=EmptyInputValidator(),
                                         style=cls.style,
                                         qmark="≻≻",
                                         amark="≻≻"
                                         ).execute()
            settings["create_completion"]['max_tokens'] = int(max_tokens)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 3:
            temperature = inquirer.number(message="Enter temperature value:",
                                          min_allowed=0,
                                          max_allowed=2,
                                          float_allowed=True,
                                          default=1,
                                          validate=EmptyInputValidator(),
                                          style=cls.style,
                                          qmark="≻≻",
                                          amark="≻≻"
                                          ).execute()
            settings["create_completion"]['temperature'] = float(temperature)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 4:
            top_p = inquirer.number(message="Enter top_p value:",
                                    min_allowed=0,
                                    max_allowed=1,
                                    float_allowed=True,
                                    default=1,
                                    validate=EmptyInputValidator(),
                                    style=cls.style,
                                    qmark="≻≻",
                                    amark="≻≻"
                                    ).execute()
            settings["create_completion"]['top_p'] = float(top_p)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 5:
            n = inquirer.number(message="Enter n value:",
                                min_allowed=1,
                                default=1,
                                validate=EmptyInputValidator(),
                                style=cls.style,
                                qmark="≻≻",
                                amark="≻≻"
                                ).execute()
            settings["create_completion"]['n'] = int(n)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 6:
            stream = inquirer.confirm(message='Press y for True & n for False.', default=False,
                                      style=cls.style, qmark="≻≻", amark="≻≻").execute()
            settings["create_completion"]['stream'] = stream
            Settings.update(settings)
            cls.settings_ui()
        elif select == 7:
            logprob = inquirer.number(message="Enter logprob value:",
                                      min_allowed=None,
                                      max_allowed=5,
                                      default=None,
                                      style=cls.style,
                                      qmark="≻≻",
                                      amark="≻≻"
                                      ).execute()
            settings["create_completion"]['logprob'] = logprob
            Settings.update(settings)
            cls.settings_ui()
        elif select == 8:
            echo = inquirer.confirm(message='Press y for True & n for False.', default=False,
                                    style=cls.style, qmark="≻≻", amark="≻≻").execute()
            settings["create_completion"]['echo'] = echo
            Settings.update(settings)
            cls.settings_ui()
        elif select == 9:
            stop = inquirer.text(message="Enter up to 4 sequences seperated by spaces:",
                                 style=cls.style, qmark="≻≻", amark="≻≻").execute()
            if stop == '':
                settings["create_completion"]['stop'] = None
            else:
                settings["create_completion"]['stop'] = stop.split(' ')
            Settings.update(settings)
            cls.settings_ui()
        elif select == 10:
            presence_penalty = inquirer.number(message="Enter presence penalty value:",
                                               min_allowed=-2,
                                               max_allowed=2,
                                               float_allowed=True,
                                               default=0,
                                               validate=EmptyInputValidator(),
                                               style=cls.style,
                                               qmark="≻≻",
                                               amark="≻≻"
                                               ).execute()
            settings["create_completion"]['presence_penalty'] = float(presence_penalty)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 11:
            frequency_penalty = inquirer.number(message="Enter frequency penalty value:",
                                                min_allowed=-2,
                                                max_allowed=2,
                                                float_allowed=True,
                                                default=0,
                                                validate=EmptyInputValidator(),
                                                style=cls.style,
                                                qmark="≻≻",
                                                amark="≻≻"
                                                ).execute()
            settings["create_completion"]['frequency_penalty'] = float(frequency_penalty)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 12:
            best_of = inquirer.number(message="Enter best of value:",
                                      min_allowed=1,
                                      default=1,
                                      validate=EmptyInputValidator(),
                                      style=cls.style,
                                      qmark="≻≻",
                                      amark="≻≻"
                                      ).execute()
            settings["create_completion"]['best_of'] = int(best_of)
            Settings.update(settings)
            cls.settings_ui()
        elif select == 13:
            user = inquirer.text(message="Enter username:", style=cls.style, qmark="≻≻", amark="≻≻").execute()
            settings["create_completion"]['user'] = user
            Settings.update(settings)
            cls.settings_ui()
        elif select is None:
            ai = Athena()
            ai.run()

