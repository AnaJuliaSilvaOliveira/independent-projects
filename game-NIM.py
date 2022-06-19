'''
This is a game that consists on a player playing against a computer in turns and entering 
numbers that are lower or equal to a chosen limit for the input. these numbers subtracts the total 
amount of pieces and the goal is to lower the amount of pieces to 0. the computer's supposed to win
every time.
'''

def inputs() -> int:
    ''' Requests the necessary variables to start the game from the player. 
    '''
    inputs.num_pieces = int(input("How many pieces would you like the match to start with? "))
    while inputs.num_pieces <=1:
        inputs.num_pieces = int(input("The number of available pieces can't be only one. Choose a different amount: "))
    inputs.max_removal = int(input("How many pieces would you like to be able to remove each turn? "))  # maximum amount of pieces that can be removed each turn if inputs.current_amount >= inputs.max_removal
    while inputs.max_removal >= inputs.num_pieces:
        inputs.max_removal = int(input("The amount of removable pieces on each turn can't be equal to ou more then the amount of pieces available. Choose a different amount of pieces to remove: "))  # maximum amount of pieces that can be removed each turn if inputs.current_amount >= inputs.max_removal
    inputs.current_amount = inputs.num_pieces

def championship():
    championship.round = 1
    championship.num_wins_computer, championship.num_wins_user = 0, 0
    championship.champ = input("Would you like to play a championship? If so you'll play three times against the computer and the winner of at least two rounds wins! (yes or no): ")
    if championship.champ.lower().strip() in ('yes','y','ye', 'ys'):
        championship.num_rounds = 3
    else:
        championship.num_rounds = 1

def start() -> int:
    ''' checks if inputs.num_pieces is multiple of (inputs.max_removal+1) and calls either computer_chooses_move()
    or user_chooses_move() to start the match. 
    '''
    if inputs.num_pieces % (inputs.max_removal + 1) == 0:
        user_chooses_move()
    else:
        computer_chooses_move()

def match() -> None:
    ''' continues the match after the first round. 
    '''
    if inputs.num_pieces % (inputs.max_removal + 1) == 0:
        while inputs.current_amount > 0:
            computer_chooses_move()
            user_chooses_move()
    else:
        while inputs.current_amount > 0:
            user_chooses_move()
            computer_chooses_move()
    championship.round += 1

def user_chooses_move() -> int:
    ''' Requests the users' choice on how many pieces to remove and only accepts appropriate numbers. 
    '''
    if inputs.current_amount > 0:
        print('Your turn!!')
        user_move = int(input('Inform the amount of pieces you want to remove: '))
        while user_move > inputs.max_removal or user_move > inputs.current_amount or user_move <= 0:
            if user_move > inputs.max_removal:
                user_move = int(input("The amount of removed pieces can't be more than the number of removable pieces per turn. Choose a different amount: "))
            elif user_move > inputs.current_amount: 
                user_move = int(input("The amount of removed pieces can't be more than the the amount of left over pieces. Choose a different amount: "))
            elif user_move <= 0:
                user_move = int(input("The removal needs to be of at least 1 piece! Choose again: "))
        inputs.current_amount -= user_move
        
        print(f'There are {inputs.current_amount} left over pieces! \n')
        if inputs.current_amount == 0 and championship.round <= 2:
            print("You won!")
            championship.num_wins_user += 1
        elif inputs.current_amount == 0 and championship.round == 3:
            print(f"You won the championship with {championship.num_wins_user + 1} wins! ")
        return inputs.current_amount

def computer_chooses_move() -> int:
    ''' chooses the computer's move. If it is not possible to remove a amount that results in a number 
    multiple of (inputs.max_removal + 1), it removes inputs.max_removal. 
    '''
    if inputs.current_amount > 0:
        print("Computer's turn!!")
        if (inputs.current_amount - inputs.max_removal) >= 0:
                possible_move = inputs.max_removal
        for computer_move in range(1, inputs.max_removal+1):
            if (((inputs.current_amount - computer_move) % (inputs.max_removal + 1) == 0) and 
            (inputs.current_amount - computer_move >= 0)):
                possible_move = computer_move
            
        inputs.current_amount -= possible_move
        
        print(f"The computer removes {possible_move}. There are {inputs.current_amount} left over pieces! \n")
        if inputs.current_amount == 0 and championship.round <= 2:
            print("Computer won!")
            championship.num_wins_computer += 1
        elif inputs.current_amount == 0 and championship.round == 3:
            print(f"Computer wins the championship with {championship.num_wins_computer + 1} wins! ")
        return inputs.current_amount


if __name__ == '__main__':
    championship()
    for round in range(championship.num_rounds):
        if championship.champ in ('yes','y','ye', 'ys'):
            print(f" ROUND {round + 1}")
        inputs()
        start()  
        match()

