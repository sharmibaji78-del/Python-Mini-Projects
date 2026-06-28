#Student Marks Calculator
Student_name=input("Enter Student Name:")
Telugu=float(input("Enter Telugu Marks:"))
Hindi=float(input("Enter Hindi Marks:"))
English=float(input("Enter English Marks:"))
Total_Marks=Telugu+Hindi+English
Total_sub=3
Max_marks=300
Percentage=(Total_Marks/Max_marks)*100
print("Student name:",Student_name)
print(f"Telugu Marks:{Telugu}")
print(f"Hindi Marks:{Hindi}")
print(f"English Marks:{English}")
print(f"Total Marks:{Total_Marks}")
print(f"Percentage of the Student:{Percentage:.2f}%")
if Telugu<35 or Hindi<35 or English<35:
    print("Result:Fail")
else:
    print("Result:Pass")
if Percentage >=80:
    print("Grade:A")
    print("Excellent")
elif Percentage>=70:
    print("Grade:B")
    print("Very Good")
elif Percentage>=50:
    print("Grade:C")
    print("Average")
elif Percentage>=40:
    print("Grade:D")
    print("Need improvement")
else:
    print("Work harder")

