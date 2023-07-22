from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    french_text = MyMemoryTranslator(source='en',target='fr').tanslate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    english_test = MyMemoryTranslator(source='fr',target='en').translate(english_test)
    print(english_text)
    return english_text
