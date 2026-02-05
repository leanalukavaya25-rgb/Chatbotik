questions = [
    "How do you usually like to spend your free time?",
    "Do you prefer creative or active hobbies?",
    "Do you enjoy being outdoors?",
    "Do you like working alone or with others?",
    "How much time do you want to spend on a hobby each week?"
]

def suggest_hobbies(answers):
    hobbies = []

    if "creative" in answers.lower():
        hobbies.append("🎨 Drawing or Painting")
    if "outdoor" in answers.lower():
        hobbies.append("🌿 Hiking or Nature Walking")
    if "people" in answers.lower() or "others" in answers.lower():
        hobbies.append("🤝 Group Sports or Clubs")
    if "alone" in answers.lower():
        hobbies.append("📚 Reading or Journaling")

    if not hobbies:
        hobbies = [
            "📸 Photography",
            "✍️ Creative Writing",
            "🧩 Puzzles or Games"
        ]

    return hobbies
