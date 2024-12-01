class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students have been added yet!")
            return

        print("\nStudent Performance:")
        print("-" * 30)
        for name, student in self.students.items():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Name: {name}, Average Score: {avg_score:.2f}, Status: {status}")

        print("-" * 30)
        print(f"Class Average: {self.calculate_class_average():.2f}")
        print("-" * 30)


def main():
    tracker = PerformanceTracker()

    while True:
        print("\nEnter student details:")
        name = input("Name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        try:
            scores = []
            for subject in ["Math", "Science", "English"]:
                score = int(input(f"Enter {subject} score: "))
                scores.append(score)
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")

    tracker.display_student_performance()


if __name__ == "__main__":
    main()
