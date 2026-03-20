import streamlit as st
from PIL import Image
from collections import OrderedDict
import base64
import time
import random

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
.block-container {
    background: rgba(11,18,8,0.65);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2rem;
}
h1, h2, h3, h4, p, label {
    color: #E5E5E5 !important;
}
.stButton>button {
    background: linear-gradient(135deg, #1E3A8A, #0B1208);
    color: white;
    border-radius: 14px;
}
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

# ------------------ MEMORY ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ LOGO ------------------
try:
    st.image(Image.open("Logo.png"), width=180)
except:
    pass

# ------------------ TITLE ------------------
st.title("🤖 AI Hobby Finder")

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

# ------------------ SMART FAKE AI ------------------
def smart_ai():
    hobbies = []
    explanations = []

    if creative == "Yes":
        hobbies += ["🎨 Painting", "✏️ Drawing", "🧵 Crafts"]
        explanations.append("You seem creative, so artistic hobbies fit you well.")

    if outdoor == "Yes":
        hobbies += ["🌿 Hiking", "🌱 Gardening"]
        explanations.append("You enjoy nature, so outdoor hobbies are great.")

    if physical == "Yes":
        if age <= 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
            explanations.append("You can handle active hobbies.")
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]
            explanations.append("Lighter activities suit your lifestyle better.")

    if tech == "Yes":
        hobbies += ["💻 Coding", "🎮 Game Development"]
        explanations.append("You like tech, so digital hobbies are perfect.")

    if music == "Yes":
        hobbies += ["🎧 Music Production", "🎸 Guitar"]
        explanations.append("Music-based hobbies match your interests.")

    # Extra input intelligence
    if extra:
        text = extra.lower()
        if "cook" in text:
            hobbies.append("👩‍🍳 Cooking")
        if "art" in text:
            hobbies.append("🎨 Digital Art")

    hobbies = list(OrderedDict.fromkeys(hobbies))

    # Build AI-style response
    intro = random.choice([
        "Based on your answers, here are some great hobbies for you:",
        "I analyzed your preferences — here are my suggestions:",
        "Here are hobbies that match your personality:"
    ])

    response = intro + "\n\n"

    for h in hobbies:
        response += f"{h}\n"

    if explanations:
        response += "\n💡 Why these fit you:\n"
        for e in explanations:
            response += f"- {e}\n"

    return response

# ------------------ BUTTON ------------------
if st.button("✨ Ask AI"):
    st.session_state.chat.append(("user", "Suggest hobbies for me"))

    with st.spinner("🤖 AI is thinking..."):
        time.sleep(1.5)
        reply = smart_ai()

    st.session_state.chat.append(("bot", reply))

# ------------------ CHAT ------------------
st.subheader("💬 Chat")

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">{msg}</div>', unsafe_allow_html=True)
