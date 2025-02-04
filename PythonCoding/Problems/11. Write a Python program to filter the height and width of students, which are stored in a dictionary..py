
students = {"sai": {"height": 160, "width": 50},"mani": {"height": 170, "width": 55},"Chintu": {"height": 150, "width": 45},
    "tom": {"height": 180, "width": 60},"seenu": {"height": 165, "width": 52}}

filtered_students = {}


for name, details in students.items():
    if details["height"] > 160 and details["width"] > 50:
        filtered_students[name] = details


print("Filtered Students (Height > 160 and Width > 50):")
print(filtered_students)
