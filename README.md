# 📄 Resume ATS Tracker using Google Gemini AI

Welcome to the **Resume ATS Tracker** project! This tool leverages the power of **Google's Gemini AI** to help you evaluate resumes against specific job descriptions, providing insights and analysis using advanced AI models. Whether you're an HR professional, recruiter, or job seeker, this app will assist in analyzing how well a resume matches job requirements.

## 🌟 Features

- **Upload your resume** in PDF format and get it evaluated using AI
- **Analyze the resume** against a job description (JD) to get valuable insights
- **Percentage match** with JD along with missing keywords to enhance your resume
- **Strengths and weaknesses** of the resume based on job requirements
- Powered by **Google Gemini AI (Gemini 1.5 Flash)**

## 🛠️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Khatri4/resume-ats-tracker.git
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

This project uses Google's Gemini API, so you'll need to create a `.env` file in the root directory. Add your **Google Gemini API key**:

```
GOOGLE_API_KEY=your-api-key-here
```

> ⚠️ **Note:** You need to use your own Google API key. If you don't have one, you can get it from the [Google Cloud Console](https://console.cloud.google.com/).

### 4. Install Poppler

This project uses **Poppler** for PDF to image conversion. Download the latest version of Poppler for Windows [here](https://github.com/oschwartz10612/poppler-windows/releases/).

After downloading, extract the folder and **add the `bin` folder to your system's PATH**:
1. Copy the path to the `bin` folder (e.g., `C:\path-to-poppler\poppler-xx.x.0\Library\bin`).
2. Go to **Control Panel** > **System and Security** > **System** > **Advanced system settings**.
3. Click on **Environment Variables**, then under **System variables**, find the `Path` variable, select it, and click **Edit**.
4. Click **New** and paste the path to Poppler's `bin` folder.
5. Click **OK** to close all dialogs.

### 5. Run the Application

Once everything is set up, run the Streamlit app:

```bash
streamlit run app.py
```

The application will start, and you can access it in your browser at `http://localhost:8501`.

## 📥 Uploading Your Resume

- Click the "Upload your resume" button to upload a **PDF**.
- Enter the **Job Description** you want to compare your resume against.
- Choose from the following options:
  - **Tell me about the resume**: Get detailed feedback on the strengths and weaknesses of your resume.
  - **Percentage match with JD**: See how well your resume matches the job description and get a list of missing keywords.

## ✨ Example Output

- **Tell me about the resume**: Get a thorough review of your resume, highlighting relevant skills and areas of improvement.
- **Percentage match with JD**: Get a percentage match score with a breakdown of missing keywords and the likelihood of selection based on the job description.

## ⚙️ Technologies Used

- **Python** 🐍
- **Streamlit** for creating interactive web apps 📊
- **Google Generative AI (Gemini)** for content generation 🤖
- **PDF2Image** for converting PDF resumes into images 📄
- **Pillow (PIL)** for image processing 🖼️
- **Poppler** for PDF conversion 📑

## 🎯 Roadmap

- [ ] Add skill enhancement recommendations
- [ ] Support for multiple resumes comparison
- [ ] Include support for additional file types (Word, Text)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🌟 If you like this project, don’t forget to give it a star!
