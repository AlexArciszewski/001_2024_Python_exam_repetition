from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Załaduj model GPT-2 i tokenizer
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Ustawienie pad_token_id na eos_token_id
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = model.config.eos_token_id

# Prompt z bardziej określonym kierunkiem
prompt = "Hi. How is going?"

# Tokenizowanie tekstu z paddingiem
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

# Generowanie odpowiedzi z kontrolowanymi parametrami
outputs = model.generate(
    input_ids=inputs["input_ids"],
    max_length=100,
    num_beams=5,
    no_repeat_ngram_size=3,
    temperature=0.5,
    top_p=0.8,
    do_sample=True,  # Włączanie sample
    early_stopping=True
)

# Dekodowanie wygenerowanego tekstu
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Drukowanie wygenerowanego tekstu
print(generated_text)