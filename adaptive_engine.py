def next_difficulty(current_level, accuracy, avg_time):
    """Rule-based logic to adjust difficulty based on performance."""
    if accuracy > 80 and avg_time < 5:
        if current_level == "Easy":
            return "Medium"
        if current_level == "Medium":
            return "Hard"
    if accuracy < 50 or avg_time > 10:
        if current_level == "Hard":
            return "Medium"
        if current_level == "Medium":
            return "Easy"
    return current_level
