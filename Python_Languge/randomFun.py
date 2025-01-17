import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number :
#         guess = int(input(f"Guess number between 1 to {x} : "))
#         if guess < random_number:
#             print("Sorry , guessed number is to low")
#         elif guess > random_number:
#             print("Sorry , guessed number is to high")
#     print(f"Congrats, you gussed correct number that is {random_number}")

# guess(10)







# def computerGuess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         computer_guess = random.randint(low, high)
#         feedback = input(f"Is {computer_guess} is to high (H) or to low (L) or correct (C) : ").lower()
#         if feedback == 'h':
#             high = computer_guess-1
#         elif feedback == 'l':
#             low = computer_guess+1
    
#     print(f"yay, congrat computer guessed correct number that is {computer_guess}")


# computerGuess(10000)






def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissores : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Win !'

    return 'You Lost !'



def is_win(player, opponent):
    if(player =='r' and opponent =='s' or player == 's' and opponent == 'p' and player == 'p' and opponent == 'r'):
        return True

print(play())
