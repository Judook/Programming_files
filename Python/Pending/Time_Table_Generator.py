import random

teachers = []
subjects = []
teach_sub = []
classes = []
no_of_periods = None
no_of_days = None
no_of_teachers = None
no_of_subjects = None
no_of_classes = None

print('''\n████████╗██╗███╗░░░███╗███████╗░░░░░░████████╗░█████╗░██████╗░██╗░░░░░███████╗
╚══██╔══╝██║████╗░████║██╔════╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
░░░██║░░░██║██╔████╔██║█████╗░░█████╗░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░
░░░██║░░░██║██║╚██╔╝██║██╔══╝░░╚════╝░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░
░░░██║░░░██║██║░╚═╝░██║███████╗░░░░░░░░░██║░░░██║░░██║██████╦╝███████╗███████
      
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n''')

# Getting teachers
no_of_teachers = int(input("Enter the number of teachers you have : "))
print("\nEnter the names of the teachers : ")
for i in range(0, no_of_teachers) :
    print("Teacher ", str(i+1), " : ", end="")
    j = str(input())
    teachers.append(j)

# Getting subjects
no_of_subjects = int(input("\nEnter the number of subjects you have : "))
print("\nEnter the subjects : ")
for i in range(0, no_of_subjects) :
    print("Subject ", str(i+1), " : ", end="")
    j = str(input())
    subjects.append(j)

# Getting classes
no_of_classes = int(input("\nEnter the number of classes you have : "))
print("\nEnter the classes : ")
for i in range(0, no_of_classes) :
    print("Class ", str(i+1), " : ", end="")
    j = str(input())
    classes.append(j)

# Appointing teachers to subjects
print("\nThis is the list of subjects :")
for i in range(0, len(subjects)) :
    print(str(i), ".", subjects[i])
print("\nAppoint your teachers subjects by typing the subject numbers beside their names.")
print("If any teacher has more than one subject, then the numbers should be seperated by commas.")
print("IMPORTANT! : DO NOT HAVE SPACES BETWEEN COMMAS.")
print("Correct way : 1,2,3,4,5")
print("Wrong way : 1, 2, 3 , 4, 5")
for i in range(0, no_of_teachers) :
    print(teachers[i], end=" : ")
    teach_sub.append(str(input()))

no_of_periods = int(input("Enter the number of periods in a day : "))
no_of_days =  int(input("Enter the nuber of days you have in a working week : "))
