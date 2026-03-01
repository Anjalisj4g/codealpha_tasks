🤖 FAQ Chatbot using Streamlit

An interactive FAQ Chatbot built using Python and Streamlit.
This chatbot answers user questions by matching them with predefined FAQs using TF-IDF vectorization and Cosine Similarity.

The system intelligently finds the most relevant answer and displays it in a chat-style interface.

## 🌐 Live Demo  
👉 https://anjali-faq-chatbot.streamlit.app/

🚀 Features

Interactive chat interface

Sidebar with FAQ categories

Quick question buttons

Chat history support

Clear chat option

Similarity-based question matching

Fallback response for unknown queries

Beginner-friendly implementation

🛠️ Technologies Used

Python

Streamlit

Pandas

Scikit-learn (TF-IDF & Cosine Similarity)

🧠 How the Chatbot Works

User selects a category from the sidebar.

User types a question.

The chatbot converts both FAQ questions and user query into numerical vectors using TF-IDF.

Cosine similarity is calculated to find the most similar question.

If similarity score crosses a defined threshold → the matching answer is displayed.

If no match is found →
"Please contact customer care for further assistance."

📂 Project Files

app.py – Main Streamlit application

faq_data.csv – FAQ dataset

requirements.txt – Required libraries

📈 Learning Outcomes

This project helped me understand:

Basic NLP concepts

Text vectorization

Cosine similarity logic

Streamlit UI development

Building beginner-friendly chatbot systems

🎯 Future Improvements

Improve similarity matching

Add database integration

Deploy the chatbot online

Enhance UI styling

👩‍💻 Author

Anjali J.
Aspiring Data Analyst | Python Enthusiast
