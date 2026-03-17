from ai.habit_learning import analyze_user_habits
from ai.mistake_detector import detect_previous_error


def build_ai_response():

    habit = analyze_user_habits()
    error = detect_previous_error()

    messages = []

    if habit:
        messages.append(habit)

    if error:
        messages.append(error)

    return "\n".join(messages)