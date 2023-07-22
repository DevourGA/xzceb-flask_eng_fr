from machinetranslation import translator
from translator import english_to_french, french_to_english
from flask import Flask

app = Flask("web_app")

@app.route("/")
def root():
    input = 'input.html'
    with open(input.html, 'r+') as readfile1:
        print(readfile1.read())
        readfile1.close()

@app.route("/englishToFrench")
english_text = str(input())
print(english_to_french(english_text))

@app.route("/frenchToEnglish")
french_text = str(input())
print(french_to_english(french_text))
