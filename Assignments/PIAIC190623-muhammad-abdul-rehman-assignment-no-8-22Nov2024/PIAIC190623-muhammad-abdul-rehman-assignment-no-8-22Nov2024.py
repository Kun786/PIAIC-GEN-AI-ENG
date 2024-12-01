def manage_student_database():
    students = []  # List to store student tuples
    student_id = 1  # Sequential ID starting from 1

    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()

        if name.lower() == "stop":
            break

        # Check for duplicate names
        if any(student[1] == name for student in students):
            print("This name is already in the list.")
            continue

        # Add student as a tuple (ID, Name)
        students.append((student_id, name))
        student_id += 1

    # Display complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student's ID and name
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Calculate statistics
    total_students = len(students)
    total_length_of_names = sum(len(student[1]) for student in students)
    longest_name = max(students, key=lambda x: len(x[1]))[1] if students else "N/A"
    shortest_name = min(students, key=lambda x: len(x[1]))[1] if students else "N/A"

    # Display statistics
    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_length_of_names}")
    print(f"The student with the longest name is: {longest_name}")
    print(f"The student with the shortest name is: {shortest_name}")


if __name__ == "__main__":
    manage_student_database()
