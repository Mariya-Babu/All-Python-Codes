# Project_4 
name = input("Enter your name : ")
print(name,"Welcome to my game ")
print("Let's Start Our Game ")
chooice = input("Your are at the end of the road you have to choose either left/right Q for quit ").lower()
if chooice == 'q':
    quit()
if(chooice == 'left'):
    chooice = input('There is a river you have to swim or cross thorugh boat (swim/cross)').lower()
    if (chooice == 'swim'):
        print('There is crocodial You lost the Game!')
    elif(chooice == 'cross'):
        chooice = input('You want to continuee on boat or you will go through road (boat/road)').lower()
        if (chooice == 'boat'):
            print('Fuel was completed you lost the game!')
        elif(chooice == 'road'):
            chooice = input('There is hill you want to climb the hill or go around (climb/go_around)').lower()
            if (chooice == 'climb'):
                print('Hey  You got the gold You Won the game!')
            elif(chooice == 'go_around'):
                print("It's too far you lost the game!")
            else:
                print('Invalid Entry....')
        else:
            print('Invalid Entry....')
    else:
        print('Invalid Entry....')
elif(chooice == 'right'):
    chooice = input('There is a Wall you go left of back to the previous road (left/back) ').lower()
    if(chooice == 'left'):
        chooice = input('There is no path to continue.... you lost').lower()
    elif (chooice == 'back'):
        choice = input('There is a dragon you have to run or walk (run/walk)').lower()
        if(chooice == 'run'):
            chooice = input('There is cave you go into the cave of not (go/not)').lower()
            if(chooice == 'go'):
                print('Hey you got the gold You Won the game!')
            elif(chooice == 'not'):
                print('Hey Wrong Chooice you lost the game')
            else:
                print('Invalid Entry')
        elif(chooice == 'walk'):
            print('Dragon Attacked you lost the game!')
        else:
            print('Invalid Entry....')
    else:
        print('Invalid Entry....')
else:
    print('Invalid Entry....')
