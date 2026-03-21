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
    border-radius: 12px;
    padding: 0.4rem;
    color: var(--text-color) !important;
}

.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    border-radius: 12px;
    border: 1px solid var(--accent-blue);
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
    st.warning("Logo not found.")

# ------------------ TITLE ------------------
st.title("🎨 Find Your Perfect Hobby")
st.write("Answer a few questions and discover hobbies tailored to you!")
st.divider()

# ------------------ PERSONAL INFO ------------------
st.subheader("🧍 Personal Info")

age = st.slider("Age", 5, 100, 25)
fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])
stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])

# ------------------ QUESTIONS ------------------
st.subheader("🧠 Preferences")

questions = {
    "creative": "Creative",
    "outdoor": "Outdoor",
    "social": "Social",
    "physical": "Physical",
    "learning": "Learning",
    "technology": "Technology",
    "music": "Music",
    "patience": "Patience",
    "competition": "Competition"
}

answers = {}
for key, label in questions.items():
    answers[key] = st.selectbox(label, ["No", "Yes"])

user_text = st.text_area("💬 Extra preferences")

# ------------------ RADAR CHART ------------------
def create_radar_chart(answers):
    labels = list(answers.keys())
    values = [1 if v == "Yes" else 0 for v in answers.values()]

    # close the loop
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color="#E5E5E5")

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["No", "Yes"], color="#E5E5E5")

    ax.set_facecolor("#16220F")
    fig.patch.set_facecolor("#0B1208")

    return fig

# ------------------ HOBBY ENGINE ------------------
def suggest_hobbies(answers, text, age, fitness):
    hobbies = []

    if answers["creative"] == "Yes":
        hobbies += ["🎨 Painting", "✏️ Sketching"]

    if answers["outdoor"] == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]

    if answers["social"] == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Acting"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if answers["physical"] == "Yes":
        if age < 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

    if answers["learning"] == "Yes":
        hobbies += ["🌍 Languages", "🧠 Courses"]

    if answers["technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if answers["music"] == "Yes":
        hobbies += ["🎸 Guitar", "🎤 Singing"]

    if answers["patience"] == "Yes":
        hobbies += ["♟️ Chess", "🧩 Puzzles"]

    if answers["competition"] == "Yes":
        hobbies += ["🏆 eSports"]

    # Text intelligence
    text = text.lower()
    if "cook" in text:
        hobbies.append("👩‍🍳 Cooking")
    if "art" in text:
        hobbies.append("🎨 Digital Art")
    if "game" in text:
        hobbies.append("🎮 Game Dev")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ BUTTON ------------------
if st.button("✨ Find My Hobby"):

    hobbies = suggest_hobbies(answers, user_text, age, fitness)

    st.subheader("📊 Your Personality Map")
    fig = create_radar_chart(answers)
    st.pyplot(fig)

    st.subheader("✨ Recommended Hobbies")

    if hobbies:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].write(hobby)
    else:
        st.write("No hobbies found — try adding more preferences!")
