import streamlit as st
import pymongo
from datetime import datetime
def app():
    #
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = myclient['millennials']
    users = db['users']
    communities = db['communities']
    posts = db['posts']
    comments = db['comments']

    st.write('Welcome to millenials!')
    username_in = st.text_input("Enter username")
    pass_in = st.text_input("Enter password")
    login = st.button('login')
    usertest = False
    if login:
        user_pass = users.find( {"username": username_in} )[0].get("pass")
        if pass_in == user_pass:
            st.write('Correct password')
            threads = posts.find({'username': username_in}).sort("creationdate", -1)
            st.header('Posts created by '+username_in)
            for x in threads:
                st.write("Post ID",x.get("creationdate"))
                title = x.get("title")
                body = x.get("content")
                comment = comments.find({"post_id": str(x.get("creationdate"))})
                count = 0
                st.write(title)
                st.write("--",body)
        else:
            st.write('Incorrect password')

