import streamlit as st
from collections import OrderedDict

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="🎯",
    layout="centered"
)

# ------------------ BACKGROUND IMAGE ------------------
def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Sunset background (unchanged)
set_bg("https://images.unsplash.com/photo-1688654966974-1770f23f3943?auto=format&fit=crop&w=1350&q=80")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

:root {
    --accent-blue: #1E3A8A;
    --hover-blue: #2746B0;
    --text-color: #FFFFFF;
    --card-bg: rgba(0, 0, 0, 0.6);
    --input-bg: rgba(0, 0, 0, 0.5);
}

body, .stApp {
    font-family: 'Roboto', sans-serif;
    color: var(--text-color);
}

/* Bubble style for selectboxes, text area, inputs */
div.stSelectbox, div.stTextArea, input, textarea {
    background-color: var(--input-bg) !important;
    border-radius: 30px;
    padding: 0.8rem;
    color: var(--text-color) !important;
    font-size: 16px;
    margin-bottom: 1rem;
}

/* Buttons */
.stButton>button {
    background-color: var(--accent-blue);
    color: var(--text-color);
    font-weight: bold;
    border-radius: 50px;
    padding: 0.8rem 1.5rem;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: var(--hover-blue);
    transform: translateY(-2px);
}

/* Divider */
hr {
    border: 1px solid var(--hover-blue);
    margin: 1.5rem 0;
}

/* Hobby card bubbles */
.hobby-card {
    background-color: var(--card-bg);
    border-radius: 30px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    text-align: center;
    font-weight: 600;
    font-size: 18px;
    transition: all 0.3s ease;
    box-shadow: 0 3px 10px rgba(0,0,0,0.5);
}
.hobby-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.7);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<h1 style='text-align:center'>🎨 Find Your Perfect Hobby 🌅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Answer a few questions and discover hobbies just for you!</p>", unsafe_allow_html=True)
st.divider()

# ------------------ PERSONAL QUESTIONS ------------------
st.subheader("👤 Personal Information")
age = st.number_input("🧓 Your age:", min_value=10, max_value=100, value=25)
fitness = st.selectbox("💪 Fitness Level:", ["Low", "Medium", "High"])
stress = st.selectbox("😌 Stress Level:", ["Low", "Medium", "High"])
work_hours = st.selectbox("🕒 Weekly work hours:", ["<20", "20-40", "40-60", "60+"])
environment = st.selectbox("🏠 Preferred environment:", ["Indoor", "Outdoor", "Both"])

st.divider()

# ------------------ HOBBY PREFERENCE QUESTIONS ------------------
st.subheader("🎯 Hobby Preferences")
questions = {
    "creative": "🎨 Do you prefer creative hobbies?",
    "outdoor": "🌳 Do you enjoy being outdoors?",
    "social": "👥 Do you like working with others?",
    "time": "⏳ Free time per week?",
    "technology": "💻 Interested in technology?",
    "music": "🎵 Do you like music?",
    "patience": "🧘 Are you patient?",
    "competition": "🏆 Do you like competition?",
    "travel": "✈️ Do you like exploring?",
    "nature": "🌿 Do you like nature?",
    "helping": "🤝 Do you enjoy helping others?"
}

options = {
    "YesNo": ["Yes", "No"],
    "Time": ["<2 hours", "2–5 hours", "5+ hours"]
}

answers = {}
for key, q in questions.items():
    answers[key] = st.selectbox(q, options["YesNo"]) if key != "time" else st.selectbox(q, options["Time"])

user_input = st.text_area("💬 Tell me more about your interests:", height=130)
st.divider()

# ------------------ HOBBY SUGGESTION FUNCTION ------------------
def suggest_hobbies(answers, age, fitness, user_text=""):
    hobbies = []

    # Creative & Mental
    if answers["creative"] == "Yes":
        hobbies += ["🎨 Painting", "🧵 Crafts", "✏️ Sketching"]
    if answers["technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]
    if answers["music"] == "Yes":
        hobbies += ["🎤 Singing", "🎧 Music Production"]
    if answers["patience"] == "Yes":
        hobbies += ["♟️ Chess", "🧩 Model Building"]

    # Outdoor / Nature
    if answers["outdoor"] == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]
        if age <= 45 and fitness != "Low":  # only suggest physical if under 45 or moderate fitness
            hobbies += ["🏋️ Gym", "🚴 Cycling", "🏊 Swimming"]

    # Social / Indoor
    if answers["social"] == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Drama"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    # Time-based hobbies
    if answers["time"] == "<2 hours": hobbies.append("🧩 Puzzles")
    elif answers["time"] == "5+ hours": hobbies.append("🎸 Learning an Instrument")

    # Travel / Nature
    if answers["travel"] == "Yes":
        hobbies += ["🗺️ Exploring", "📸 Travel Blogging"]
    if answers["nature"] == "Yes":
        hobbies += ["🌿 Bird Watching", "🍃 Nature Walks"]

    # Helping / competition
    if answers["helping"] == "Yes": hobbies += ["🤝 Volunteering", "👶 Mentoring"]
    if answers["competition"] == "Yes": hobbies += ["🏆 eSports", "🥊 Martial Arts"]

    # Adjust based on personal preferences
    if environment == "Indoor": hobbies = [h for h in hobbies if "🎮" in h or "📚" in h or "🎨" in h or "💻" in h]
    elif environment == "Outdoor": hobbies = [h for h in hobbies if "🥾" in h or "🌱" in h or "🚴" in h or "🏊" in h]

    # User text input logic
    if user_text:
        text = user_text.lower()
        if "art" in text: hobbies.append("🎨 Digital Art")
        if "cook" in text: hobbies.append("👩‍🍳 Cooking")
        if "game" in text: hobbies.append("🎮 Game Development")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ DISPLAY HOBBIES ------------------
if st.button("✨ Suggest Hobbies"):
    results = suggest_hobbies(answers, age, fitness, user_input)
    st.subheader("🌅 Recommended Hobbies For You:")
    if not results:
        st.write("Try adding more details!")
    else:
        cols = st.columns(3)
        for i, hobby in enumerate(results):
            cols[i % 3].markdown(f"<div class='hobby-card'>{hobby}</div>", unsafe_allow_html=True)
