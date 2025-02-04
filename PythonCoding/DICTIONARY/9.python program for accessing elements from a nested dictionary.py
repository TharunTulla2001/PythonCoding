my_dict = {
    "student": {
        "name": "Tharun",
        "age": 23,
        "courses": {
            "math": "A",
            "science": "B",
            "english": "A"
        }
    },
    "teacher": {
        "name": "Mr. pavan",
        "age": 45,
        "subjects": ["math", "science", "history"]
    }
}

student_course=my_dict["student"]
student_teacher=my_dict["teacher"]
print(student_course["courses"])
print(student_teacher["name"])