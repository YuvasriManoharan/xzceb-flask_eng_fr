from machinetranslation import translator
from flask import Flask, render_template, request, jsonify

app = Flask("Web Translator")

@app.route('/englishToFrench')
def translate_english_to_french():
    text_to_translate = request.args.get('textToTranslate', '')
    french_translation = translator.english_to_french(text_to_translate)
    return jsonify({"translatedText": french_translation})

@app.route('/frenchToEnglish')
def translate_french_to_english():
    text_to_translate = request.args.get('textToTranslate', '')
    english_translation = translator.french_to_english(text_to_translate)
    return jsonify({"translatedText": english_translation})

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
