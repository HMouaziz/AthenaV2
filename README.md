# AthenaV2 Documentation

## Overview

A program i created to learn about the openai api and chatbots in general, AthenaV2 is an AI-driven chatbot built using OpenAI's GPT-3, designed to simulate a conversation with Athena, the ancient Greek goddess associated with wisdom, warfare, and handicraft. Athena aims to provide helpful responses, expanding her knowledge through interactions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HMouaziz/AthenaV2.git
    cd AthenaV2
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    - Replace `# SET API KEY` in the `Athena` class with your actual OpenAI API key.

## Usage

### Running Athena

To start the Athena chatbot, run the following command:
```sh
python -m core
```

This will initialize the Athena application and begin an interactive session where you can type queries and receive responses.

### Example Code

```python
from core import Athena

if __name__ == '__main__':
    app = Athena()
    app.run(startup=True)
```

## Configuration

Athena uses a `settings.json` file to configure the OpenAI API parameters. Below is an example configuration:

```json
{
    "model": "text-davinci-003",
    "prompt": null,
    "max_tokens": 3000,
    "temperature": 0.8,
    "top_p": 1.0,
    "n": 1,
    "stream": false,
    "logprobs": null,
    "echo": null,
    "stop": ["\n"],
    "presence_penalty": 0.3,
    "frequency_penalty": 0.0,
    "best_of": 1,
    "user": ""
}
```

You can modify this file to adjust the chatbot's behavior.

### Changing Settings

To change the request settings interactively, type `settings` or `open settings` during the chat. You will be presented with a menu to adjust various parameters such as model, max tokens, temperature, and more.

## Class and Method Overview

### Athena Class

The `Athena` class is responsible for handling the main logic of the chatbot.

#### Methods:

- **__init__(self)**: Initializes the chatbot with the necessary settings.
- **run(self, startup=False)**: Starts the chatbot's main loop.
- **create_request(self, query)**: Creates a request prompt for the OpenAI API.
- **run_request(self)**: Sends the request to the OpenAI API and retrieves the response.
- **append_chat_log(self, query, response)**: Appends the current interaction to the chat log.
- **erase_last_log(self)**: Erases the last logged interaction.

### Interface Class

The `Interface` class handles the user interface and input/output operations.

#### Methods:

- **display_start_message(cls, message)**: Displays the start message.
- **get_input(cls)**: Gets input from the user.
- **display_response(cls, response)**: Displays the response to the user.
- **settings_ui(cls)**: Provides a UI for changing settings.

### Settings Class

The `Settings` class manages the configuration settings.

#### Methods:

- **get(cls)**: Retrieves the current settings from `settings.json`.
- **update(cls, settings)**: Updates the settings in `settings.json`.

### Utils Class

The `Utils` class provides utility functions.

#### Methods:

- **get_terminal_width(cls)**: Gets the terminal width for formatting output.

## Example Interaction

```text
≻≻ Hello, who are you?
Athena: I am Athena, collector and guardian of knowledge. How can I help you?

≻≻ What is the capital of France?
Athena: The capital of France is Paris.
```

## Exiting the Chatbot

To exit the chatbot, type any of the following commands:
- `/q`
- `quit`
- `exit`
- `-q`
- `bye`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the GPT-3 model.

Developed by Halim Mouaziz @ project-hephaestus.com © 2024
