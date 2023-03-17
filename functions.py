import json
import os


class Utils:

    @classmethod
    def get_terminal_width(cls):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 80


class Settings:
    @classmethod
    def get(cls):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        return settings

    @classmethod
    def update(cls, settings):
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
