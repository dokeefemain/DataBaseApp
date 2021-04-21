import streamlit as st
from multiapp import MultiApp
from apps import home, data, account, create, comments # import your app modules here

app = MultiApp()

st.markdown("""
# Strawberry

Where millennials have fun

""")

# Add all your application here
app.add_app("Login", home.app)
app.add_app("Create Account", account.app)
app.add_app("Make new post", create.app)
app.add_app("Comment on post", comments.app)
app.add_app("Feed", data.app)
#app.add_app("Popular", model.app)

# The main app
app.run()
