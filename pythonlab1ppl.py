print('''This is the grade calculation system.
      You have to give input of marks if you wish to calculate grade and give exit to stop the program
      ''')
while 1:
    marks = input('enter the marks :')
    if marks.isnumeric():
        m=int(marks)
        if m<40:
             print("F")
        elif m>=40 and m<=59:
             print("D")
        elif m>=60 and m<=74:
             print("C")  
        elif m>=75 and m<=89:
             print("B")
        elif m>=90 and m<=100:
             print("A")
        else:
             print("Invalid input")
    elif marks =='exit':
        break 
    else:
        print('Invalid input')