# Project_1 Quiz (Question and answers) 
print("Welcome to my game!")
playing = input("Do you want to play a game? yes :")
score = 0
if (playing.lower()!='yes'):
    quit()
else:
    answer = input("Who is our Prime Minister? ")
    if(answer.lower()=='narendra modi'.lower()):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    answer = input("What is our country name? ")
    if(answer.lower()=='India'.lower()):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("What is our Country Capital? ")
    if(answer.lower()=='Delhi'.lower()):
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    answer = input('What is AP people native language? ')
    if(answer.lower()=='telugu'.lower()):
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    answer = input('what is CPU Standers for? ')
    if(answer.lower()=='central processing unit'.lower()):
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    print('You got the score of ',score)
    print('You have got ',(score/5)*100,"%.")