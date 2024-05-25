import streamlit as st
from transformers import pipeline

st.title("Text Summarization Tool")

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("summarization")

model = load_model()

user_input = st.text_area("Enter text to summarize:", height=200)
if user_input:
    summary = model(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    st.write("Summary:")
    st.write(summary)
