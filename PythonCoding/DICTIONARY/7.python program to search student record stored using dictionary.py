student_id=int(input("Enter the Student id:"))
student_records={
    101: {'name': 'Tharun', 'age': 23, 'grade': 'A'},
    102: {'name': 'meghanath', 'age': 24, 'grade': 'B'},
    103: {'name': 'pavan', 'age': 25, 'grade': 'A'}
}

if student_id in student_records:
    print(student_records[student_id])
else:
    print(f"Invalid Student Id {student_id}")
