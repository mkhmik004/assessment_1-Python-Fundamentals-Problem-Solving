# Question 1
def get_student_year(student_id: str):
    """
    STEP 1: The student ID format is 'abcdjhb024' (where '024' is the year 2024).
    TODO: Extract the last 3 digits to determine the year.
    Return the year as a full 4-digit string (e.g., '2024').
    
    Hint: Use slicing with negative indexes and an f-string.
    """
    return

# print(get_student_year('abcdjhb024')) # Should return '2024'


# Question 2
def get_username(email_address: str):
    """
    STEP 2: Extract the username from the student email.
    Format: 'abcdjhb024@student.wethinkcode.co.za'
    TODO: Return just the 'abcdjhb024' part.
    
    Hint: You can use the .split() method or finding the index of '@'.
    """
    return

# print(get_username('abcdjhb024@student.wethinkcode.co.za'))


# Question 3
def get_campus(student_id: str):
    """
    STEP 3: Determine the campus based on the student ID.
    Format: 'abcdjhb024' or 'abcdcpt024' or 'abcddbn024'.
    
    Logic:
    - If 'jhb' is in the student_id, return 'Johannesburg'.
    - If 'cpt' is in the student_id, return 'Cape Town'.
    - If 'dbn' is in the student_id, return 'Durban'.
    - Otherwise, return 'Remote'.
    """
    return

# print(get_campus('abcdcpt024')) # Should return 'Cape Town'


# Question 4
def cohort_check(n: int):
    """
    TODO: Write a function that prints numbers from 1 to n.
    - For multiples of 3, print "Cohort".
    - For multiples of 5, print "Group".
    - For multiples of both 3 and 5, print "CohortGroup".
    - Otherwise, print the number.
    """
    return

# cohort_check(15)


# Question 5
def check_student_progress(score: int):
    """
    TODO: Using TDD (Test Driven Development), implement tests for the logic below.
    Create a test file called `test_progress.py`.
    
    Logic for the function:
    1. If score is less than 0 or greater than 100, return 'Invalid Score'.
    2. If score is 0, return 'No Submission'.
    3. For valid positive scores:
       - If score is below 50 (exclusive), return 'Fail'.
       - If score is 50 or above, but odd, return 'Pass - Review Needed'.
       - If score is 50 or above, and even, return 'Pass - Good'.
       - However! If the score is exactly 100, return 'Perfect'.
    """
    return