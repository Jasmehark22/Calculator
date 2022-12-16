print('Welcome')
opt = int(input('What do you want to do?\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n'))
n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
if opt == 1:
    result = n1+n2
    print('Sum of',n1,'and',n2,'is',result)
elif opt == 2: 
    result = n1-n2
    print('Difference of',n1,'and',n2,'is',result)   
elif opt == 3:
    result = n1/n2
    print('Quotient of',n1,'and',n2,'is',result)   
elif opt == 4:
    result = n1*n2
    print('Product of',n1,'and',n2,'is',result)
print('Thank You!')
