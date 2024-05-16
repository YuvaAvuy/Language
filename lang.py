pip install streamlit googletrans gtts
import streamlit as st
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import IPython.display as ipd


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp


def main():
    st.title("South Indian Language Translator with Pronunciation")

    # Input text
    input_text = st.text_area("Enter text to translate")

    # Select target language
    target_language = st.selectbox("Select target language", ["Hindi", "Tamil", "Telugu", "Malayalam", "Kannada"])

    # Translate button
    if st.button("Translate"):
        if target_language == "Hindi":
            translated_text = translate_text(input_text, "hi")
            language_code = "hi"
        elif target_language == "Tamil":
            translated_text = translate_text(input_text, "ta")
            language_code = "ta"
        elif target_language == "Telugu":
            translated_text = translate_text(input_text, "te")
            language_code = "te"
        elif target_language == "Malayalam":
            translated_text = translate_text(input_text, "ml")
            language_code = "ml"
        elif target_language == "Kannada":
            translated_text = translate_text(input_text, "kn")
            language_code = "kn"

        # Display translated text
        st.text_area("Translated Text", translated_text, height=200)

        # Pronunciation feature
        st.subheader("Listen to Pronunciation")
        st.audio(text_to_speech(translated_text, language_code), format='audio/mp3')


if __name__ == "__main__":
    main()
