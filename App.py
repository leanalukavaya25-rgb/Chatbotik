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
body, .stApp {
    background-color: var(--main-bg);
}
.block-container {
    background: rgba(11,18,8,0.9);
    padding: 2rem;
    border-radius: 18px;
}
h1, h2, h3, h4, p, label {
    color: var(--text-color) !important;
}
.stSelectbox div, textarea {
    background-color: var(--secondary-bg) !important;
    color: var(--text-color) !important;
    border-radius: 12px;
}
.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    border: 1px solid var(--accent-blue);
    border-radius: 12px;
}
.chat-user {
    background-color: var(--accent-blue);
    color: white;
    padding: 10px;
    border-radius: 12px;
    text-align: right;
    margin: 5px 0;
}
.chat-bot {
    background-color: var(--secondary-bg);
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
    pass

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

# ------------------ SCORING SYSTEM ------------------
def get_hobbies_with_scores():
    scores = {}

    def add_score(hobby, value):
        scores[hobby] = scores.get(hobby, 0) + value

    if creative == "Yes":
        add_score("🎨 Painting", 3)
        add_score("✏️ Drawing", 3)

    if outdoor == "Yes":
        add_score("🌿 Hiking", 3)
        add_score("🌱 Gardening", 2)

    if physical == "Yes":
        if age <= 45 and fitness != "Low":
            add_score("🏋️ Gym", 4)
            add_score("🚴 Cycling", 3)
        else:
            add_score("🚶 Walking", 4)
            add_score("🧘 Yoga", 3)

    if tech == "Yes":
        add_score("💻 Coding", 3)

    if music == "Yes":
        add_score("🎧 Music Production", 3)

    if extra:
        text = extra.lower()
        if "cook" in text:
            add_score("👩‍🍳 Cooking", 3)
        if "art" in text:
            add_score("🎨 Digital Art", 3)

    return scores

# ------------------ BUILD RESPONSE ------------------
def smart_ai():
    scores = get_hobbies_with_scores()

    # Sort hobbies by score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top3 = ranked[:3]
    all_hobbies = [h[0] for h in ranked]

    intro = random.choice([
        "Here are your best hobby matches:",
        "Based on your profile, these are perfect for you:",
        "Top hobbies for you:"
    ])

    response = intro + "\n\n"

    # Top 3 section
    if top3:
        response += "🏆 TOP 3 FOR YOU:\n"
        medals = ["🥇", "🥈", "🥉"]
        for i, (hobby, score) in enumerate(top3):
            response += f"{medals[i]} {hobby} (score: {score})\n"

    # Other hobbies
    if len(all_hobbies) > 3:
        response += "\n✨ Other suggestions:\n"
        for hobby in all_hobbies[3:]:
            response += f"{hobby}\n"

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
