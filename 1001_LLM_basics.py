from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def generate_text(prompt: str, max_tokens: int = 50) -> str:
    # Ładujemy tokenizer i model
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")

    # Tokenizacja promptu
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generowanie tekstu
    outputs = model.generate(inputs, max_length=max_tokens, do_sample=True, temperature=0.7)

    # Dekodowanie wynikowego tekstu
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    user_prompt = "Jeszcze Polska nie zginęła kiedy"
    generated = generate_text(user_prompt)
    print(generated)