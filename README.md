# Simple Streamlit Blog App

This is a simple blog application built using Streamlit. It allows users to write and view blog posts directly from the app. The app is designed to operate within the Streamlit free tier and does not require any API keys.

## Features
- **Write Blogs**: Users can create new blog posts with a title and content.
- **View Blogs**: Users can view a list of all published blogs and read their content.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamlit-blog-app.git
   cd streamlit-blog-app
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser and start writing or viewing blogs!

## Directory Structure
- `app.py`: The main Streamlit application file.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: This file.
- `blog_posts/`: Directory where blog posts are stored as Markdown files.

## Notes
- Blog posts are saved as Markdown files in the `blog_posts` directory.
- The app does not include user authentication or database storage, making it lightweight and suitable for the Streamlit free tier.