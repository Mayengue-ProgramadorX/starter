# Grade Tracker

This program reads student grades from a CSV file, calculates averages, assigns letter grades, and generates a summary report.

## Features

### 1. Load Student Data

The program reads data from a CSV file using:

```python
csv.DictReader(file)
```

Each student record contains:

- student_name
- math
- science
- english
- history

Some grades may be empty.

---

### 2. Average Calculation

Student averages are calculated using:

```python
calculate_average(grades)
```

The function:

- Ignores empty grades
- Converts grades to float
- Calculates the average
- Rounds the result to 1 decimal place

---

### 3. Letter Grade Assignment

Letter grades are assigned using:

```python
get_letter_grade(average)
```

Grade scale:

- A = 90+
- B = 80-89
- C = 70-79
- D = 60-69
- F = Below 60

---

### 4. Report Generation

The program generates:

- Total students
- Class average
- Highest average
- Lowest average
- Grade distribution
- Individual student results

---

### 5. Report File Output

The report is saved as:

```text
grade_report.txt
```

The file includes class statistics and student grades.

---

## How to Run

```bash
python main.py
```

---

## Example Output

```text
Loading student data...
Loaded 10 students.

--- Summary ---
Total students: 10
Class average: 84.5
Highest average: 96.0
Lowest average: 65.3

Grade Distribution:
A: 3
B: 4
C: 2
D: 1
F: 0

Report written to grade_report.txt
```