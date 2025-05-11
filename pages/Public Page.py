import streamlit as st
import json
import os

st.set_page_config(page_title="Link Bio Publik", layout="centered")

st.title("🌐 Halaman Publik Link Bio")

username = st.text_input("Masukkan username:", "")

if username:
    file_path = f"saved_pages/{username}.json"
    if not os.path.exists(file_path):
        st.error("Halaman tidak ditemukan.")
    else:
        with open(file_path, "r") as f:
            data = json.load(f)
        
        st.markdown(f"## {data['title']}")
        st.markdown(f"**@{data['username']}**")
        st.markdown("---")
        for link in data["links"]:
            st.markdown(f"🔗 [{link['label']}]({link['url']})")
