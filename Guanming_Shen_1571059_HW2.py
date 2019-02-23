rightg = ['A' ,'B' , 'C' , 'D' ,'F']
rightc = ['2','3','5']

total_credit = 0
total_grade = 0

while True:
    
    grade = input("Enter grade (A, B, C, D, or F):")
    while grade not in rightg:
        print("Invalid grade! Try again!")
        grade = input("Enter grade (A, B, C, D, or F):")
    
    credit = input("Enter credit count (2, 3, or 5):")
    while credit not in rightc:
        print("Invalid credit count! Try again!")
        credit = input("Enter credit count (2, 3, or 5):")
    total_credit += int(credit)
    
    if grade == 'A':
        num = 4
    elif grade == 'B':
        num = 3
    elif grade == 'C':
        num = 2
    elif grade == 'D':
        num = 1
    elif grade == 'F':
        num = 0
        
    total_grade += num*(int(credit))
    
    user = input("If you are done, enter DONE; otherwise, just press enter: ")
    if user == "DONE":
        print("Average GPA is: ","%.2f" % (total_grade/total_credit))
        break