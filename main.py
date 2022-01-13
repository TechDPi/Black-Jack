############### Blackjack Project #####################

import random
import os 
from art import logo

def clear():
    os.system('cls') #on Windows System

def deal_card():
  """Return a random card from the list of cards
  11 = ace
  10 = face cards (jacks, queens, kings)
  """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(user_score, computer_score):
    """Compare the scores
    0 = black jack (the sum of black jack is 21)"""
    if user_score > 21 and computer_score > 21:
        return "Computer win 🎲"

    if user_score == computer_score:
        return "It is a Draw 🎲"
    elif computer_score == 0:
        return "Computer win 🥺"
    elif user_score == 0:
        return "You Win ♥️"
    elif computer_score > 21:
        return "You Win ♥️"
    elif user_score > 21:
        return "Computer win 🥺"
    elif computer_score > user_score:
        return "Computer win 🥺"
    elif user_score > computer_score:
        return "You Win ♥️"

def calculate_score(list_of_cards):
  sum(list_of_cards)
  # In my logic the Blackjack value is 0
  if sum(list_of_cards) == 21:
    return 0
  for card in list_of_cards:
    if card == 11 and sum(list_of_cards) > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
  return sum(list_of_cards)


def black_jack():
  print(logo)
  user_cards = []
  computer_cards = []
  game_continue = True


#Using a for loop for genearte 2 random card for the player and the computer
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  print(f"  This is your 2 cards : {user_cards} 🍀 \n")
  print(f"  Computer's first card is : {computer_cards[0]} 🖥️ \n")

#Infite loop for continue the game till a condition is met for stop it
  while game_continue:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your total score at the moment is {user_score} ✔️")
    #print(computer_score) prints statment for check if the program works
    #print(computer_cards)
    if computer_score == 0 or user_score == 0 or user_score > 21:
      game_continue = False
    else:
      draw_again = input("Do you want to draw another card? type yes or no: \n")
      if draw_again == "yes":
        user_cards.append(deal_card())
        print(f"You just draw this card: {user_cards[-1]} ✔️ and this is your hand now {user_cards} ✔️")
      else:
        game_continue = False

    # the computer turn
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print(f"  Your final score is {user_score} 🏁 ")
  print(f"  The Computer final score is {computer_score} 🏁 ")
  print(compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  black_jack()
