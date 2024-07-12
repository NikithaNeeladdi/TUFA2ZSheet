
def practiceInputOutPuts():
    # test input :
    # input('prompt')
    # # Taking input from user:
    # user_input = input("Enter a number: ")
    # print("You entered:", user_input)
    # print("The type of input:",type(user_input))
    
    # #type conversion:
    # user_input = input("Enter a number: ")
    # num = int(user_input)
    # print('You entered: ',num)
    # print("Type of input:",type(num))
    
    # #Taking List elements as input:
    # n = int(input("Enter the number of elements: "))
    # list = []
    # for i in range(n):
    #     elem = int(input(f"Enter Element {i+1}: "))
    #     list.append(elem)
    # print("List:",list) 
    
    #using map and list functions:
    # user_input = input("Enter the input seperated by space: ")
    # my_list = list(map(int,user_input.split()))  
    # print("list: ",my_list) 
    
    #practice outputs
    # print(object(s), sep=' ', end='\n', file=file, flush=flush)
    
    #Default Seperator and End:
    # print("Hello","World")
    # print("Python is awesome!")
    
    #Custom seperator and end
    # print("Hello","World",sep=' & ')
    # print("Python is awesome",end = " !!!")
    
    #Python Import - brings modules into python interpreter
    # Modules are simply files with ".py " extension containing code
    
    #practoce-1:
    # import math
    # print("factorial of 5 ", math.factorial(5), sep =" is :")
    # print("GCD of 24 and 18 ", math.gcd(24,18),sep = ' is ',end = " Yaaay !!!")
    
    #practice-2:
    # from math import factorial ,gcd
    # print("Factorial of 4 is :",factorial(4))
    # print("GCD of 24 and 18 is : ",gcd(24,18))
    
    #Pratice-3:
    # import math as m
    # print("Factorial of 4 is:" ,m.factorial(5) )
    # print("GCD of 24 and 18 :" , m.gcd(24,18))
    
    #Write output to a file:
    # with open('output.txt' ,'w') as f :
    #     print("This output will be written into the file",file = f) 
    
    #testing the flush of the print statements:
    import time
    print("This statenet will be flushed ", flush = True)
    time.sleep(2)
    print("This statement will be buffered")
practiceInputOutPuts()