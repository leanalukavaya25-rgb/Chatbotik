import streamlit as st
from PIL import Image
from collections import OrderedDict
import base64
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Hobby Finder",
    page_icon="favicon.png",
    layout="centered"
)

# ------------------ BACKGROUND ------------------
def set_bg(image):
    with open(image, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("a_digital_photograph_showcases_a_living_room_bathe.png")

# ------------------ MODERN UI ------------------
st.markdown("""
<style>

/* Glass effect */
.block-container {
    background: rgba(11,18,8,0.65);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2rem;
}

/* Text */
h1, h2, h3, h4, p, label {
    color: #E5E5E5 !important;
}

/* Inputs */
.stSelectbox div, textarea {
    background: rgba(22,34,15,0.7) !important;
    border-radius: 12px !important;
    color: white !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #1E3A8A, #0B1208);
    color: white;
    border-radius: 14px;
    box-shadow: 0 0 15px rgba(30,58,138,0.5);
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
}

/* Chat bubbles */
.chat-user {
    background: #1E3A8A;
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
    text-align: right;
}
.chat-bot {
    background: rgba(255,255,255,0.1);
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SESSION MEMORY ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ LOGO ------------------
try:
    st.image(Image.open("Logo.png"), width=180)
except:
    pass

# ------------------ TITLE ------------------
st.title("🤖 AI Hobby Finder")

# ------------------ INPUT SECTION ------------------
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
def suggest(age, fitness, creative, outdoor, physical, tech, music, text):
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

    if text:
        if "cook" in text.lower():
            hobbies.append("👩‍🍳 Cooking")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ BUTTON ------------------
if st.button("✨ Ask AI"):
    
    # Save user message
    st.session_state.chat.append(("user", "Suggest hobbies for me"))

    # Fake AI thinking
    with st.spinner("🤖 AI is thinking..."):
        time.sleep(1.5)

    hobbies = suggest(age, fitness, creative, outdoor, physical, tech, music, extra)

    response = "Here are hobbies I recommend:\n\n"
    for h in hobbies:
        response += f"{h}\n"

    st.session_state.chat.append(("bot", response))

# ------------------ CHAT DISPLAY ------------------
st.subheader("💬 Chat")

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">{msg}</div>', unsafe_allow_html=True)
