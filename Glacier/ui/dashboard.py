import streamlit as st

st.set_page_config(page_title="Esports News Summarizer", layout="wide")
st.title("Esports News Summarizer Dashboard")

st.sidebar.header("Filters")
st.sidebar.multiselect("Game", options=["Dota 2", "CS:GO", "LoL", "Valorant"])
st.sidebar.multiselect("Region", options=["NA", "EU", "Asia", "Global"])
st.sidebar.multiselect("Type", options=["Result", "Transfer", "Feature", "Rumor", "Business"])

st.header("Latest News")
st.info("News articles will appear here.")

st.header("QA/Admin Panel")
st.info("QA and admin controls will appear here.")