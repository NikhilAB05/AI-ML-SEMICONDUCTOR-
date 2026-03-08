#CHIP _TESTING

score = float(input("Enter the Score: "))

if score>=80:
              print("Excellent Quality Chip")
elif score>=60:
              print("Good Quality Chip")
elif score>=40:
              print("Need to be Retest")
else:
              print("Rejected")


'''Output
Enter the Score: 95
Excellent Quality Chip
Condition 2 — Score 60 to 79
Enter the Score: 65
Good Quality Chip
Condition 3 — Score 40 to 59
Enter the Score: 45
Need to be Retest
Condition 4 — Score below 40
Enter the Score: 25
Rejected
'''
