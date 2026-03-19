import streamlit as st
from PIL import Image

# ------------------ PAGE CONFIG (FAVICON) ------------------
st.set_page_config(
    page_title="Find Your Hobby",
    page_icon="favicon.png",  # ✅ Your custom favicon file
    layout="centered"
)

# ------------------ LOAD IMAGES ------------------
logo = Image.open("Logo.png")

# ------------------ HEADER ------------------
st.image(logo, width=220)

st.title("🎨🏀⚽ Find Your Hobby ♟️👩🏻‍🍳🎾")
st.write("Answer a few questions and I'll suggest hobbies for you!")

st.divider()

# ------------------ QUESTIONS ------------------
creative = st.selectbox(
    "🎨 Do you prefer creative hobbies?",
    ["Yes", "No"]
)

outdoor = st.selectbox(
    "🌳 Do you enjoy being outdoors?",
    ["Yes", "No"]
)

social = st.selectbox(
    "👥 Do you like working with other people?",
    ["Yes", "No"]
)

time = st.selectbox(
    "⏳ How much free time do you have each week?",
    ["Less than 2 hours", "2-5 hours", "5+ hours"]
)

st.divider()

# ------------------ BUTTON ------------------
if st.button("✨ Suggest Hobbies"):

    hobbies = []

    if creative == "Yes":
        hobbies.append("🎨 Drawing or Painting")
        hobbies.append("🧵 DIY Crafts")

    if outdoor == "Yes":
        hobbies.append("🥾 Hiking")
        hobbies.append("🌱 Gardening")

    if social == "Yes":
        hobbies.append("⚽ Team Sports")
        hobbies.append("🎭 Drama Club")
    else:
        hobbies.append("📚 Reading")
        hobbies.append("✍️ Journaling")

    if time == "Less than 2 hours":
        hobbies.append("🧩 Puzzles")
    elif time == "5+ hours":
        hobbies.append("🎸 Learning an Instrument")

    if not hobbies:
        hobbies.append("🎲 Board Games")

    # ------------------ OUTPUT ------------------
    st.subheader("✨ Recommended Hobbies For You:")

    for hobby in hobbies:
        st.write(hobby)

    st.success("🎉 Hope you found something fun to try!")
