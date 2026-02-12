import streamlit as st

st.title("🎯 Hobby & Interests Chatbot")
st.write("Answer a few questions and I'll suggest hobbies for you!")

# Questions
creative = st.selectbox("Do you prefer creative hobbies?", ["Yes", "No"])
outdoor = st.selectbox("Do you enjoy being outdoors?", ["Yes", "No"])
social = st.selectbox("Do you like working with other people?", ["Yes", "No"])
time = st.selectbox("How much free time do you have each week?", 
                    ["Less than 2 hours", "2-5 hours", "5+ hours"])

# Button
if st.button("Suggest Hobbies"):
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

    if social == "No":
        hobbies.append("📚 Reading")
        hobbies.append("✍️ Journaling")

    if time == "Less than 2 hours":
        hobbies.append("🧩 Puzzles")
    elif time == "5+ hours":
        hobbies.append("🎸 Learning an Instrument")

    if not hobbies:
        hobbies.append("🎲 Board Games")

    st.subheader("✨ Recommended Hobbies For You:")
    for hobby in hobbies:
        st.write(hobby)
