import csv


def load_students(file_path):
    """Load those from the students table"""

    #try this if data exists
    try: 
        #Read data Students
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            print(reader.fieldnames)  # Get CSV column names

            students = list(reader) # Store all students in a list
            total_students = len(students) #get total number students

            #return like dictionary 
            return{
                "students": students,
                "total_students": total_students,      
            }
     
    #if data students does not exist
    except FileNotFoundError:
         return {
            "total_students": 0,
            "students": [],
            "error": "CSV file does not exist"
        }


#main
def main():

   result =  load_students("data/students.csv")
   print(f"Loaded {result['total_students']} students.")

   for student in result["students"]:
        for column, value in student.items():
                print(f"{column}: {value}")

if __name__ == "__main__":
    main()