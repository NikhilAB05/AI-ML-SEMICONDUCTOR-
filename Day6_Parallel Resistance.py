#Parallel Resistance Check
R1 = float(input("Enter Resistance R1: "))
R2 = float(input("Enter Resistance R2: "))
R3 = float(input("Enter Resistance R3: "))

R= (1/((1/R1)+(1/R2)+(1/R3)))
print("Total Parallel Resistance: ", R)



'''Output

Enter Resistance R1: 10
Enter Resistance R2: 20
Enter Resistance R3: 30
Total Parallel Resistance:  5.454545454545454

=== Code Execution Successful ===
'''
