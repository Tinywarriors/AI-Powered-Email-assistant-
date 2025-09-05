import streamlit as st
import pandas as pd
from processor import categorize_email, prioritize_email, draft_reply

# Load data
df = pd.read_csv("emails.csv")

# Process
df["Category"] = df.apply(lambda x: categorize_email(x["subject"], x["body"]), axis=1)
df["Priority"] = df["body"].apply(prioritize_email)
df["Draft Reply"] = df["Category"].apply(draft_reply)

# Dashboard
st.title("📧 AI-Powered Email Assistant")
st.metric("Total Emails", len(df))
st.metric("Urgent Emails", len(df[df["Priority"] == "Urgent"]))

st.subheader("Processed Emails")
st.dataframe(df[["sender", "subject", "Category", "Priority", "Draft Reply"]])

st.subheader("⚡ Urgent Emails")
urgent_df = df[df["Priority"] == "Urgent"]
st.table(urgent_df[["sender", "subject", "Category", "Draft Reply"]])
