# ai-text-completion-project

This is a simple Python application that allows users to interactively generate text completions using a Hugging Face language model. The app accepts user prompts, sends them to the model via the Hugging Face API, and displays generated responses. It supports multiple prompts per session and includes basic input validation and error handling.

---

## Features

- Interactive prompt input via terminal or notebook cell
- Customizable generation parameters: `max_tokens`, `temperature`, and `top_p`
- Handles API errors and invalid inputs
- Allows multiple prompt submissions in one session

---

## Dependencies

- Python 3.7+
- `transformers` library
- `huggingface_hub`
