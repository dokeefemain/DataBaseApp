import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import pymongo
#feed
def app():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = myclient['millennials']
    users = db['users']
    communities = db['communities']
    posts = db['posts']
    comments = db['comments']
    username_in = st.text_input("Enter usernamme")
    post_id_in = st.text_input("Enter post ID")
    comment_in = st.text_input("Enter comment")
    if st.button("Add comment"):
        comment_dict = {"username": username_in, "post_id": post_id_in, "comment": comment_in}
        comments.insert_one(comment_dict)
        st.write("Comment has been created")
