from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text_translated = translator.english_to_french(textToTranslate)
…    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
