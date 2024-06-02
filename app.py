import streamlit as st
import io
from pdf_processing import load_pdf_text
from answer_logic import get_random_answer

# Set page configuration
st.set_page_config(page_title="CourseQuest 🗺️", page_icon=":books:", layout="wide")

# Main title
st.title("CourseQuest 🗺️")
st.markdown("## Your Interactive Course Catalog Assistant")

# Sidebar for file upload
st.sidebar.header("Upload Course Catalog PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

# Initialize session state for catalog text
if 'catalog_text' not in st.session_state:
    st.session_state['catalog_text'] = ""

# Load PDF and extract text
if uploaded_file and st.session_state['catalog_text'] == "":
    with st.spinner('Loading PDF...'):
        pdf_stream = io.BytesIO(uploaded_file.read())
        catalog_text = load_pdf_text(pdf_stream)
        st.session_state['catalog_text'] = catalog_text
        st.success('PDF loaded successfully!')

# User question input
st.markdown("### Ask a Question About the Course Catalog")
user_question = st.text_input("Enter your question here:")

# Button to get answer
if st.button("Get Answer"):
    if user_question:
        answer = get_random_answer()
        st.markdown(f"**Question:** {user_question}")
        st.markdown(f"**Answer:** {answer}")
    else:
        st.error("Please enter a question.")
