
from ast import For

# print("\t\tMark Sheet")
# print("Enter Marks")
# name = input("Student Name: ")
# sub1 = int(input("English: "))
# sub2 = int(input("Urdu: "))
# sub3 = int(input("Islamiat: "))
# sub4 = int(input("Computer: "))
# sub5 = int(input("Physics: "))
# avg = int((sub1 + sub2 + sub3 + sub4 + sub5) / 5)
# if (avg >= 90):
#     print("Grade: A")
# elif(avg >= 80 and avg < 90):
#     print("Grade: B")
# elif(avg >= 70 and avg < 80):
#     print("Grade: C")
# elif(avg >= 60 and avg < 70):
#     print("Grade: D")
# else:
#     print("Grade: F")




num = int(input("Enter number: "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
