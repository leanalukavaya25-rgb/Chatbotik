import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Find Your Hobby", page_icon="🎯")

# ------------------ TITLE ------------------
st.title("🎨 Find Your Perfect Hobby")
st.write("Answer a few questions and get hobby suggestions!")

st.divider()

# ------------------ INPUTS ------------------
age = st.slider("Age", 5, 100, 25)
fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])

st.subheader("Preferences")

answers = {
    "Creative": st.selectbox("Creative?", ["No", "Yes"]),
    "Outdoor": st.selectbox("Outdoor?", ["No", "Yes"]),
    "Social": st.selectbox("Social?", ["No", "Yes"]),
    "Physical": st.selectbox("Physical?", ["No", "Yes"]),
    "Tech": st.selectbox("Tech?", ["No", "Yes"])
}

user_text = st.text_area("Extra preferences (optional)")

# ------------------ RADAR CHART ------------------
def create_radar(data):
    labels = list(data.keys())
    values = [1 if v == "Yes" else 0 for v in data.values()]

    # close shape
    values.append(values[0])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles.append(angles[0])

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#0B1208")
    ax.set_facecolor("#16220F")

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.3)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["No", "Yes"])

    return fig

# ------------------ HOBBY LOGIC ------------------
def suggest_hobbies(ans, text, age, fitness):
    hobbies = []

    if ans["Creative"] == "Yes":
        hobbies.append("🎨 Painting")

    if ans["Outdoor"] == "Yes":
        hobbies.append("🥾 Hiking")

    if ans["Social"] == "Yes":
        hobbies.append("⚽ Team Sports")
    else:
        hobbies.append("📚 Reading")

    if ans["Physical"] == "Yes":
        if age < 45 and fitness != "Low":
            hobbies.append("🏋️ Gym")
        else:
            hobbies.append("🚶 Walking")

    if ans["Tech"] == "Yes":
        hobbies.append("💻 Coding")

    # text input
    text = text.lower()
    if "cook" in text:
        hobbies.append("👩‍🍳 Cooking")
    if "music" in text:
        hobbies.append("🎵 Music")

    return list(OrderedDict.fromkeys(hobbies))

# ------------------ BUTTON ------------------
if st.button("✨ Find My Hobby"):

    st.subheader("📊 Your Profile")
    st.pyplot(create_radar(answers))

    hobbies = suggest_hobbies(answers, user_text, age, fitness)

    st.subheader("✨ Suggested Hobbies")

    if hobbies:
        for h in hobbies:
            st.write(h)
    else:
        st.write("Try selecting more options!")
