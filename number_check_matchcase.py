n=int(input("Enter any number="))
g=int(input("1.positive or negative\n2.odd or even\nEnter your choice="))
match g:
    case 1:
        if a>0:
            print("number is positive")
        else:
            print("number is negative")    
    case 2:
        if n%2==0:
            print("number is even")        
        else:
            print("number is odd")    
            