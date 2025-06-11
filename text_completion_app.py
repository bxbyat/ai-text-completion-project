from transformers import pipeline, set_seed
from huggingface_hub import login
import os

generator = pipeline("text-generation", model="gpt2")

set_seed(42)

def get_user_input():
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            return None
        if not prompt:
            print("Please enter a non-empty prompt.")
            continue
        if len(prompt) > 1000:
            print("Prompt is too long. Try to shorten it.")
            continue
        return prompt

def get_generation_settings():
    try:
        max_length = int(input("Max tokens (default 100): ") or "100")
        temperature = float(input("Temperature (default 1.0): ") or "1.0")
        top_p = float(input("Top-p (default 0.9): ") or "0.9")
        return max_length, temperature, top_p
    except ValueError:
        print("Invalid input for settings. Using default values.")
        return 100, 1.0, 0.9

def generate_text(prompt, max_length=100, temperature=1.0, top_p=0.9):
    try:
        output = generator(
            prompt,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            num_return_sequences=1
        )
        print("\n📝 Generated Text:\n" + output[0]['generated_text'])
    except Exception as e:
        print(f"Error generating text: {e}")

print("Type 'exit' to quit the app.")

while True:
    prompt = get_user_input()
    if prompt is None:
        print("Goodbye!")
        break

    max_len, temp, top_p = get_generation_settings()
    generate_text(prompt, max_length=max_len, temperature=temp, top_p=top_p)
