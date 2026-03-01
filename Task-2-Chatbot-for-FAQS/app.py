
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------
# 1️⃣ Load FAQ Data
# ---------------------------------
faq_df = pd.read_csv("faq_data.csv")

# ---------------------------------
# 2️⃣ Initialize Session State
# ---------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# ---------------------------------
# 3️⃣ Sidebar - Category Selection
# ---------------------------------
st.sidebar.title("FAQ Categories")

categories = faq_df["Category"].unique()
selected_category = st.sidebar.selectbox("Choose Category", categories)

# Filter questions by category
filtered_df = faq_df[faq_df["Category"] == selected_category]

# ---------------------------------
# 4️⃣ Sidebar - Quick Questions
# ---------------------------------
st.sidebar.write("Quick Questions:")

for question in filtered_df["Question"]:
    if st.sidebar.button(question):
        st.session_state.input_value = question

# ---------------------------------
# 5️⃣ Sidebar - Clear Chat
# ---------------------------------
if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []

# ---------------------------------
# 6️⃣ Main Title
# ---------------------------------
st.title("Smart FAQ Chatbot")

# Input box (reads from session_state)
user_input = st.text_input(
    "Type your question:",
    value=st.session_state.input_value
)

# ---------------------------------
# 7️⃣ When Send is Clicked
# ---------------------------------
if st.button("Send") and user_input.strip() != "":

    questions = filtered_df["Question"]
    answers = filtered_df["Answer"]

    # Convert FAQ questions into vectors
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)

    # Convert user question into vector
    user_vector = vectorizer.transform([user_input])

    # Compare similarity
    similarity = cosine_similarity(user_vector, X)

    best_index = similarity.argmax()
    best_score = similarity[0][best_index]

    # Decide response
    if best_score < 0.5:
        response = "Please contact customer care for further assistance."
    else:
        response = answers.iloc[best_index]

    # Save conversation
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

    # Clear input after sending
    st.session_state.input_value = ""

# ---------------------------------
# 8️⃣ Display Chat History
# ---------------------------------
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")