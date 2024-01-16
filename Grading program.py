def grade_calculator(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <=60:
        return 'F'
    else:
        return 'Invalid Score'
try:
    user_score = float(input("Enter the student's score: "))

    grade = grade_calculator(user_score)
    print(f"Your grade is: {grade}")
except ValueError:
    print("Please enter a valid score.")
