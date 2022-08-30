from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings ---
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL Settings ---
PAGE_TITLE = "Digital CV | Jonathan Aaron"
PAGE_ICON = ":wave:"
NAME = "Jonathan Aaron"
DESCRIPTION = """
Third year Computer science student ,highly motivated passion for technology and innovation.
"""
EMAIL ="jonathanmicrosoftacc@gmail.com"
SOCIAL_MEDIA ={
    "LinkedIn" : "https://www.linkedin.com/in/jonathana5/",
    "GitHub" : "https://github.com/JonathanAaronDev"
}

PROJETCTS = {
    ":trophy: My final C project in introduction to programming course" : "https://github.com/JonathanAaronDev/Project-in-C-for-studies",
    ":trophy: Educational math software for Sixth grade(C-sharp)" : "https://github.com/JonathanAaronDev/Final-Project-C-sharp",
    ":trophy: Lottery game (using HTML,CSS and JS)" : "https://github.com/JonathanAaronDev/Web-Development",
    ":trophy: Conway's Game of Life (Python)" : "https://github.com/JonathanAaronDev/Game_Of_Life-python-",
    ":trophy: Sales Dashboard - Comparing sales across countries" : "https://github.com/JonathanAaronDev/Dashboard_data",
    ":trophy: NBA Dashboard(21/22) - Comparing stats between diffrent NBA teams " : "https://github.com/JonathanAaronDev/NBA_Dashboard_21-22",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

# --- HEAD ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic ,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":e-mail:", EMAIL)
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platfrom, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platfrom}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Specializing student in data science
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)
# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C#, C, JAVA, HTML, CSS, JS, SQL
- 📊 Data Visualization: Plotly, Matplotlib, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decision trees, naive bayes  and much more
- 🗄️ Databases: MySQL
"""
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJETCTS.items():
    st.write(f"[{project}]({link})")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://scx2.b-cdn.net/gfx/news/hires/2019/galaxy.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)