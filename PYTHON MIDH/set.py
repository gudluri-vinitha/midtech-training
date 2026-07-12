numbers={1,2,3,4,5,6,3,2,2,1}
print (numbers)
courses={"java","python","java"}
print(courses)
unique_courses=set(courses)
print("unique_courses:" ,unique_courses)
#set task
students = {"Vinitha", "Anu", "Rahul"}

print("Original Set:", students)

students.add("Kiran")
print("After Adding:", students)

students.remove("Anu")
print("After Removing:", students)
print("Total Students:", len(students))
students.update({"Kiran", "Ravi"})
print("After Update:", students)

students.discard("Anu")
print("After Discard:", students)

removed = students.pop()
print("Removed Student:", removed)
print("After Pop:", students)

copy_students = students.copy()
print("Copied Set:", copy_students)

new_students = {"Ravi", "Sita", "Ram"}

print("Union:", students.union(new_students))
print("Intersection:", students.intersection(new_students))
print("Difference:", students.difference(new_students))

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print("Is Subset:", set1.issubset(set2))
print("Is Superset:", set2.issuperset(set1))

students.clear()
print("After Clear:", students)
