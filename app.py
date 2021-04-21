import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, account # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

""")

# Add all your application here
app.add_app("Login", home.app)
app.add_app("Create Account", account.app)
app.add_app("Feed", data.app)
app.add_app("Popular", model.app)
# The main app
app.run()
