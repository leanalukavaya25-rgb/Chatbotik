import streamlit as st
from PIL import Image
from collections import OrderedDict
import time
import random

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="favicon.png",
    layout="centered"
)

# ------------------ COLORS ------------------
st.markdown("""
<style>
:root {
    --main-bg: #0B1208;
    --secondary-bg: #16220F;
    --accent-blue: #1E3A8A;
    --text-color: #E5E5E5;
}

/* App background */
body, .stApp {
    background-color: var(--main-bg);
}

/* Container */
.block-container {
    background: rgba(11,18,8,0.9);
    padding: 2rem;
    border-radius: 18px;
}

/* Text */
h1, h2, h3, h4, p, label {
    color: var(--text-color) !important;
}

/* Inputs */
.stSelectbox div, textarea {
    background-color: var(--secondary-bg) !important;
    color: var(--text-color) !important;
    border-radius: 12px;
}

/* Button */
.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    border: 1px solid var(--accent-blue);
    border-radius: 12px;
    transition: 0.2s;
}
.stButton>button:hover {
    background-color: var(--secondary-bg);
}

/* Chat bubbles */
.chat-user {
    background-color: var(--accent-blue);
    color: white;
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
    text-align: right;
}
.chat-bot {
    background-color: var(--secondary-bg);
    color: var(--text-color);
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ LOGO ------------------
try:
    st.image(Image.open("Logo.png"), width=180)
except:
    st.write("")

# ------------------ TITLE ------------------
st.title("🎨 Find Your Hobby")

# ------------------ INPUT ------------------
st.subheader("🧍 Tell me about yourself")

age = st.number_input("Age", 5, 100, 25)
fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])
creative = st.selectbox("Creative?", ["Yes", "No"])
outdoor = st.selectbox("Outdoor?", ["Yes", "No"])
physical = st.selectbox("Physical activity?", ["Yes", "No"])
tech = st.selectbox("Tech interest?", ["Yes", "No"])
music = st.selectbox("Music?", ["Yes", "No"])
extra = st.text_area("Anything else?")

# ------------------ AI LOGIC ------------------
def smart_ai():
    hobbies = []

    if creative == "Yes":
        hobbies += ["🎨 Painting", "✏️ Drawing"]
    if outdoor == "Yes":
        hobbies += ["🌿 Hiking", "🌱 Gardening"]
    if physical == "Yes":
        if age <= 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]
    if tech == "Yes":
        hobbies += ["💻 Coding"]
    if music == "Yes":
        hobbies += ["🎧 Music Production"]

    if extra:
        text = extra.lower()
        if "cook" in text:
            hobbies.append("👩‍🍳 Cooking")
        if "art" in text:
            hobbies.append("🎨 Digital Art")

    hobbies = list(OrderedDict.fromkeys(hobbies))

    intro = random.choice([
        "Based on your answers, here are great hobbies:",
        "Here are hobbies that match you:",
        "I recommend these hobbies for you:"
    ])

    response = intro + "\n\n"
    for h in hobbies:
        response += f"{h}\n"

    return response

# ------------------ TYPING EFFECT ------------------
def type_text(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(
            f'<div class="chat-bot">{typed}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.008)

# ------------------ BUTTON ------------------
if st.button("✨ Ask AI"):
    st.session_state.chat.append(("user", "Suggest hobbies for me"))

    with st.spinner("🤖 AI is thinking..."):
        time.sleep(1)
        reply = smart_ai()

    st.session_state.chat.append(("bot", reply))

# ------------------ CHAT ------------------
st.subheader("💬 Chat")

for i, (role, msg) in enumerate(st.session_state.chat):
    if role == "user":
        st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
    else:
        if i == len(st.session_state.chat) - 1:
            type_text(msg)
        else:
            st.markdown(f'<div class="chat-bot">{msg}</div>', unsafe_allow_html=True)
