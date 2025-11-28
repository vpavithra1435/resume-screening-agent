import streamlit as st
import pandas as pd
import os
from utils import extract_text, score_resumes, generate_job_description, mock_generate_job_description, mock_score_resumes

st.set_page_config(page_title="Resume Screening AI Agent", layout="wide")

st.title("📄 Resume Screening AI Agent")
st.markdown("Upload resumes and a job description to get AI-powered rankings and insights.")

# Sidebar for Configuration
with st.sidebar:
    st.header("Configuration")
    
    # Demo Mode Toggle
    demo_mode = st.checkbox("Enable Demo Mode (No API Key required)")
    
    api_key = ""
    if not demo_mode:
        # Check for env var
        env_api_key = os.getenv("GOOGLE_API_KEY")
        api_key = st.text_input("Enter Google Gemini API Key", value=env_api_key if env_api_key else "", type="password")
        if not api_key:
            st.warning("API Key is required to use the AI features.")
        st.info("Get your API key from [Google AI Studio](https://aistudio.google.com/)")
    else:
        st.success("Demo Mode Enabled: Using simulated AI responses.")

# Main Content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Job Description")
    jd_source = st.radio("Select Job Description Source:", ["Paste Text", "Upload File", "Generate with AI"], horizontal=True)
    
    job_description = ""
    
    if jd_source == "Paste Text":
        job_description = st.text_area("Paste the Job Description (JD) here", height=300)
    elif jd_source == "Upload File":
        jd_file = st.file_uploader("Upload Job Description (PDF/DOCX)", type=["pdf", "docx"])
        if jd_file:
            job_description = extract_text(jd_file)
            if job_description:
                st.success("Job Description extracted successfully!")
                with st.expander("View Extracted JD"):
                    st.write(job_description)
            else:
                st.error("Could not extract text from the uploaded file.")
    elif jd_source == "Generate with AI":
        role = st.text_input("Enter Job Role / Title (e.g., 'Senior Python Developer')")
        if st.button("Generate Job Description"):
            if not api_key and not demo_mode:
                st.error("Please enter your API Key in the sidebar first.")
            elif not role:
                st.error("Please enter a job role.")
            else:
                with st.spinner("Generating Job Description..."):
                    if demo_mode:
                        job_description = mock_generate_job_description(role)
                    else:
                        job_description = generate_job_description(role, api_key)
                    st.session_state['generated_jd'] = job_description
        
        # Persist generated JD
        if 'generated_jd' in st.session_state:
            job_description = st.text_area("Generated Job Description", value=st.session_state['generated_jd'], height=300)

with col2:
    st.subheader("2. Upload Resumes")
    uploaded_files = st.file_uploader("Upload PDF or DOCX resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Analyze Resumes", type="primary"):
    if not api_key and not demo_mode:
        st.error("Please enter your Google Gemini API Key in the sidebar.")
    elif not job_description:
        st.error("Please provide a Job Description.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        with st.spinner("Analyzing resumes... This may take a moment."):
            # 1. Extract Text
            resumes_data = []
            for uploaded_file in uploaded_files:
                text = extract_text(uploaded_file)
                if text:
                    resumes_data.append({"filename": uploaded_file.name, "text": text})
            
            if not resumes_data:
                st.error("Could not extract text from uploaded files.")
            else:
                # 2. Score Resumes
                if demo_mode:
                    results = mock_score_resumes(resumes_data, job_description)
                else:
                    results = score_resumes(resumes_data, job_description, api_key)
                
                # 3. Display Results
                st.success("Analysis Complete!")
                
                # Create DataFrame for display
                df = pd.DataFrame(results)
                
                # Reorder columns for better readability
                cols = ["filename", "score", "recommendation", "experience_years", "matching_skills", "missing_skills", "summary"]
                # Handle case where some keys might be missing if error occurred
                available_cols = [c for c in cols if c in df.columns]
                df_display = df[available_cols]
                
                st.subheader("🏆 Candidate Rankings")
                st.dataframe(
                    df_display.style.background_gradient(subset=['score'], cmap='Greens'),
                    use_container_width=True
                )
                
                # Detailed View
                st.subheader("📝 Detailed Analysis")
                for index, row in df.iterrows():
                    with st.expander(f"#{index+1}: {row['filename']} - Score: {row.get('score', 'N/A')}"):
                        st.write(f"**Recommendation:** {row.get('recommendation', 'N/A')}")
                        st.write(f"**Experience:** {row.get('experience_years', 'N/A')}")
                        st.write(f"**Summary:** {row.get('summary', 'N/A')}")
                        
                        c1, c2 = st.columns(2)
                        with c1:
                            st.write("**✅ Matching Skills:**")
                            st.write(", ".join(row.get('matching_skills', [])) if isinstance(row.get('matching_skills'), list) else row.get('matching_skills'))
                        with c2:
                            st.write("**❌ Missing Skills:**")
                            st.write(", ".join(row.get('missing_skills', [])) if isinstance(row.get('missing_skills'), list) else row.get('missing_skills'))
