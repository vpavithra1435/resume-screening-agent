from fpdf import FPDF
import os

def create_pdf(filename, title, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    
    # Content
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=content)
    
    output_path = os.path.join("job_description", filename)
    pdf.output(output_path)
    print(f"Created {output_path}")

# Job Descriptions Data
jds = [
    {
        "filename": "JD_Frontend_Developer.pdf",
        "title": "Job Description: Frontend Developer",
        "content": """
Role: Frontend Developer
Location: Remote / Hybrid
Type: Full-time

About the Role:
We are looking for a skilled Frontend Developer to join our team. You will be responsible for building user-facing features for our web applications, ensuring high performance and responsiveness.

Responsibilities:
- Develop new user-facing features using React.js.
- Build reusable code and libraries for future use.
- Ensure the technical feasibility of UI/UX designs.
- Optimize application for maximum speed and scalability.
- Collaborate with other team members and stakeholders.

Requirements:
- Proven work experience as a Frontend Developer.
- Strong proficiency in JavaScript, including DOM manipulation and the JavaScript object model.
- Thorough understanding of React.js and its core principles.
- Experience with popular React.js workflows (such as Flux or Redux).
- Familiarity with newer specifications of EcmaScript.
- Knowledge of modern authorization mechanisms, such as JSON Web Token.
- Familiarity with modern front-end build pipelines and tools.
        """
    },
    {
        "filename": "JD_DevOps_Engineer.pdf",
        "title": "Job Description: DevOps Engineer",
        "content": """
Role: DevOps Engineer
Location: Remote
Type: Full-time

About the Role:
We are seeking a DevOps Engineer to help us build functional systems that improve customer experience. You will deploy product updates, identify production issues, and implement integrations that meet customer needs.

Responsibilities:
- Deploy updates and fixes.
- Provide Level 2 technical support.
- Build tools to reduce occurrences of errors and improve customer experience.
- Develop software to integrate with internal back-end systems.
- Perform root cause analysis for production errors.
- Investigate and resolve technical issues.
- Develop scripts to automate visualization.
- Design procedures for system troubleshooting and maintenance.

Requirements:
- Work experience as a DevOps Engineer or similar software engineering role.
- Good knowledge of Ruby or Python.
- Working knowledge of databases and SQL.
- Problem-solving attitude.
- Collaborative team spirit.
- Experience with AWS, Docker, and Kubernetes.
- Experience with CI/CD pipelines (Jenkins, GitLab CI, etc.).
        """
    },
    {
        "filename": "JD_Product_Manager.pdf",
        "title": "Job Description: Product Manager",
        "content": """
Role: Product Manager
Location: On-site
Type: Full-time

About the Role:
We are looking for an experienced Product Manager who is passionate about building products that customers love. You will join a dynamic and fast-paced environment and work with cross-functional teams to design, build, and roll out products that deliver the company's vision and strategy.

Responsibilities:
- Gain a deep understanding of customer experience, identify and fill product gaps and generate new ideas that grow market share, improve customer experience and drive growth.
- Create buy-in for the product vision both internally and with key external partners.
- Translate product strategy into detailed requirements and prototypes.
- Scope and prioritize activities based on business and customer impact.
- Work closely with engineering teams to deliver with quick time-to-market and optimal resources.
- Drive product launches including working with public relations team, executives, and other product management team members.
- Act as a product evangelist to build awareness and understanding.

Requirements:
- Proven work experience in product management.
- Proven track record of managing all aspects of a successful product throughout its lifecycle.
- Proven ability to develop product and marketing strategies and effectively communicate recommendations to executive management.
- Solid technical background with understanding and/or hands-on experience in software development and web technologies.
- Strong problem-solving skills and willingness to roll up one's sleeves to get the job done.
- Skilled at working effectively with cross functional teams in a matrix organization.
- Excellent written and verbal communication skills.
        """
    }
]

if __name__ == "__main__":
    # Ensure directory exists
    if not os.path.exists("job_description"):
        os.makedirs("job_description")
        
    for jd in jds:
        create_pdf(jd["filename"], jd["title"], jd["content"])
