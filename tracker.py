class Tracker:
    """Tracks learner performance and calculates metrics."""
    def __init__(self):
        self.records = []

    def record(self, correct, time_taken):
        self.records.append({"correct": correct, "time": time_taken})

    def summary(self):
        total = len(self.records)
        correct = sum(1 for r in self.records if r["correct"])
        accuracy = (correct / total * 100) if total else 0
        avg_time = (sum(r["time"] for r in self.records) / total) if total else 0
        return accuracy, avg_time
