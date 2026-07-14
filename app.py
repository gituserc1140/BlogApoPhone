import streamlit as st
import os
import datetime

# Directory to store blog posts
BLOG_DIR = "blog_posts"

# Ensure the blog directory exists
os.makedirs(BLOG_DIR, exist_ok=True)

def save_blog(title, content):
    filename = f"{title}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    filepath = os.path.join(BLOG_DIR, filename)
    with open(filepath, "w") as file:
        file.write(f"# {title}\n\n{content}")

def list_blogs():
    return sorted([f for f in os.listdir(BLOG_DIR) if f.endswith(".md")], reverse=True)

def read_blog(filename):
    filepath = os.path.join(BLOG_DIR, filename)
    with open(filepath, "r") as file:
        return file.read()

st.title("Simple Streamlit Blog")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Write a Blog", "View Blogs"])

if page == "Write a Blog":
    st.header("Write a New Blog")
    title = st.text_input("Blog Title")
    content = st.text_area("Blog Content", height=300)
    if st.button("Publish Blog"):
        if title and content:
            save_blog(title, content)
            st.success("Blog published successfully!")
        else:
            st.error("Please fill in both title and content.")

elif page == "View Blogs":
    st.header("View Blogs")
    blogs = list_blogs()
    if blogs:
        selected_blog = st.selectbox("Select a blog to read", blogs)
        st.markdown(read_blog(selected_blog))
    else:
        st.info("No blogs available. Write one!")