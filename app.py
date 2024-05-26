import streamlit as st
from transformers import pipeline

st.title("Text Generation Tool")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

user_input = st.text_area("Enter a prompt to generate text:", height=200)
if user_input:
    generated_text = model(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    st.write("Generated Text:")
    st.write(generated_text)
