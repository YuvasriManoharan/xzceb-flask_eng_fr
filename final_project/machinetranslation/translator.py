from translate import Translator

# Create an instance of the Translator


def english_to_french(english_text):
    translator = Translator(from_lang="en", to_lang="fr")
    try:
        # Use the translate method to translate the text from English to French
        french_text = translator.translate(english_text)
        return french_text
    except Exception as e:
        # Handle any errors that may occur during translation
        print("Error during translation:", e)
        return None

def french_to_english(french_text):
    translator = Translator(from_lang="fr", to_lang="en")
    try:
        # Use the translate method to translate the text from French to English
        english_text = translator.translate(french_text)
        return english_text
    except Exception as e:
        # Handle any errors that may occur during translation
        print("Error during translation:", e)
        return None
