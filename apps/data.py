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
    #post_dict = {  "creationdate": post.created, "title": post.title, "content": bigPosts[count]}
    threads = posts.find().sort("creationdate", -1)
    count = 0
    for x in threads:
        count+=1
        st.write(count)
        title = x.get("title")
        body = x.get("content")
        st.write(title)
        st.write(body)
        

