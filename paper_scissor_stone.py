import random
def game(choice1,ran):

    match(choice1):
        case 1:
            print("You choose Rock")
        case 2:
                print("You chose Paper ")
        case 3:
            print("You chose Scissor")

    print("BOT= ",ran)
    match(ran):
        case 1:
            print("i chose Rock")
        case 2:
            print("i chose Paper")
        case 3:
            print("i chose Scissor")
    print("The result is==")
    if choice1==1 and ran==3:
        print("you win")
    elif choice1==2 and ran==1:
        print("you win")
    elif choice1==3 and ran==2:
        print("you win")
    elif choice1==1 and ran==1:
        print("Match Draw")
    elif choice1==2 and ran==2:
        print("match Draw")
    elif choice1==3 and ran==3:
        print("match Draw")
    else:
        print("i win")

bot=[1,2,3]
try:
    print("Enter 1 for rock,2 for paper,3 for scissor")
    choice1=int(input("enter your choice = "))
    ran=int(random.choice(bot))
    game(choice1,ran)
except:
    print("Well played")
finally:
    print("--------- -----------------------------keep playing----------------------")
    
 
