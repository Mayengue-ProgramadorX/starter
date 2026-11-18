import csv


def load_students(file_path):
    """Load those from the students table"""

    # try this if data exists
    try:
        # Read data Students
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            # return list
            return list(reader)

    # if data students does not exist
    except FileNotFoundError:
        print("CSV file does not exist")
        return []


def calculate_average(grades):
    """calculate average and returns the average as a float rounded to 1 decimal place, or None if there are no valid grades."""

    # List comprehension is a way to write code that is clean and clear.
    # This list comprehension iterates through each item in the grades list; it then performs a validation—if an item is not empty, it appends it to valid_grades after converting it to a float.
    valid_grades = [float(grade) for grade in grades if grade != ""]

    # check if there are any notes
    if len(valid_grades) == 0:
        return None

    # calculate average
    average = sum(valid_grades) / len(valid_grades)

    # Round to one decimal place. To do this, we will use round(), passing the parameter we wish to round (in this case, average) and specifying the number of decimal places (in this case, 1), then return the rounded average.
    return round(average, 1)


def get_letter_grade(average):
    """Converts a numeric average into a letter grade."""

    # Check if average is none
    if average is None:
        return None

    # check average
    if average >= 90:
        return "A"  # return just A

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


def generate_report(students):
    """"""

    # It will keep a completed report card for each student (name, average, grade).
    students_results = []

    # You’re only going to keep the average figures.
    all_averages = []

    # To count how many students got each letter.
    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    # each student
    for student in students:

        # put the 4 notes into a list
        grades = [
            student["math"],
            student["science"],
            student["english"],
            student["history"]
        ]

        # get result average
        avg = calculate_average(grades)

        # get letter that corresponds to each average
        letter = get_letter_grade(avg)

        # Keep the student's individual report card
        students_results.append({
            "student_name": student["student_name"],
            "average": avg,
            "grade": letter
        })

        # if avg not none
        if avg is not None:
            all_averages.append(avg)
            grade_distribution[letter] += 1

    # total number of students
    total_students = len(students)

    if len(all_averages) > 0:
        class_average = calculate_average(all_averages)
        highest_average = max(all_averages)
        lowest_average = min(all_averages)
    else:
        class_average = None
        highest_average = None
        lowest_average = None

    # Returns the final dictionary with everything organized.
    return {
        "total_students": total_students,
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_distribution,
        "student_results": students_results,
    }


def write_report(report, filepath):
    """Writes a formatted summary report to a text file."""

    # Creates a file in write mode ("w")
    with open(filepath, "w") as file:

        # Class Header and Statistics
        file.write("=== Student Grade Report ===\n\n")
        file.write("--- Class Summary ---\n")
        file.write(f"Total students:   {report['total_students']}\n")
        file.write(f"Class average:    {report['class_average']}\n")
        file.write(f"Highest average:  {report['highest_average']}\n")
        file.write(f"Lowest average:   {report['lowest_average']}\n\n")

        # Grade Distribution
        file.write("--- Grade Distribution ---\n")
        for grade, count in report["grade_distribution"].items():
            file.write(f"  {grade}: {count}\n")

        file.write("\n")

        # Individual Results for Each Student
        file.write("--- Individual Student Results ---\n")

        for student in report["student_results"]:

            # If the student does not have an average, "N/A" is displayed.
            avg_display = (
                student["average"]
                if student["average"] is not None
                else "N/A"
            )

            file.write(
                f"{student['student_name']}: {avg_display} ({student['grade']})\n"
            )


# main
def main():

    print("Loading student data...")

    students = load_students("data/students.csv")

    print(f"Loaded {len(students)} students.")

    if not students:
        return

    print("Generating report...\n")

    report = generate_report(students)

    print("--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}\n")

    print("Grade Distribution:")

    for grade, count in report["grade_distribution"].items():
        print(f"  {grade}: {count}")

    print()

    print("Top 5 students:")

    # Filters only students with a valid average and sorts them from highest to lowest
    valid_students = [
        s for s in report["student_results"]
        if s["average"] is not None
    ]

    top_5 = sorted(
        valid_students,
        key=lambda s: s["average"],
        reverse=True
    )[:5]

    for student in top_5:
        print(
            f"  {student['student_name']:<20} {student['average']} ({student['grade']})"
        )

    print()

    write_report(report, "grade_report.txt")

    print("Report written to grade_report.txt")


if __name__ == "__main__":
    main()