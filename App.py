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
    border: 1px solid var(--accent-blue);
    border-radius: 12px;
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
    st.image(logo, width=220)
except:
    st.write("")

# ------------------ TITLE ------------------
st.title("🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾")
st.write("Answer these questions and I'll suggest hobbies just for you!")
st.divider()

# ------------------ PERSONAL INFO ------------------
st.subheader("🧍 Personal Info")

age = st.number_input("🗓️ Age", min_value=5, max_value=100, value=25)
fitness = st.selectbox("💪 Fitness Level", ["Low", "Medium", "High"])
stress_level = st.selectbox("😌 Stress Level", ["Low", "Medium", "High"])
work_hours = st.selectbox("⌛ Weekly Work Hours", ["<20", "20-40", "40+"])
sleep_hours = st.selectbox("🛌 Average Sleep Hours", ["<5", "5-7", "7+"])

# ------------------ QUESTIONS ------------------
st.subheader("🧠 Preferences")

questions = {
    "creative": "🎨 Do you prefer creative hobbies?",
    "outdoor": "🌳 Do you enjoy being outdoors?",
    "social": "👥 Do you like working with other people?",
    "time": "⏳ Free time per week?",
    "physical": "💪 Do you enjoy physical activity?",
    "budget": "💰 Budget level?",
    "learning": "📚 Do you enjoy learning new things?",
    "technology": "💻 Interested in technology?",
    "music": "🎵 Do you like music?",
    "patience": "🧘 Are you patient?",
    "competition": "🏆 Do you like competition?",
    "travel": "✈️ Do you like traveling/exploring?",
    "nature": "🌿 Do you like nature?",
    "indoor": "🏠 Prefer indoor activities?",
    "helping": "🤝 Do you enjoy helping others?"
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

# ------------------ TEXT INPUT ------------------
user_input = st.text_area("💬 Tell me anything else about what you like:")
st.divider()

# ------------------ RADAR CHART ------------------
def create_radar_chart(ans):
    labels = list(ans.keys())

    values = []
    for v in ans.values():
        if v == "Yes":
            values.append(1)
        elif v == "No":
            values.append(0)
        elif v in ["Low", "<2 hours"]:
            values.append(0)
        elif v in ["Medium", "2–5 hours"]:
            values.append(0.5)
        else:
            values.append(1)

    values.append(values[0])
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles.append(angles[0])

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    fig.patch.set_facecolor("#0B1208")
    ax.set_facecolor("#16220F")

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color="white", fontsize=8)

    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels(["Low", "Medium", "High"], color="white")

    return fig

# ------------------ HOBBY LOGIC ------------------
def suggest_hobbies(ans, text, age, fitness):
    hobbies = []

    if ans["creative"] == "Yes":
        hobbies += ["🎨 Painting", "🧵 Crafts", "✏️ Sketching"]

    if ans["outdoor"] == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]

    if ans["social"] == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Drama"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if ans["physical"] == "Yes":
        if age <= 45 and fitness in ["Medium", "High"]:
            hobbies += ["🏋️ Gym", "🚴 Cycling"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

    if ans["budget"] == "Low":
        hobbies += ["📖 Reading", "✍️ Writing"]
    elif ans["budget"] == "High":
        hobbies += ["📷 Photography", "🎮 Gaming Setup"]

    if ans["learning"] == "Yes":
        hobbies += ["🌍 Languages", "🧠 Courses"]

    if ans["technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if ans["music"] == "Yes":
        hobbies += ["🎤 Singing", "🎧 Music Production"]

    if ans["patience"] == "Yes":
        hobbies += ["♟️ Chess", "🧩 Model Building"]

    if ans["competition"] == "Yes" and age <= 45:
        hobbies += ["🏆 eSports"]

    if ans["travel"] == "Yes":
        hobbies += ["🗺️ Exploring"]

    if ans["nature"] == "Yes":
        hobbies += ["🌿 Nature Walks"]

    if ans["indoor"] == "Yes":
        hobbies += ["🎮 Gaming"]

    if ans["helping"] == "Yes":
        hobbies += ["🤝 Volunteering"]

    # TEXT MATCH
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

    st.subheader("📊 Your Profile")
    st.pyplot(create_radar_chart(answers))

    hobbies = suggest_hobbies(answers, user_input, age, fitness)

    st.subheader("✨ Recommended Hobbies")

    if hobbies:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].write(hobby)
    else:
        st.write("Try adding more details!")
