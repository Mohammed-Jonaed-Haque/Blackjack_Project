import random
import art

def deal_cards():   #<--- plays the cards randomly
    """It returns a random card from the deck to the players"""
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_list)
    return card


def calculate_score(cards_list):
    """Calculates the total score of the cards, and also changes the score on the ACE card accordingly """
    score = sum(cards_list)
    if score==21 and len(cards_list)==2:
        return 0  #<--- here zero represents a black jack

    if 11 in cards_list and score>21:  #<--- changing the score of ACE (which is, 11 , here accordingly
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)
    return score


def compare(u_score, c_score):
    """Compares the user's score and the computer's score"""
    if u_score==c_score:
        return "its a draw"
    elif c_score==0:
        return "You LOSE, opponent has a BLACKJACK"
    elif u_score==0:
        return "You WIN, you have a BLACKJACK"
    elif u_score>21:
        return "You LOSE, your score is over 21"
    elif c_score>21:
        return "You WIN, computer score is over 21"
    elif c_score>u_score:
        return "You LOSE, computer score is more than your score"
    else:
        return "You WIN, your score is more than computer score"

def start_game():
    """all the main functionalities of the game"""
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_the_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_the_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards in hand are: {user_cards},  making your score {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score > 21:
            is_the_game_over=True
            print ("game over")
        else:
            user_choice = input("do you wish to draw another card, type 'y' for 'YES' or 'n' for 'NO'")
            if user_choice=='y':
                user_cards.append(deal_cards())
            else:
                is_the_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"Your final cards in hand are: {user_cards},  making your score: {user_score}")
    print(f"Computer's final cards in hand are: {computer_cards},  making its score: {computer_score}")
    print(compare(user_score, computer_score))


while  input("type 'y' to start a new game, or type 'n' to end game")=='y':
    print("\n"*100)
    start_game()
