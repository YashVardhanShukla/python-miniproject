def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    try:
        score = float(input("Enter the student's score: "))
        if score < 0 or score > 100:
            print("Invalid score! Score must be between 0 and 100.")
        else:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
