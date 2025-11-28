RESUME SCREENING AI AGENT
An intelligent AI-powered resume screening system built using Streamlit, OpenAI, and Python.
This tool extracts content from resumes, analyzes job descriptions, evaluates candidate fit, and produces detailed screening reports automatically.
FEATURES
Upload & Extract Text
Supports PDF/DOCX resume extraction using pdfplumber and python-docx.
AI-Powered Screening
Uses OpenAI LLM to evaluate:
  Skill match
  Experience relevance
  Strengths & weaknesses
  Overall candidate fit score
  Job Description Parsing
Upload job descriptions → Automatically summarizes required skills.
Clear and Structured Output
  Summary
  Skills match score
  Missing skills
  Overall rating
  Recommendation (Hire / Consider / Reject)
Interactive UI
Built using Streamlit for a clean and intuitive interface.

HOW IT WORKS?
Upload a resume (PDF/DOCX)
Upload or paste a job description
AI processes and evaluates candidate fit
Instant result on the screen
Optionally download the evaluation report

TECH STACK
| Component    | Technology              |
| ------------ | ----------------------- |
| Frontend     | Streamlit               |
| Backend      | Python                  |
| AI Model     | OpenAI GPT              |
| File Parsing | pdfplumber, python-docx |
| Packaging    | requirements.txt        |

PROJECT STRUCTURE
resume-screening-agent/
│── app.py                # Main Streamlit application
│── utils.py              # Helper functions
│── requirements.txt      # Dependencies
│── job_description/
│     ├── JD_Data_Scientist.pdf
│     ├── JD_Python_Developer.pdf
│     └── JD_DevOps_Engineer.pdf
│── README.md

Running the Project Locally
1. Clone the repository
git clone https://github.com/vpavithra1435/resume-screening-agent.git
cd resume-screening-agent

2. Install dependencies
pip install -r requirements.txt

3. Add your OpenAI API key

Create a .env file:

OPENAI_API_KEY=your_key_here

4. Run the app
streamlit run app.py

USES CASES
HR recruiters automating resume screening
Students evaluating their resumes
Companies doing bulk resume filtering
Skill gap analysis for job seekers

FUTURE ENHANCEMENT
Export results as PDF
Support for multiple resumes at once
ATS scoring
Integrate Gemini/Claude models
Deploy to Streamlit Cloud
