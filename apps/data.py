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
    
    for x in threads:
        
        st.write("Post ID",x.get("creationdate"))
        title = x.get("title")
        body = x.get("content")
        comment = comments.find({"post_id": str(x.get("creationdate"))})
        count = 0
        st.write(title)
        st.write("--",body)
        for y in comment:
            count +=1
            st.write("----",y.get("comment"))
        

