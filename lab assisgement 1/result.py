students = []

def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / 3

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

for i in range(5):
    print("\nEnter information for Student", i + 1)

    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")

    marks = {}

    marks["Python"] = float(input("Enter Python marks: "))
    marks["Artificial Intelligence"] = float(input("Enter Artificial Intelligence marks: "))
    marks["Mathematics"] = float(input("Enter Mathematics marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

highest_student = None

with open("results.txt", "w") as file:
    file.write("STUDENT RESULTS\n")
    file.write("=" * 40 + "\n\n")

    for student in students:
        total, percentage, grade = calculate_result(student["marks"])

        student["total"] = total
        student["percentage"] = percentage
        student["grade"] = grade

        result = (
            "Name: " + student["name"] + "\n"
            + "Roll No: " + student["roll_no"] + "\n"
            + "Total Marks: " + str(total) + "/300\n"
            + "Percentage: " + str(round(percentage, 2)) + "%\n"
            + "Grade: " + grade + "\n"
            + "-" * 40 + "\n"
        )

        print("\n" + result)
        file.write(result + "\n")

        if highest_student is None:
            highest_student = student
        elif percentage > highest_student["percentage"]:
            highest_student = student

print("\nHighest Percentage Student:")
print("Name:", highest_student["name"])
print("Roll Number:", highest_student["roll_no"])
print("Percentage:", round(highest_student["percentage"], 2), "%")
print("Grade:", highest_student["grade"])

print("\nAll results have been saved in results.txt")