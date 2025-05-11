import streamlit as st
import json
import uuid
from pathlib import Path

st.set_page_config(page_title="Mini Link Bio", layout="centered")

st.title("🔗 Link Bio Builder")

st.subheader("📝 Informasi Umum")
username = st.text_input("Username unik", key="username")
page_title = st.text_input("Judul halaman", key="page_title")
profile_pic = st.file_uploader("Upload foto profil (opsional)", type=["jpg", "png"])

st.subheader("🔗 Daftar Link")
if "links" not in st.session_state:
    st.session_state.links = []

def add_link():
    st.session_state.links.append({"label": "", "url": ""})

def remove_link(index):
    st.session_state.links.pop(index)

st.button("➕ Tambah Link", on_click=add_link)

for i, link in enumerate(st.session_state.links):
    col1, col2, col3 = st.columns([3, 5, 1])
    with col1:
        label = st.text_input(f"Nama Link {i+1}", value=link["label"], key=f"label_{i}")
    with col2:
        url = st.text_input(f"URL {i+1}", value=link["url"], key=f"url_{i}")
    with col3:
        if st.button("❌", key=f"del_{i}"):
            remove_link(i)
            st.experimental_rerun()
    st.session_state.links[i] = {"label": label, "url": url}

if st.button("👀 Lihat Preview"):
    st.markdown("---")
    st.subheader("🔍 Preview Halaman")
    if profile_pic:
        st.image(profile_pic, width=100)
    st.markdown(f"## {page_title}")
    for link in st.session_state.links:
        st.markdown(f"🔗 [{link['label']}]({link['url']})")

if st.button("💾 Simpan Link Page"):
    data = {
        "id": str(uuid.uuid4()),
        "username": username,
        "title": page_title,
        "links": st.session_state.links,
    }

    Path("saved_pages").mkdir(exist_ok=True)
    with open(f"saved_pages/{username}.json", "w") as f:
        json.dump(data, f, indent=2)

    st.success(f"Halaman {username} berhasil disimpan!")
