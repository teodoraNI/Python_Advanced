students = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in students:
        students[name]= []
    students[name].append(float(grade))
for student, grades in students.items():
    average_grade = sum(grades)/len(grades)
    convert_grades = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{student} -> {convert_grades} (avg: {average_grade:.2f})")


