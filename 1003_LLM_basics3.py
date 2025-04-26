#Model dokończy zdanie „Hi. How is going?” i spróbuje napisać coś sensownego w stylu ludzkim.
from transformers import GPT2LMHeadModel, GPT2Tokenizer


model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#Ładuje gotowy model distilgpt2 (mniejsza i szybsza wersja GPT-2) oraz jego tokenizer.Tokenizator to tłumacz między tekstem a liczbami, który:
#Zamienia tekst (np. zdanie) na liczby zrozumiałe dla modelu językowego.
#Zamienia z powrotem liczby na tekst, który możesz przeczytać.

# Ustawia znak końca tekstu jako „wypełniacz”, żeby model wiedział jak traktować puste miejsca w tekście.
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = model.config.eos_token_id

#Zamienia tekst na liczby, które model potrafi zrozumieć (tokenizacja).
prompt = "Hi. How is going?"
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)


outputs = model.generate(
    input_ids=inputs["input_ids"],
    max_length=100,         #maks. długość odpowiedzi
    num_beams=5,            # przeszukiwanie różnych możliwych ścieżek odpowiedzi (lepsza jakość)
    no_repeat_ngram_size=3, #nie powtarza 3-wyrazowych fragmentów
    temperature=0.5,        #mniej losowości (niższa wartość = bardziej „pewny” model)
    top_p=0.8,              # wybiera tylko najpewniejsze słowa (kontrola kreatywności)
    do_sample=True,
    early_stopping=True
)
# Zamienia wygenerowane liczby z powrotem na tekst i go wyświetla.
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)