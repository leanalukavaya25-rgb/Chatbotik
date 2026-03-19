import streamlit as st
from PIL import Image
from collections import OrderedDict

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="🎯",
    layout="centered"
)

# ------------------ CUSTOM CSS FOR FUN MODERN DARK THEME ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

:root {
    --main-bg: #0B1208;       /* ultra dark olive */
    --secondary-bg: #16220F;  /* input background */
    --accent-blue: #1E3A8A;   /* subtle blue */
    --hover-blue: #2746B0;    /* hover glow */
    --text-color: #E5E5E5;    /* off-white text */
    --card-bg: #1F2C14;       /* hobby card background */
}

/* Global app background and font */
body, .stApp {
    background: linear-gradient(135deg, var(--main-bg), #051207);
    color: var(--text-color);
    font-family: 'Roboto', sans-serif;
}

/* Logo spacing */
.css-1d391kg {
    margin-bottom: 2rem;
}

/* Inputs & Selectboxes */
div.stSelectbox, div.stTextArea, input, textarea {
    background-color: var(--secondary-bg) !important;
    border-radius: 14px;
    padding: 0.6rem;
    color: var(--text-color) !important;
    font-size: 16px;
}

/* Button styling */
.stButton>button {
    background-color: var(--accent-blue);
    color: var(--text-color);
    font-weight: bold;
    border-radius: 16px;
    padding: 0.7rem 1.2rem;
    border: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(30, 58, 138, 0.5);
}
.stButton>button:hover {
    background-color: var(--hover-blue);
    box-shadow: 0 6px 20px rgba(39, 70, 176, 0.7);
    transform: translateY(-2px);
}

/* Divider color */
hr {
    border: 1px solid #2746B0;
}

/* Titles */
h1, h2, h3, h4 {
    color: var(--text-color);
}

/* Hobby card design */
.hobby-card {
    background-color: var(--card-bg);
    border-radius: 16px;
    padding: 1rem;
    margin-bottom: 1rem;
    text-align: center;
    font-weight: 600;
    font-size: 18px;
    transition: all 0.3s ease;
    box-shadow: 0 3px 10px rgba(0,0,0,0.5);
}
.hobby-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(39, 70, 176, 0.7);
}

/* Links / accent text */
a {
    color: var(--accent-blue);
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ------------------ LOAD LOGO ------------------
try:
    logo = Image.open("Logo.png")
    st.image(logo, width=220)
except:
    st.write("🏷️ Logo not found. Place 'Logo.png' in the folder.")

# ------------------ TITLE ------------------
st.markdown("<h1 style='text-align:center'>🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px'>Answer these questions and I'll suggest hobbies just for you!</p>", unsafe_allow_html=True)
st.divider()

# ------------------ QUESTIONS ------------------
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

# ------------------ BIG TEXT AREA ------------------
user_input = st.text_area(
    "💬 Tell me anything else about what you like:",
    height=150
)
st.divider()

# ------------------ HOBBY SUGGESTION FUNCTION ------------------
def suggest_hobbies(answers, user_text=""):
    hobbies = []

    if answers["creative"] == "Yes":
        hobbies += ["🎨 Painting", "🧵 Crafts", "✏️ Sketching"]
    if answers["outdoor"] == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]
    if answers["social"] == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Drama"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if answers["time"] == "<2 hours":
        hobbies.append("🧩 Puzzles")
    elif answers["time"] == "5+ hours":
        hobbies.append("🎸 Learning an Instrument")

    if answers["physical"] == "Yes":
        hobbies += ["🏋️ Gym", "🚴 Cycling"]
    if answers["budget"] == "Low":
        hobbies += ["📖 Reading", "✍️ Writing"]
    elif answers["budget"] == "High":
        hobbies += ["📷 Photography", "🎮 Gaming Setup"]
    if answers["learning"] == "Yes":
        hobbies += ["🌍 Learning Languages", "🧠 Online Courses"]
    if answers["technology"] == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]
    if answers["music"] == "Yes":
        hobbies += ["🎤 Singing", "🎧 Music Production"]
    if answers["patience"] == "Yes":
        hobbies += ["♟️ Chess", "🧩 Model Building"]
    if answers["competition"] == "Yes":
        hobbies += ["🏆 eSports", "🥊 Martial Arts"]
    if answers["travel"] == "Yes":
        hobbies += ["🗺️ Exploring", "📸 Travel Blogging"]
    if answers["nature"] == "Yes":
        hobbies += ["🌿 Nature Walks", "🐦 Bird Watching"]
    if answers["indoor"] == "Yes":
        hobbies += ["🎮 Gaming", "🎬 Movies"]
    if answers["helping"] == "Yes":
        hobbies += ["🤝 Volunteering", "👶 Mentoring"]

    if user_text:
        text = user_text.lower()
        if "art" in text:
            hobbies.append("🎨 Digital Art")
        if "game" in text:
            hobbies.append("🎮 Game Development")
        if "cook" in text:
            hobbies.append("👩‍🍳 Cooking")
        if "sport" in text:
            hobbies.append("⚽ Sports Practice")
        if "music" in text:
            hobbies.append("🎼 Composing Music")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ DISPLAY HOBBIES ------------------
if st.button("✨ Suggest Hobbies"):
    hobbies = suggest_hobbies(answers, user_input)
    
    st.subheader("✨ Recommended Hobbies For You:")

    if not hobbies:
        st.write("Hmm… we couldn't find a match! Try adding more details.")
    else:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].markdown(f"<div class='hobby-card'>{hobby}</div>", unsafe_allow_html=True)
