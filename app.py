from pathlib  import Path

import streamlit as st

from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile.jpg"

PAGE_TITLE = "Digital CV | Chikondi Suniah"
PAGE_ICON = ":wave:"
NAME = "Chikondi Suniah"
DESCRIPTION = """ Strategic Information Technology technician skilled in guiding navigation of modern technology. Accustomed to driving efficiency and effectiveness by developing, delivering and supporting strategic plans. Demonstrated skill in translating technical requirements to business solutions. Successful in building positive relationships with internal and external stakeholders. """
EMAIL = "suniahchiko@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "",
    "LinkedIn": "",
    "GitHub": "",
    "Twitter": "",
}

PROJECTS = {
    "GELLION": "",
    "SALES": "",
    "TWITTER": "",
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

st.title("hello there") 

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1,col2, = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)    
    st.download_button(
        label=" Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write("",EMAIL)

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - 8 Years experiance extracting actionable insights from data
    - Strong hands on experience and knowledge in Python and excel
    - Good understanding of statidtical principles and their respective applcations
    - Excellent team-player and displaying strong sense of initiative on tasks
    """
)

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
     - Programming: Python (Scikit-learn,Pandas), SQL,VBA
     - Data Visulisation: PowerBi, MS Excel, Plotly
     - Modeling: Logistic regression,  linear regression, decition trees
     - Databases: Postgres, MongoDB, MySQL
    """
)

st.write("#")
st.subheader("Work History")
st.write("---")

st.write(" ", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write (
    """
    - Used PowerBI and SQL to redefine and track KPIS surrounding marketing initiatives, and 
    supplied recommendation to boost landing page conversion rate by 38%
    - Led a team of 4 analysts to brainstorm potential marketing and sales improvements,
    and implemented A/B tests to generate 15% more client leads 
    - Resigned data model through iterations that improved predications by 12%
    """
)


st.write(" ", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write (
    """
    - Used PowerBI and SQL to redefine and track KPIS surrounding marketing initiatives, and 
    supplied recommendation to boost landing page conversion rate by 38%
    - Led a team of 4 analysts to brainstorm potential marketing and sales improvements,
    and implemented A/B tests to generate 15% more client leads 
    - Resigned data model through iterations that improved predications by 12%
    """
)


st.write(" ", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write (
    """
    - Used PowerBI and SQL to redefine and track KPIS surrounding marketing initiatives, and 
    supplied recommendation to boost landing page conversion rate by 38%
    - Led a team of 4 analysts to brainstorm potential marketing and sales improvements,
    and implemented A/B tests to generate 15% more client leads 
    - Resigned data model through iterations that improved predications by 12%
    """
)

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("----")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

