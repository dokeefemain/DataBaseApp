import streamlit as st
import pymongo
import time
def app():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = myclient['millennials']
    users = db['users']
    communities = db['communities']
    posts = db['posts']
    comments = db['comments']
    username = st.text_input("Enter username")
    title = st.text_input("Enter title")
    body = st.text_area("Enter content")
    dt = time.time()
    post_dict = { "username": username, "creationdate": dt, "title": title, "content": body}
    create_post = st.button('Create post')
    if create_post:
        posts.insert_one(post_dict)
        st.write("Post has been created")