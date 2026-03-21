import streamlit as st
from PIL import Image
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="🎯",
    layout="centered"
)

# ------------------ THEME ------------------
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
    color: var(--text-color);
}

div.stSelectbox, div.stTextArea, input, textarea {
    background-color: var(--secondary-bg) !important;
    border-radius: 10px;
    color: var(--text-color) !important;
}

.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    border: 1px solid var(--accent-blue);
    border-radius: 10px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: var(--secondary-bg);
}

h1, h2, h3 {
    color: var(--text-color);
}
</style>
""", unsafe_allow_html=True)

# ------------------ LOGO ------------------
try:
    logo = Image.open("Logo.png")
    st.image(logo, width=200)
except:
    st.write("")

# ------------------ TITLE ------------------
st.title("🎨 Find Your Perfect Hobby")
st.write("Answer a few questions and discover hobbies tailored to you!")
st.divider()

# ------------------ PERSONAL INFO ------------------
st.subheader("🧍 Personal Info")

age = st.slider("Age", 5, 100, 25)
fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])

# ------------------ QUESTIONS ------------------
st.subheader("🧠 Preferences")

questions = {
    "Creative": "Do you enjoy creative activities?",
    "Outdoor": "Do you like being outdoors?",
    "Social": "Do you enjoy social activities?",
    "Physical": "Do you like physical activity?",
    "Learning": "Do you enjoy learning new things?",
    "Technology": "Are you interested in technology?",
    "Music": "Do you enjoy music?",
    "Patience": "Are you patient?",
    "Competition": "Do you like competition?"
}

answers = {}

for key, question in questions.items():
    answers[key] = st.selectbox(question, ["No", "Yes"])

user_text = st.text_area("💬 Extra preferences (optional)")

# ------------------ RADAR CHART ------------------
def create_radar_chart(answers):
    labels = list(answers.keys())
    values = [1 if v == "Yes" else 0 for v in answers.values()]

    # close the loop
    values.append(values[0])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles.append(angles[0])

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["No", "Yes"])

    # DARK THEME FIX
    fig.patch.set_facecolor("#0B1208")
    ax.set_facecolor("#16220F")
    ax.tick_params(colors="white")

    return fig

# ------------------ HOBBY LOGIC ------------------
def suggest_hobbies(answers, text, age, fitness):
    hobbies = []

    if answers["Creative"] == "Yes":
        hobbies += ["🎨 Painting", "✏️ Sketching"]

    if answers["Outdoor"] == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]

    if answers["Social"] == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Acting"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if answers["Physical"] == "Yes":
        if age < 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

    if answers["Learning"] == "Yes":
        hobbies += ["🌍 Learning Languages", "🧠 Online Courses"]

    if answers["Technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if answers["Music"] == "Yes":
        hobbies += ["🎸 Guitar", "🎤 Singing"]

    if answers["Patience"] == "Yes":
        hobbies += ["♟️ Chess", "🧩 Puzzles"]

    if answers["Competition"] == "Yes":
        hobbies += ["🏆 eSports"]

    # TEXT MATCHING
    text = text.lower()

    if "cook" in text:
        hobbies.append("👩‍🍳 Cooking")
    if "art" in text:
        hobbies.append("🎨 Digital Art")
    if "game" in text:
        hobbies.append("🎮 Game Development")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ BUTTON ------------------
if st.button("✨ Find My Hobby"):

    st.subheader("📊 Your Personality Map")
    fig = create_radar_chart(answers)
    st.pyplot(fig)

    hobbies = suggest_hobbies(answers, user_text, age, fitness)

    st.subheader("✨ Recommended Hobbies")

    if hobbies:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].write(hobby)
    else:
        st.write("Try selecting more preferences!")
