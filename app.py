import streamlit as st

# Set page configuration for a clean, professional layout
st.set_page_config(page_title="Jaideep Balde's Interactive Resume", page_icon=":briefcase:", layout="wide")

# Title of the Resume Page
st.title("Jaideep Balde's Interactive Resume")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("[Objective](#objective)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Technical Skills](#technical-skills)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Certifications](#certifications)")
st.sidebar.markdown("[Contact](#contact)")
st.sidebar.markdown("[Download Resume](#download-resume)")

# Profile Section with the correct image URL
st.image("https://huggingface.co/spaces/JaideepB/jaideep-profile/raw/main/Profile.jpg.jpg", width=200)  # Displaying profile image
st.write("**Jaideep Balde**")
st.write("Phone: +91-8788437458 | Email: [jaydeepbalade15@gmail.com](mailto:jaydeepbalade15@gmail.com)")
st.write("LinkedIn: [linkedin.com/in/jaideep-balde](https://linkedin.com/in/jaideep-balde)")

# The rest of the sections remain the same...

# Objective Section
st.header("Objective")
st.write("""
    To leverage my skills in machine learning, software development, and data analytics in a challenging
    environment that offers growth and development opportunities. Passionate about research, stock analysis,
    and creating impactful applications.
""")

# Education Section
st.header("Education")
st.write("**Sardar Patel Institute of Technology, Mumbai** (2021 – 2025)")
st.write("B.Tech in Electronics and Telecommunication Engineering")
st.write("**Narayana E-Techno Junior College, Thane** (2019 – 2021)")
st.write("12th Standard - HSC")
st.write("**Army Public School, Pune** (2019)")
st.write("10th Standard - CBSE")

# Relevant Coursework Section
st.header("Relevant Coursework")
st.write("""
    - Hugging Face
    - FlutterFlow
    - Machine Learning
    - Database Management
    - Artificial Intelligence
    - Data Analysis
    - Selenium
    - Streamlit
""")

# Technical Skills Section
st.header("Technical Skills")
st.write("**Programming**: Python, C++, Java, JavaScript, HTML/CSS")
st.write("**Tools**: VS Code, Git, Jupyter Notebook, Google Colab, Tableau, MongoDB")
st.write("**Technologies**: Streamlit, Hugging Face, Machine Learning, Data Visualization")
st.write("**Specialized Skills**: Budget Tracking, Trading Simulators, Stock Analysis Apps")

# Projects Section
st.header("Projects")
st.write("**1. Brain Tumor Detection (AIML) (2023 – 2024)**")
st.write("   - Developed a U-Net model for MRI-based tumor segmentation, enhancing diagnostic efficiency.")
st.write("   - Achieved high accuracy through iterative model optimization.")
st.write("**2. Options Trading Simulator (2023 – 2024)**")
st.write("   - Built a simulator for evaluating trading strategies with dynamic dashboards.")
st.write("   - Enabled users to assess financial risks effectively.")
st.write("**3. Stock Analysis App (2023 – 2024)**")
st.write("   - Designed a web app for real-time stock analysis with interactive visualizations.")
st.write("   - Integrated APIs for live market data and insights.")
st.write("**4. Personal Finance Tracker (2022 – 2023)**")
st.write("   - Created a tracker with budgeting and financial goal management features.")
st.write("   - Enhanced user experience with interactive data visualization.")

# Extracurricular Activities Section
st.header("Extracurricular Activities")
st.write("**Cybersecurity Enthusiast**: Ranked top 5 in Barclays Cybershala hackathon.")
st.write("**Tech Blogger**: Writes beginner-friendly tutorials on Medium.")
st.write("**Open Source Contributor**: Worked on visualization and backend projects.")

# Certifications Section
st.header("Certifications")
st.write("**Barclays Cybershala: Fundamentals of Cybersecurity and Ethical Hacking (2024)**")

# Additional Information Section
st.header("Additional Information")
st.write("**Languages**: Fluent in English, Hindi, and Marathi")
st.write("**Interests**: Data-driven research, financial markets, and AI for healthcare")
st.write("**Volunteering**: Organized technical workshops for underprivileged students, fostering STEM education.")

# Contact Section
st.header("Contact")
st.write("Feel free to reach out for any collaboration, technical discussions, or job inquiries.")
st.write("I'm always open to learning new things and sharing ideas.")

# Contact Form Section
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        st.success("Thank you for reaching out! I will get back to you shortly.")

# Download Resume Button
st.header("Download Resume")
st.download_button(
    label="Download My Resume",
    data="https://huggingface.co/spaces/JaideepB/jaideep-profile/resolve/main/Latest_Jaideep_2.pdf",
    file_name="Latest_Jaideep_2.pdf",
    mime="application/pdf"
)

# Footer Section
st.markdown("""
    <footer style="text-align:center; padding:10px; font-size:12px; color:#777;">
        <p>&copy; 2025 Jaideep Balde | All Rights Reserved</p>
    </footer>
""", unsafe_allow_html=True)
