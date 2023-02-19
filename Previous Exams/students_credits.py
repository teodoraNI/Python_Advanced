def students_credits(*args):
    results = {}
    total_credits = 0
    for arg in args:
        course, credits, max_points, diyan_points = arg.split('-')
        results[course] = int(diyan_points) / int(max_points) * int(credits)
        total_credits += int(diyan_points) / int(max_points) * int(credits)
    final = '\n'.join(str(f'{key} - {value:.1f}') for key, value in sorted(results.items(), key=lambda x:-x[1]))

    if total_credits >= 240:
        return f"Diyan gets a diploma with {total_credits:.1f} credits.\n"  + final
    else:
        return f"Diyan needs {(240-total_credits):.1f} credits more for a diploma.\n" + final


print(students_credits("Computer Science-12-300-250","Basic Algebra-15-400-200","Algorithms-25-500-490"))
print(students_credits("Discrete Maths-40-500-450","AI Development-20-400-400","Algorithms Advanced-50-700-630","Python Development-15-200-200","JavaScript Development-12-500-480","C++ Development-30-500-405","Game Engine Development-70-100-70","Mobile Development-25-250-225","QA-20-300-300",))