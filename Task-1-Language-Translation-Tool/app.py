import streamlit as st
from deep_translator import GoogleTranslator

# Page config (MUST be first Streamlit command)
st.set_page_config(page_title="AI Translator", page_icon="🌍", layout="centered")

# Custom Background CSS
page_bg = """
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}
div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌍 AI Language Translator")
st.write("Translate text instantly using AI technology")

# Language dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn"
}

source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

text = st.text_area("Enter text to translate")

if st.button("Translate"):
    if text:
        translator = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        )

        translated_text = translator.translate(text)

        st.success("Translation Completed ✅")
        st.write("### Translated Text:")
        st.write(translated_text)
    else:
        st.warning("Please enter some text.")
