import streamlit as st
from PIL import Image
from collections import OrderedDict
import base64

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="favicon.png",
    layout="centered"
)

# ------------------ BACKGROUND IMAGE ------------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("a_digital_photograph_showcases_a_living_room_bathe.png")

# ------------------ CUSTOM CSS ------------------
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
.css-1d391kg { margin-bottom: 2rem; }
div.stSelectbox, div.stTextArea, input, textarea {
    background-color: var(--secondary-bg) !important;
    border-radius: 12px;
    padding: 0.5rem;
    color: var(--text-color) !important;
}
.stButton>button {
    background-color: var(--main-bg);
    color: var(--text-color);
    font-weight: bold;
    border-radius: 12px;
    padding: 0.5rem 1rem;
    border: 1px solid var(--accent-blue);
    transition: all 0.2s ease;
}
.stButton>button:hover {
    background-color: var(--secondary-bg);
    border: 1px solid var(--text-color);
}
hr { border: 1px solid var(--secondary-bg); }
h1, h2, h3, h4 { color: var(--text-color); }
a { color: var(--accent-blue); }
</style>
""", unsafe_allow_html=True)

# ------------------ LOAD LOGO ------------------
try:
    logo = Image.open("Logo.png")
    st.image(logo, width=220)
except:
    st.write("🏷️ Logo not found. Place 'Logo.png' in the folder.")

# ------------------ TITLE ------------------
st.title("🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾")
st.write("Answer these questions and I'll suggest hobbies just for you!")
st.divider()

# ------------------ PERSONAL QUESTIONS ------------------
st.subheader("🧍 Personal Info")
age = st.number_input("🗓️ Age", min_value=5, max_value=100, value=25)
fitness = st.selectbox("💪 Fitness Level", ["Low", "Medium", "High"])
stress_level = st.selectbox("😌 Stress Level", ["Low", "Medium", "High"])
work_hours = st.selectbox("⌛ Weekly Work Hours", ["<20", "20-40", "40+"])
sleep_hours = st.selectbox("🛌 Average Sleep Hours", ["<5", "5-7", "7+"])


# ------------------ HOBBY QUESTIONS ------------------
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
def suggest_hobbies(answers, user_text="", age=25, fitness="Medium"):
    hobbies = []

    # Base logic
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

    # Physical activities - age and fitness aware
    if answers["physical"] == "Yes":
        if age <= 45 and fitness in ["Medium", "High"]:
            hobbies += ["🏋️ Gym", "🚴 Cycling", "🥊 Martial Arts"]
        else:
            hobbies += ["🚶 Walking", "🧘 Yoga"]

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
    if answers["competition"] == "Yes" and age <= 45:
        hobbies += ["🏆 eSports"]
    if answers["travel"] == "Yes":
        hobbies += ["🗺️ Exploring", "📸 Travel Blogging"]
    if answers["nature"] == "Yes":
        hobbies += ["🌿 Nature Walks", "🐦 Bird Watching"]
    if answers["indoor"] == "Yes":
        hobbies += ["🎮 Gaming", "🎬 Movies"]
    if answers["helping"] == "Yes":
        hobbies += ["🤝 Volunteering", "👶 Mentoring"]

    # Smart text input
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

    # Remove duplicates
    return list(OrderedDict.fromkeys(hobbies))

# ------------------ DISPLAY HOBBIES ------------------
if st.button("✨ Suggest Hobbies"):
    hobbies = suggest_hobbies(answers, user_input, age=age, fitness=fitness)

    st.subheader("✨ Recommended Hobbies For You:")

    if not hobbies:
        st.write("Hmm… we couldn't find a match! Try adding more details.")
    else:
        cols = st.columns(3)
        for i, hobby in enumerate(hobbies):
            cols[i % 3].write(hobby)
