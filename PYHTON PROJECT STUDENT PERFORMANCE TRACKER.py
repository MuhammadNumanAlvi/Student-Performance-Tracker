class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        for score in self.scores:
            if score < passing_score:
                return False
        return True


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0

        total_scores = 0
        for student in self.students.values():
            total_scores += student.calculate_average()

        class_average = total_scores / len(self.students)
        return class_average

    def display_student_performance(self):
        for student in self.students.values():
            avg = student.calculate_average()
            if student.is_passing():
                status = "Passing"
            else:
                status = "Failing"
            print("Student:", student.name)
            print("Average Score:", round(avg, 2))
            print("Status:", status)
            print("-" * 20)


def get_student_input():
    while True:
        try:
            name = input("Enter student's name ('finish' to finish the program): ").strip()
            if name.lower() == 'finish':
                break
            scores = []
            for subject in ['math', 'science', 'English']:
                score = int(input(f"Enter {name}'s score for {subject}: "))
                scores.append(score)
            yield name, scores
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")


def main():
    tracker = PerformanceTracker()

    print("=" * 50)
    print(" Welcome to the Student Performance Tracker ".center(50, "="))
    print("=" * 50)

    print("Please enter student information (type 'finish' to finish):\n")
    for name, scores in get_student_input():
        tracker.add_student(name, scores)

    if tracker.students:
        print("\n--- Student Performance Summary ---")
        tracker.display_student_performance()

        print("\n--- Overall Class Performance ---")
        class_average = tracker.calculate_class_average()
        print(f"Class Average Score: {class_average:.2f}")
    else:
        print("\nNo student data entered. Exiting program...\n")

    print("\n=====================================")
    print("   Thank you for using the Tracker!")
    print("=====================================\n")


if __name__ == "__main__":
    main()
