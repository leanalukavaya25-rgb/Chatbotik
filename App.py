import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
from PIL import Image

# ------------------ PAGE CONFIG ------------------
try:
    icon = Image.open("favicon.png")
except:
    icon = "🎯"

st.set_page_config(
    page_title="Find Your Hobby",
    page_icon=icon,
    layout="centered"
)

# ------------------ THEME ------------------
st.markdown("""
<style>
:root {
    --main-bg: #0B1208;
    --secondary-bg: #16220F;
    --accent-green: #39FF14;
    --text-color: #E5E5E5;
}

body, .stApp {
    background-color: var(--main-bg);
    color: var(--text-color);
}

/* INPUTS */
div.stSlider, div.stTextArea, input, textarea {
    background-color: var(--secondary-bg) !important;
    border-radius: 12px;
    color: var(--text-color) !important;
}

/* FORCE GREEN EVERYWHERE */
* {
    accent-color: var(--accent-green) !important;
}

/* -------- SLIDER -------- */

/* Track */
.stSlider div[data-baseweb="slider"] > div {
    background-color: #2a2a2a !important;
}

/* Filled track */
.stSlider div[data-baseweb="slider"] > div > div,
.stSlider div[data-baseweb="slider"] > div > div > div {
    background-color: var(--accent-green) !important;
}

/* Handle */
.stSlider div[data-baseweb="slider"] [role="slider"] {
    background-color: var(--accent-green) !important;
    border: 2px solid var(--accent-green) !important;
}

/* Remove glow / hover effects */
.stSlider div[data-baseweb="slider"] [role="slider"]:hover,
.stSlider div[data-baseweb="slider"] [role="slider"]:active,
.stSlider div[data-baseweb="slider"] [role="slider"]:focus {
    box-shadow: none !important;
}

/* -------- REMOVE VALUE POPUP -------- */

/* This hides the floating number bubble */
.stSlider div[data-baseweb="slider"] [data-testid="stThumbValue"] {
    display: none !important;
}

/* Extra fallback (for different Streamlit versions) */
.stSlider div[role="tooltip"] {
    display: none !important;
}

/* Hide any span-based value labels */
.stSlider span {
    color: var(--accent-green) !important;
}

/* SVG elements */
.stSlider svg * {
    stroke: var(--accent-green) !important;
    fill: var(--accent-green) !important;
}

/* -------- BUTTON -------- */
.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    border: 1px solid var(--accent-green);
    border-radius: 12px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: var(--accent-green);
    color: black;
}

/* TEXT */
h1, h2, h3 {
    color: var(--text-color);
}
</style>
""", unsafe_allow_html=True)

# ------------------ LOGO ------------------
try:
    logo = Image.open("Logo.png")
    st.image(logo, width=220)
except:
    pass

# ------------------ TITLE ------------------
st.title("🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾")
st.write("Rate each statement from 1 (Hate) to 5 (Love)")
st.divider()

# ------------------ PERSONAL INFO ------------------
st.subheader("🧍 Personal Info")

age = st.number_input("🗓️ Age", 5, 100, 25)
fitness = st.selectbox("💪 Fitness Level", ["Low", "Medium", "High"])

# ------------------ QUESTIONS ------------------
st.subheader("🧠 Preferences (1 = Hate, 5 = Love)")

questions = {
    "creative": "🎨 Creative activities",
    "outdoor": "🌳 Being outdoors",
    "social": "👥 Social interaction",
    "physical": "💪 Physical activity",
    "learning": "📚 Learning new things",
    "technology": "💻 Technology",
    "music": "🎵 Music",
    "patience": "🧘 Patience activities",
    "competition": "🏆 Competition",
    "travel": "✈️ Travel & exploring",
    "nature": "🌿 Nature",
    "indoor": "🏠 Indoor activities",
    "helping": "🤝 Helping others"
}

answers = {}

for key, label in questions.items():
    answers[key] = st.slider(label, 1, 5, 3)

# ------------------ TEXT INPUT ------------------
user_input = st.text_area(" Tell me anything else you like:")
st.divider()

# ------------------ RADAR CHART ------------------
def create_radar_chart(ans):
    labels = list(ans.keys())
    values = list(ans.values())

    values = [v / 5 for v in values]

    values.append(values[0])
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles.append(angles[0])

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    fig.patch.set_facecolor("#0B1208")
    ax.set_facecolor("#16220F")

    ax.plot(angles, values, color="#39FF14", linewidth=2)
    ax.fill(angles, values, color="#39FF14", alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color="white", fontsize=8)

    ax.set_yticks([0.2, 0.5, 0.8, 1])
    ax.set_yticklabels(["1", "2-3", "4", "5"], color="white")

    return fig

# ------------------ HOBBY LOGIC ------------------
def suggest_hobbies(ans, text, age, fitness):
    hobbies = []

    if ans["creative"] >= 4:
        hobbies += ["🎨 Painting", "✏️ Sketching", "🧵 Crafts"]

    if ans["outdoor"] >= 4:
        hobbies += ["🥾 Hiking", "🌱 Gardening"]

    if ans["social"] >= 4:
        hobbies += ["⚽ Team Sports", "🎭 Drama"]
    elif ans["social"] <= 2:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if ans["physical"] >= 4:
        if age <= 45 and fitness != "Low":
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

    if ans["learning"] >= 4:
        hobbies += ["🌍 Learning Languages", "🧠 Online Courses"]

    if ans["technology"] >= 4:
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if ans["music"] >= 4:
        hobbies += ["🎤 Singing", "🎧 Music Production"]

    if ans["patience"] >= 4:
        hobbies += ["♟️ Chess", "🧩 Puzzles"]

    if ans["competition"] >= 4:
        hobbies += ["🏆 eSports"]

    if ans["travel"] >= 4:
        hobbies += ["🗺️ Exploring"]

    if ans["nature"] >= 4:
        hobbies += ["🌿 Nature Walks"]

    if ans["indoor"] >= 4:
        hobbies += ["🎮 Gaming"]

    if ans["helping"] >= 4:
        hobbies += ["🤝 Volunteering"]

    text = text.lower()
    if "art" in text:
        hobbies.append("🎨 Digital Art")
    if "game" in text:
        hobbies.append("🎮 Game Development")
    if "cook" in text:
        hobbies.append("👩‍🍳 Cooking")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ BUTTON ------------------
if st.button("✨ Suggest Hobbies"):

    st.subheader("📊 Your Personality Map")
    st.pyplot(create_radar_chart(answers))

    hobbies = suggest_hobbies(answers, user_input, age, fitness)

    st.subheader("✨ Recommended Hobbies")

    if hobbies:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].write(hobby)
    else:
        st.write("Try increasing some ratings!")
