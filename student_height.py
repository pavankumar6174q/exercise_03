student_height = input("enter student height in cm with space ").split()
for n in range(0, len(student_height)):
    student_height[n]=int(student_height[n])

print(student_height)
# total = sum(student_height)
# count= len(student_height)
# avg=total/count
# print(round(avg))
total_height =0
for i in student_height:
    total_height += i
total_students = 0
for std in student_height:
    total_students +=1
# print(total_students)
# print(total_height)
avg = total_height/total_students
print(round(avg))