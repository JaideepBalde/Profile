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

# Interactive Quiz Section
st.header("Interactive Quiz")

# Question 1
st.subheader("1. What does AIML stand for?")
options_q1 = ["Artificial Intelligence and Machine Learning", "Artificial Intelligence and Mixed Learning", "Advanced Interactive Machine Learning"]
answer_q1 = "Artificial Intelligence and Machine Learning"
user_answer_q1 = st.radio("Choose the correct option:", options_q1)

# Button to check the answer for Question 1
if st.button("Submit Answer for Question 1"):
    if user_answer_q1 == answer_q1:
        st.success("Correct! AIML stands for Artificial Intelligence and Machine Learning.")
    else:
        st.error("Incorrect! Please try again.")

# Question 2
st.subheader("2. Which language is primarily used for web development?")
options_q2 = ["Python", "JavaScript", "C++"]
answer_q2 = "JavaScript"
user_answer_q2 = st.radio("Choose the correct option:", options_q2, key="q2")

# Button to check the answer for Question 2
if st.button("Submit Answer for Question 2"):
    if user_answer_q2 == answer_q2:
        st.success("Correct! JavaScript is primarily used for web development.")
    else:
        st.error("Incorrect! Please try again.")

# Question 3
st.subheader("3. What does the acronym 'API' stand for?")
options_q3 = ["Application Programming Interface", "Artificial Programming Interface", "Application Process Integration"]
answer_q3 = "Application Programming Interface"
user_answer_q3 = st.radio("Choose the correct option:", options_q3, key="q3")

# Button to check the answer for Question 3
if st.button("Submit Answer for Question 3"):
    if user_answer_q3 == answer_q3:
        st.success("Correct! API stands for Application Programming Interface.")
    else:
        st.error("Incorrect! Please try again.")

# Question 4
st.subheader("4. Which of the following is a popular Python library for data manipulation?")
options_q4 = ["NumPy", "TensorFlow", "React"]
answer_q4 = "NumPy"
user_answer_q4 = st.radio("Choose the correct option:", options_q4, key="q4")

# Button to check the answer for Question 4
if st.button("Submit Answer for Question 4"):
    if user_answer_q4 == answer_q4:
        st.success("Correct! NumPy is a popular library for data manipulation in Python.")
    else:
        st.error("Incorrect! Please try again.")

# Question 5
st.subheader("5. What does the acronym 'ML' stand for?")
options_q5 = ["Machine Learning", "Mixed Learning", "Model Learning"]
answer_q5 = "Machine Learning"
user_answer_q5 = st.radio("Choose the correct option:", options_q5, key="q5")

# Button to check the answer for Question 5
if st.button("Submit Answer for Question 5"):
    if user_answer_q5 == answer_q5:
        st.success("Correct! ML stands for Machine Learning.")
    else:
        st.error("Incorrect! Please try again.")

# Question 6
st.subheader("6. What is the primary use of Streamlit?")
options_q6 = ["Data Science Applications", "Game Development", "Web Design"]
answer_q6 = "Data Science Applications"
user_answer_q6 = st.radio("Choose the correct option:", options_q6, key="q6")

# Button to check the answer for Question 6
if st.button("Submit Answer for Question 6"):
    if user_answer_q6 == answer_q6:
        st.success("Correct! Streamlit is primarily used for building Data Science applications.")
    else:
        st.error("Incorrect! Please try again.")

# Question 7
st.subheader("7. Which framework is used for Android app development?")
options_q7 = ["Flutter", "React Native", "Android Studio"]
answer_q7 = "Android Studio"
user_answer_q7 = st.radio("Choose the correct option:", options_q7, key="q7")

# Button to check the answer for Question 7
if st.button("Submit Answer for Question 7"):
    if user_answer_q7 == answer_q7:
        st.success("Correct! Android Studio is used for Android app development.")
    else:
        st.error("Incorrect! Please try again.")

# Question 8
st.subheader("8. What does 'SQL' stand for?")
options_q8 = ["Structured Query Language", "Simple Query Language", "Standardized Query Language"]
answer_q8 = "Structured Query Language"
user_answer_q8 = st.radio("Choose the correct option:", options_q8, key="q8")

# Button to check the answer for Question 8
if st.button("Submit Answer for Question 8"):
    if user_answer_q8 == answer_q8:
        st.success("Correct! SQL stands for Structured Query Language.")
    else:
        st.error("Incorrect! Please try again.")

# Question 9
st.subheader("9. What is a major application of Machine Learning in healthcare?")
options_q9 = ["Predicting Disease Outcomes", "Managing Financial Portfolios", "Web Development"]
answer_q9 = "Predicting Disease Outcomes"
user_answer_q9 = st.radio("Choose the correct option:", options_q9, key="q9")

# Button to check the answer for Question 9
if st.button("Submit Answer for Question 9"):
    if user_answer_q9 == answer_q9:
        st.success("Correct! Machine Learning is used for predicting disease outcomes.")
    else:
        st.error("Incorrect! Please try again.")

# Question 10
st.subheader("10. Which platform is widely used for deploying Machine Learning models?")
options_q10 = ["Google Cloud", "AWS", "All of the above"]
answer_q10 = "All of the above"
user_answer_q10 = st.radio("Choose the correct option:", options_q10, key="q10")

# Button to check the answer for Question 10
if st.button("Submit Answer for Question 10"):
    if user_answer_q10 == answer_q10:
        st.success("Correct! All of the above platforms are used for deploying Machine Learning models.")
    else:
        st.error("Incorrect! Please try again.")
