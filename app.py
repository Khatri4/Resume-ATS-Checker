import base64
from dotenv import load_dotenv
import streamlit as st
import os, sys
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input,pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # convert pdf to image
        poppler_path = 'D:\\Gen AI projects\\allGeminiBot\\resume_ats\\poppler-24.07.0\\Library\\bin'
        os.environ["PATH"] += os.pathsep + poppler_path
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        #convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/png",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
#app
st.set_page_config(page_icon="RESUME ATS")
st.header("ATS tracking system")
input_text = st.text_area("Job Description", key='input')
uploaded_file = st.file_uploader("Upload your resume", type=['pdf'])


if uploaded_file is not None:
    st.write("Resume uploaded successfully")

submit1 = st.button("Tell me about the resume")

# submit2 = st.button("How can i improvise my skills ?")

submit3 = st.button("Percentage match with JD")

input_prompt1 = '''
you are an experienced HR with tech experience in the field of Data Science, Full Stack,
Web Development, Artificial Intelligence, Machine Learning, Generative AI, Data Engineering, UI/UX
App Development, DevOps, Data Analyst. Your task is to review the provided resume against the job description.
Please share your professional evaluaion on whether the candidate's profile aligns with the role.
Highlight the strengths and weakness of the applicant in relation to the specified job requiremnets.
'''

# input_prompt2 = '''
# You are an Technical Human Resource Manager with expertise in  Data Science, Full Stack,
# Web Development, Artificial Intelligence, Machine Learning, Generative AI, Data Engineering, UI/UX
# App Development, DevOps, Data Analyst. Your role is to scrutinize the resume in light of the job description provided.
# Share your insights on the candidate's suitability for the role from an HR perspective.
# Additionally, offer advice on enhancing the candidate's skills and identify areas
# '''

input_prompt3 = '''
You are an skilled ATS(Applicant Tracking System) scanner with deep understanding of  Data Science, Full Stack,
Web Development, Artificial Intelligence, Machine Learning, Generative AI, Data Engineering, UI/UX
App Development, DevOps, Data Analyst and deep ATS functionality.
your task is to evaluate the Resume against the provided job description. give me the percentage of match if the resume matches job description and possibility of selection of the resume.
First the output should came as percentage and then keyword missing in the resume and after that possibility of resume selection.
''' 

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content,input_text)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")
