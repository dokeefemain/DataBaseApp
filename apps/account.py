import streamlit as st
def app():
    #Create account stuff here
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = myclient['millennials']
    users = db['users']
    communities = db['communities']
    posts = db['posts']
    comments = db['comments']

    st.write('Welcome to millenials!')
    username_in = st.text_input("Enter username")
    pass_in = st.text_input("Enter password")
    login = st.button('Create Account')
    usertest = False
    if login:
        username_dict = {'username': username_in, 'pass': pass_in}
        users.insert_one(username_dict)
    