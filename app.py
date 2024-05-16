import streamlit as st
from transformers import pipeline

# Load a pre-trained sentiment-analysis pipeline from Hugging Face
sentiment_analysis = pipeline("sentiment-analysis")

# Set the title of the Streamlit app
st.title("Sentiment Analysis App")

# Prompt the user to input text
user_input = st.text_area("Enter text to analyze sentiment", "")

# Create a button to trigger the sentiment analysis
if st.button("Analyze"):
    if user_input:
        # Use the model to make a prediction
        results = sentiment_analysis(user_input)
        # Display the results
        for result in results:
            st.write(f"Label: {result['label']}, Score: {result['score']:.2f}")
    else:
        st.write("Please enter some text to analyze.")
