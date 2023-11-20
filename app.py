import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/sundar_1.jpg")
img_lottie_animation = Image.open("images/yt_lottie_animation.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sundar :wave:")
    st.title("CTO of Localhelper")
    st.write(
        "I bring a wealth of experience in steering organizations towards sustainable growth through the strategic integration of cutting-edge technologies."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/sundararaja25/)")

    # ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As an accomplished Chief Technology Officer, I bring a wealth of experience in steering organizations 
            towards sustainable growth through the strategic integration of cutting-edge technologies. 
            Renowned for my proficiency in artificial intelligence (AI) and 
            mastery of advanced technologies such as LLM (Large Language Models), IoT, and cloud computing.
            I have consistently led teams to deliver innovative solutions that drive operational efficiency and elevate decision-making processes.
            My strategic planning expertise is evident in the successful alignment of technology initiatives with 
            overarching business objectives, resulting in the development and execution of comprehensive technology roadmaps.
            I have a proven track record of building high-performing teams and fostering
            a culture of innovation, collaborating effectively 
            with cross-functional teams to ensure the timely delivery of transformative solutions.
            Notable achievements include orchestrating the development of an AI-driven predictive analytics platform,
            leading the adoption of LLM for CRM, and successfully navigating a major cloud migration initiative.
            Committed to anticipating and proactively addressing future challenges,
            I possess an entrepreneurial mindset and a keen ability to translate
            complex technical concepts into tangible business value.
            I am poised to lead our organization to unprecedented success,
            capturing the interest of forward-thinking investors ready to embark on a transformative journey.
            """
        )
       # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate ChatApp Inside Your Streamlit App")
        st.write(
            """
            Learn how to use ChatApp in Streamlit!
            """
        )
       # st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sundar@localher.in" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()