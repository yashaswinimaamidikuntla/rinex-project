import streamlit as st
import joblib
model=joblib.load('twitter-analysis')
st.title('twitter-analysis CLASSIFIER')
ip=st.text_input('Enter your text')
op=model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
