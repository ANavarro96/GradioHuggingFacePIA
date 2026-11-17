from transformers import pipeline

modelo1 = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

modelo2 = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

texto = "Man, this guy sucks..."

print(modelo1(texto))
print(modelo2(texto))