'''
You have a record of  students.
Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer  followed by the names and marks for students.
are required to save the record in a dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Calculate average salary
    a = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Print to the second decimal
    print("%.2f" % a)
