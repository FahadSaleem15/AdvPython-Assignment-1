import csv

avg_steps = open('steps.csv','r')

file_reader = csv.reader(avg_steps)

next(file_reader)

steps_month_1 = []
steps_month_2 = []
steps_month_3 = []
steps_month_4 = []
steps_month_5 = []
steps_month_6 = []
steps_month_7 = []
steps_month_8 = []
steps_month_9 = []
steps_month_10 = []
steps_month_11 = []
steps_month_12 = []

for rec in file_reader:
    month = int(rec[0])
    steps = int(rec[1])

    if month == 1:
        steps_month_1.append(steps)
    elif month == 2:
        steps_month_2.append(steps)
    elif month == 3:
        steps_month_3.append(steps)
    elif month == 4:
        steps_month_4.append(steps)
    elif month == 5:
        steps_month_5.append(steps)
    elif month == 6:
        steps_month_6.append(steps)
    elif month == 7:
        steps_month_7.append(steps)
    elif month == 8:
        steps_month_8.append(steps)
    elif month == 9:
        steps_month_9.append(steps)
    elif month == 10:
        steps_month_10.append(steps)
    elif month == 11:
        steps_month_11.append(steps)
    elif month == 12:
         steps_month_12.append(steps)

avg_month_1 = sum(steps_month_1) / len(steps_month_1) 
avg_month_2 = sum(steps_month_2) / len(steps_month_2) 
avg_month_3 = sum(steps_month_3) / len(steps_month_3)
avg_month_4 = sum(steps_month_4) / len(steps_month_4)
avg_month_5 = sum(steps_month_5) / len(steps_month_5)
avg_month_6 = sum(steps_month_6) / len(steps_month_6)
avg_month_7 = sum(steps_month_7) / len(steps_month_7)
avg_month_8 = sum(steps_month_8) / len(steps_month_8)
avg_month_9 = sum(steps_month_9) / len(steps_month_9)
avg_month_10 = sum(steps_month_10) / len(steps_month_10)
avg_month_11 = sum(steps_month_11) / len(steps_month_11)
avg_month_12 = sum(steps_month_12) / len(steps_month_12)

print(f'January - {avg_month_1}')
print(f'February - {avg_month_2}')
print(f'March - {avg_month_3}')
print(f'April - {avg_month_4}')
print(f'May - {avg_month_5}')
print(f'June - {avg_month_6}')
print(f'July - {avg_month_7}')
print(f'August - {avg_month_8}')
print(f'September - {avg_month_9}')
print(f'October - {avg_month_10}')
print(f'November - {avg_month_11}')
print(f'December - {avg_month_12}')




       


    

