import streamlit as st
from PIL import Image
from collections import OrderedDict
import base64

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="favicon.png",
    layout="centered"
)

# ------------------ BACKGROUND IMAGE ------------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("a_digital_photograph_showcases_a_living_room_bathe.png")

# ------------------ MODERN GLASS UI ------------------
st.markdown("""
<style>

/* Glass container */
.main {
    background: rgba(11, 18, 8, 0.65);
    backdrop-filter: blur(14px);
    padding: 2rem;
    border-radius: 20px;
}

/* Text */
h1, h2, h3, h4, p, label {
    color: #E5E5E5 !important;
}

/* Inputs */
.stSelectbox div, .stTextArea textarea {
    background: rgba(22, 34, 15, 0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #1E3A8A, #0B1208);
    color: white;
    border-radius: 14px;
    padding: 0.6rem 1.2rem;
    border: none;
    box-shadow: 0 0 15px rgba(30,58,138,0.4);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(30,58,138,0.7);
}

/* Divider */
hr {
    border: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# ------------------ LOGO ------------------
try:
    logo = Image.open("Logo.png")
    st.image(logo, width=200)
except:
    st.write("Logo not found")

# ------------------ TITLE ------------------
st.title("🎨 Find Your Hobby")
st.write("Answer a few questions and discover hobbies tailored to you.")
st.divider()

# ------------------ PERSONAL QUESTIONS ------------------
st.subheader("🧍 Personal Info")
age = st.number_input("Age", 5, 100, 25)
fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])
stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])
work = st.selectbox("Weekly Work Hours", ["<20", "20-40", "40+"])
sleep = st.selectbox("Sleep Hours", ["<5", "5-7", "7+"])

# ------------------ HOBBY QUESTIONS ------------------
questions = {
    "creative": "Creative?",
    "outdoor": "Like outdoors?",
    "social": "Social?",
    "time": "Free time?",
    "physical": "Like physical activity?",
    "budget": "Budget?",
    "learning": "Like learning?",
    "technology": "Tech interest?",
    "music": "Like music?",
    "patience": "Patient?",
    "competition": "Competitive?",
    "travel": "Like travel?",
    "nature": "Like nature?",
    "indoor": "Prefer indoors?",
    "helping": "Like helping others?"
}

options_dict = {
    "YesNo": ["Yes", "No"],
    "Time": ["<2 hours", "2–5 hours", "5+ hours"],
    "Budget": ["Low", "Medium", "High"]
}

answers = {}
for key, q in questions.items():
    if key == "time":
        answers[key] = st.selectbox(q, options_dict["Time"])
    elif key == "budget":
        answers[key] = st.selectbox(q, options_dict["Budget"])
    else:
        answers[key] = st.selectbox(q, options_dict["YesNo"])

# ------------------ TEXT AREA ------------------
user_input = st.text_area("Extra preferences...", height=120)

st.divider()

# ------------------ LOGIC ------------------
def suggest_hobbies(answers, user_text="", age=25, fitness="Medium"):
    hobbies = []

    if answers["creative"] == "Yes":
        hobbies += ["🎨 Painting", "✏️ Sketching"]
    if answers["outdoor"] == "Yes":
        hobbies += ["🌿 Hiking", "🌱 Gardening"]
    if answers["social"] == "Yes":
        hobbies += ["⚽ Team Sports"]
    else:
        hobbies += ["📚 Reading"]

    if answers["physical"] == "Yes":
        if age <= 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

    if answers["technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if answers["music"] == "Yes":
        hobbies += ["🎧 Music Production"]

    if user_text:
        text = user_text.lower()
        if "cook" in text:
            hobbies.append("👩‍🍳 Cooking")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ OUTPUT ------------------
if st.button("✨ Suggest Hobbies"):
    hobbies = suggest_hobbies(answers, user_input, age, fitness)

    st.subheader("✨ Your Hobbies")

    cols = st.columns(3)
    for i, hobby in enumerate(hobbies):
        cols[i % 3].write(hobby)
