import streamlit as st
from PIL import Image

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="favicon.png",
    layout="centered"
)

# ------------------ LOAD LOGO ------------------
logo = Image.open("Logo.png")
st.image(logo, width=220)

# ------------------ TITLE ------------------
st.title("🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾")
st.write("Answer these questions and I'll suggest hobbies just for you!")

st.divider()

# ------------------ QUESTIONS ------------------

creative = st.selectbox("🎨 Do you prefer creative hobbies?", ["Yes", "No"])
outdoor = st.selectbox("🌳 Do you enjoy being outdoors?", ["Yes", "No"])
social = st.selectbox("👥 Do you like working with other people?", ["Yes", "No"])
time = st.selectbox("⏳ Free time per week?", ["<2 hours", "2–5 hours", "5+ hours"])

physical = st.selectbox("💪 Do you enjoy physical activity?", ["Yes", "No"])
budget = st.selectbox("💰 Budget level?", ["Low", "Medium", "High"])
learning = st.selectbox("📚 Do you enjoy learning new things?", ["Yes", "No"])
technology = st.selectbox("💻 Interested in technology?", ["Yes", "No"])
music = st.selectbox("🎵 Do you like music?", ["Yes", "No"])
patience = st.selectbox("🧘 Are you patient?", ["Yes", "No"])
competition = st.selectbox("🏆 Do you like competition?", ["Yes", "No"])
travel = st.selectbox("✈️ Do you like traveling/exploring?", ["Yes", "No"])
nature = st.selectbox("🌿 Do you like nature?", ["Yes", "No"])
indoor = st.selectbox("🏠 Prefer indoor activities?", ["Yes", "No"])
helping = st.selectbox("🤝 Do you enjoy helping others?", ["Yes", "No"])

# ------------------ QUESTION BOX ------------------
user_input = st.text_input("💬 Tell me anything else about what you like:")

st.divider()

# ------------------ BUTTON ------------------
if st.button("✨ Suggest Hobbies"):

    hobbies = []

    # Base logic
    if creative == "Yes":
        hobbies += ["🎨 Painting", "🧵 Crafts", "✏️ Sketching"]

    if outdoor == "Yes":
        hobbies += ["🥾 Hiking", "🌱 Gardening"]

    if social == "Yes":
        hobbies += ["⚽ Team Sports", "🎭 Drama"]
    else:
        hobbies += ["📚 Reading", "✍️ Journaling"]

    if time == "<2 hours":
        hobbies.append("🧩 Puzzles")
    elif time == "5+ hours":
        hobbies.append("🎸 Learning an Instrument")

    # Extra logic
    if physical == "Yes":
        hobbies += ["🏋️ Gym", "🚴 Cycling"]

    if budget == "Low":
        hobbies += ["📖 Reading", "✍️ Writing"]
    elif budget == "High":
        hobbies += ["📷 Photography", "🎮 Gaming Setup"]

    if learning == "Yes":
        hobbies += ["🌍 Learning Languages", "🧠 Online Courses"]

    if technology == "Yes":
        hobbies += ["💻 Coding", "🤖 Robotics"]

    if music == "Yes":
        hobbies += ["🎤 Singing", "🎧 Music Production"]

    if patience == "Yes":
        hobbies += ["♟️ Chess", "🧩 Model Building"]

    if competition == "Yes":
        hobbies += ["🏆 eSports", "🥊 Martial Arts"]

    if travel == "Yes":
        hobbies += ["🗺️ Exploring", "📸 Travel Blogging"]

    if nature == "Yes":
        hobbies += ["🌿 Nature Walks", "🐦 Bird Watching"]

    if indoor == "Yes":
        hobbies += ["🎮 Gaming", "🎬 Movies"]

    if helping == "Yes":
        hobbies += ["🤝 Volunteering", "👶 Mentoring"]

    # ------------------ SMART TEXT INPUT LOGIC ------------------
    if user_input:
        text = user_input.lower()

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
    hobbies = list(set(hobbies))

    # ------------------ OUTPUT ------------------
    st.subheader("✨ Recommended Hobbies For You:")

    for hobby in hobbies:
        st.write(hobby)

    st.success("🎉 Try a few and see what you love!")
