''' DICE PIG GAME '''

import random

#constants
winning_score = 50
min_players = 2
max_players = 4

# Number of players playing
def player_count():
    while True:
        try:
            players = int(input("Enter number of players (2-4): "))
            if not min_players <= players <= max_players:
                raise ValueError
            break

        except ValueError:
            print(f"Invalid Input! The number should be between {min_players} and {max_players}")
    return players
    

# function to roll a dice and get a number between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value,max_value)
    return value

# function to check winner
def check_winner(player_scores, player_index):
    if player_scores[player_index] > winning_score:
        return True
    else:
        return False
    
# funtion to start the game --> result is winner
def main():
    winner = False
    players = player_count()
    player_scores = [0 for i in range(players)]

    while not winner:
        for i in range(players):
            while True:
                player_res = input(f"Player {i+1}, Would you like to roll? (y/n): ")
                if player_res.lower() != 'y':
                    break
                value = roll()
                if value==1:
                    print("You got 1!. No more try :(")
                    break
                player_scores[i] += value
                if check_winner(player_scores,i):
                    winner = True
                    break
                print(f"You rolled: {value}. Your current score: {player_scores[i]}")
            
            if winner:
                break
    
    winning_player = player_scores.index(max(player_scores))
    print(f"Hurray! We have a winner! : Player{winning_player + 1} -- Your Score : {player_scores[winning_player]}")


if __name__ == "__main__":
    main()  

