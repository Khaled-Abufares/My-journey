#~~~~~بسم الله الرحمن الرحيم~~~~#
import numpy as np
np.random.seed(42)  
grades = np.random.randint(50, 101, (10,5)) 
student_names = [f"Student {i+1}" for i in range(grades.shape[0])]
print("Grades:\n", grades)
print("~" * 50)
student_mean = grades.mean(axis=1)
for i, mean in enumerate(student_mean):
    print(f"{student_names[i]} average: {mean:.2f}")
print("~" * 50)
subject_mean = grades.mean(axis=0)
print(f"Average per subject: {subject_mean}")
print("~" * 50)
pass_fail = grades >= 60
print(f"Pass/Fail matrix:\n{pass_fail}")
print("~" * 50)
subject_std = grades.std(axis=0)
print(f"Std per subject: {subject_std}")
print("~" * 50)
successful_students = np.all(pass_fail, axis=1)
print(f"Successful students: {successful_students}")
print("~" * 50)
success_rate = successful_students.mean() * 100
print(f"Success rate: {success_rate:.1f}%")
print("~" * 50)
valid_means = student_mean[successful_students]
if valid_means.size > 0:  
    highest_score = valid_means.max()
    top_students = np.where(student_mean == highest_score)[0]
    print("Top students:")
    for i in top_students:
        print(f" - {student_names[i]} with average (only successful students) {student_mean[i]:.2f}")
else:
    print("No student passed all subjects.")
