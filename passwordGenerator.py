import minimodules
import secrets
#First, we need to make a random symbol
def randomSymb(isSC):
    LettersNormal = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0".split()
    LettersSC = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) - _ = + ` ~ , . < > / ? ; : ' [ ] { } ".split()
    if isSC:
        return secrets.choice(LettersSC)
    else:
        return secrets.choice(LettersNormal)
#then we gonna need to ask user how long do he wants the  password
def InputSys():
    resp= input("How long the password should be?")    
    while True:
        
        if  minimodules.IntCheck(resp):
            if int(resp) >= 1:
                break
        else:
            print("Please provide a number!")
            resp= input("How long the password should be?") 
    lengthofpassword= int(resp)
    isSCT = False
    resp = input("""Do you want Special Characters($,#, @...)?
If yes, DONT type anything here. Even spaces. 
If no, then type something for example ' ' would work, 
and 'apple' would work too.""")
    if resp == "":
        isSCT = True
    else:
        isSCT = False
    print(f"""Your password is:
{passwordGenFunc(lengthofpassword,isSCT)}
Dont forget to save as text on your computer!
This password is fully random, and i dont think you can remember,
For example '#8lf:>$=u;mk51=@$%&'.
""")
#then we gonna generate our password!
def passwordGenFunc(lengthofpass,  isSCS):
    password = ""
    for i in range(lengthofpass):
        password += randomSymb(isSCS)
    return password
#Main Cycle!
def Main():
    while True:
        InputSys()
        resp = input("""Do you to generate another password?
If yes, DONT type anything here. Even spaces. 
If no, then type something for example ' ' would work, 
and 'apple' would work too.""")
        if resp == "":
            break
minimodules.InitializationOfApp("Password Generator", "1.0.2")
Main()