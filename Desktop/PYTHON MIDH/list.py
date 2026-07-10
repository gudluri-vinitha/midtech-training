student_marks=[3,5,4]
total=sum(student_marks)
average=total/len(student_marks)
print("Average marks:",average)
student_marks.append(2)
student_marks.extend([8, 9])
student_marks.insert(0, 1)
student_marks.remove(5)
student_marks.pop(2)

print("Index of 8:", student_marks.index(8))
print("Count of 2:", student_marks.count(2))

student_marks.sort()
student_marks.reverse()

new_list = student_marks.copy()

print("Student Marks:", student_marks)
print("Copied List:", new_list)


print(student_marks)