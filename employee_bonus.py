import csv


employee_bonus = open('employee_data.csv','r')

file_reader = csv.reader(employee_bonus)

next(file_reader)

for rec in file_reader:
    Bonus = float(rec[3])*float(rec[7])
    Total_pay = float(rec[3]) + Bonus
    print(f"Name: {rec[1]}")
    print(f"Salary: $ {float(rec[3])}")
    print(f"Bonus: $ {Bonus}")
    print(f"Pay: $ {Total_pay}")


    input()


