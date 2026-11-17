grades = [15, 18, 12, "", 10, ""]

def calculate_average(grades):
    """calculate average and returns the average as a float rounded to 1 decimal place, or None if there are no valid grades."""
        
    #List comprehension is a way to write code that is clean and clear.
    #This list comprehension iterates through each item in the `grades` list; it then performs a validation—if an item is not empty, it appends it to `valid_grades` after converting it to a float.
    valid_grades = [float(grade) for grade in grades if grade !=""]

    #check if there are any notes
    if len(valid_grades) == 0:
        return None
    
    #calculate average
    average = sum(valid_grades) / len(valid_grades)

    #Round to one decimal place. To do this, we will use `round()`, passing the parameter we wish to round (in this case, `average`) and specifying the number of decimal places (in this case, 1), then return the rounded `average`.
    return round(average, 1)
result = calculate_average(grades)
print(result)
