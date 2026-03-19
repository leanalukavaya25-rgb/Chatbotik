import streamlit as st
from PIL import Image
from collections import OrderedDict

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="🎯",
    layout="centered"
)

# ------------------ SET SUNSET BACKGROUND ------------------
def set_bg(image_url):
    """
    Set a full-screen sunset background image
    """
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

# Use beautiful sunset sunset background
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

/* Inputs & selects */
div.stSelectbox, div.stTextArea, input, textarea {
    background-color: var(--input-bg) !important;
    border-radius: 12px;
    padding: 0.6rem;
    color: var(--text-color) !important;
}

/* Button */
.stButton>button {
    background-color: var(--accent-blue);
    color: var(--text-color);
    font-weight: bold;
    border-radius: 16px;
    padding: 0.7rem 1.2rem;
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
}

/* Hobby cards */
.hobby-card {
    background-color: var(--card-bg);
    border-radius: 16px;
    padding: 1rem;
    margin-bottom: 1rem;
    text-align: center;
    font-weight: 600;
    font-size: 18px;
    transition: all 0.3s ease;
}
.hobby-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<h1 style='text-align:center'>🎨 Find Your Perfect Hobby 🌅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Answer a few questions and let me recommend hobbies just for you!</p>", unsafe_allow_html=True)
st.divider()

# ------------------ QUESTIONS ------------------
questions = {
    "creative": "🎨 Do you prefer creative hobbies?",
    "outdoor": "🌳 Do you enjoy being outdoors?",
    "social": "👥 Do you like working with others?",
    "time": "⏳ Free time per week?",
    "physical": "💪 Do you enjoy physical activity?",
    "budget": "💰 Budget level?",
    "learning": "📚 Do you enjoy learning new things?",
    "technology": "💻 Interested in technology?",
    "music": "🎵 Do you like music?",
    "patience": "🧘 Are you patient?",
    "competition": "🏆 Do you like competition?",
    "travel": "✈️ Do you like exploring?",
    "nature": "🌿 Do you like nature?",
    "indoor": "🏠 Prefer indoor activities?",
    "helping": "🤝 Do you enjoy helping others?"
}

options = {
    "YesNo": ["Yes", "No"],
    "Time": ["<2 hours", "2–5 hours", "5+ hours"],
    "Budget": ["Low", "Medium", "High"]
}

answers = {}
for key, q in questions.items():
    if key == "time":
        answers[key] = st.selectbox(q, options["Time"])
    elif key == "budget":
        answers[key] = st.selectbox(q, options["Budget"])
    else:
        answers[key] = st.selectbox(q, options["YesNo"])

user_input = st.text_area("💬 Tell me more about your interests:", height=130)
st.divider()

# ------------------ HOBBY SUGGESTION ------------------
def suggest_hobbies(answers, user_text=""):
    hobbies = []
    if answers["creative"] == "Yes": hobbies += ["🎨 Painting", "🧵 Crafts"]
    if answers["outdoor"] == "Yes": hobbies += ["🥾 Hiking", "🌱 Gardening"]
    if answers["social"] == "Yes": hobbies += ["⚽ Team Sports", "🎭 Drama"]
    else: hobbies += ["📚 Reading", "✍️ Journaling"]
    if answers["time"] == "<2 hours": hobbies.append("🧩 Puzzles")
    elif answers["time"] == "5+ hours": hobbies.append("🎸 Learning an Instrument")
    if answers["physical"] == "Yes": hobbies += ["🏃 Running", "🏊 Swimming"]
    if answers["budget"] == "Low": hobbies += ["📖 Reading", "✍️ Writing"]
    elif answers["budget"] == "High": hobbies += ["📷 Photography", "🎮 Gaming"]
    if answers["learning"] == "Yes": hobbies += ["🌍 Language Learning", "🧠 Courses"]
    if answers["technology"] == "Yes": hobbies += ["💻 Coding", "🤖 Robotics"]
    if answers["music"] == "Yes": hobbies += ["🎤 Singing", "🎧 Music Production"]
    if answers["patience"] == "Yes": hobbies += ["♟️ Chess", "🧩 Model Building"]
    if answers["competition"] == "Yes": hobbies += ["🏆 eSports", "🥊 Martial Arts"]
    if answers["travel"] == "Yes": hobbies += ["🗺️ Exploring", "📸 Travel Blogging"]
    if answers["nature"] == "Yes": hobbies += ["🌿 Bird Watching", "🍃 Nature Walks"]
    if answers["indoor"] == "Yes": hobbies += ["🎮 Gaming", "🎬 Movies"]
    if answers["helping"] == "Yes": hobbies += ["🤝 Volunteering", "👶 Mentoring"]
    if user_text:
        text = user_text.lower()
        if "art" in text: hobbies.append("🎨 Digital Art")
        if "cook" in text: hobbies.append("👩‍🍳 Cooking")
        if "game" in text: hobbies.append("🎮 Game Dev")
    return list(OrderedDict.fromkeys(hobbies))

if st.button("✨ Suggest Hobbies"):
    results = suggest_hobbies(answers, user_input)
    st.subheader("🌅 Recommended Hobbies For You:")
    if not results:
        st.write("Try adding more details!")
    else:
        cols = st.columns(3)
        for i, hobby in enumerate(results):
            cols[i % 3].markdown(f"<div class='hobby-card'>{hobby}</div>", unsafe_allow_html=True)
