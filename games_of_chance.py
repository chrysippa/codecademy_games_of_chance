import random

money = 100

punc_and_space = '''!()[]{};:'"\, <>./?@#$%^&*_~'''

def clean_text(call):
    if type(call) == str:
        for i in call:
            if i in punc_and_space:
                call = call.replace(i, "")
    if type(call) == str:
        call = call.capitalize()
    return call

def clean_text_roulette(call):
    if call == "00":
        call = "-1"
    try:
        call = int(call)
        return call
    except ValueError:
        return call

# a coin is flipped. Bet on whether it is "Heads" or "Tails".
def coin_flip(call, bet):
    global money 
    if bet > money: 
        return "Sorry, you can't bet more money than you have."
    if bet <= 0:
        return "Sorry, your bet must be greater than 0."
    call = clean_text(call)
    if call != "Heads" and call != "Tails":
        return "Sorry, your call must be Heads or Tails."
    print("You bet that the coin flip would be " + call + ".")
    result = random.randint(0, 1)
    if result == 0:
        print("The coin flip is heads.")
        if call == "Heads":
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
    else:
        print("The coin flip is tails.")
        if call == "Heads":
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."

# 2 die are rolled and their values added together. Bet on whether the sum is "Even" or "Odd".
def cho_han(call, bet):
    global money
    if bet > money: 
        return "Sorry, you can't bet more money than you have."
    if bet <= 0:
        return "Sorry, your bet must be greater than 0."
    call = clean_text(call)
    if call != "Even" and call != "Odd":
        return "Sorry, your call must be Even or Odd."
    print("You bet that the Cho-Han total would be " + call + ".")
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    sum = roll1 + roll2
    print("The dice rolled " + str(roll1) + " and " + str(roll2) + " for a total of " + str(sum) + ".")
    if sum % 2 == 0:
        print("The Cho-Han total is even.")
        if call == "Even":
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
    else:
        print("The Cho-Han total is odd.")
        if call == "Even":
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."

# 2 players draw cards from a deck. Bet an amount of money.
# you'll win your bet if your card is higher, lose it if your card is lower.
def draw_cards(bet):
    global money
    if bet > money: 
        return "Sorry, you can't bet more money than you have."
    if bet <= 0:
        return "Sorry, your bet must be greater than 0."
    print("In this card-drawing game, face cards have the following numeric values: ace = 1, jack = 11, queen = 12, king = 13. You bet on whether your card is higher.")
    deck = list(range(1, 14))
    for i in range(2):
        deck[0:0] = deck[:]
    real_player = deck[random.randint(0, len(deck) - 1)]
    deck.remove(real_player)
    sim_player = deck[random.randint(0, len(deck) - 1)]
    print("You drew " + str(real_player) + " and the other player drew " + str(sim_player) + ".")
    if real_player > sim_player:
        money += bet
        return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."
    elif real_player < sim_player:
        money -= bet
        return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points." 
    else:
        return "It's a tie! You don't gain or lose any money."

# player spins an American double-zero roulette wheel. 
# Bet on whether the wheel lands on an "Even" number, "Odd" number, on "00", 
# or on any integer "0" - "36" inclusive. You win 1x your bet if you correctly guessed "Even" or "Odd", 
# or win 35x your bet if you correctly guessed the specific number.
def roulette(call, bet):
    global money
    if bet > money: 
        return "Sorry, you can't bet more money than you have."
    if bet <= 0:
        return "Sorry, your bet must be greater than 0."
    if type(call) != str:
        return "Sorry, please enter your call as a string."
    call = clean_text(call)
    call = clean_text_roulette(call)
    if type(call) == str:
        if call != "Even" and call != "Odd":
            return "Sorry, your call must be Even, Odd, 00, or an integer between 0-36."
    if type(call) == int:
        if call < -1 or call > 36:
            return "Sorry, your call must be Even, Odd, 00, or an integer between 0-36."
    if call == -1:
        call = "00"
    print("You bet that the roulette spin would be " + str(call) + ".")
    spin = random.randint(-1, 36)
    if spin == -1:
        spin = "00"
    print("The roulette wheel landed on " + str(spin) + ".")
    if call == "Even":
        if spin == "00" or spin == 0:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        elif spin % 2 != 0:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."
    elif call == "Odd":
        if spin == "00" or spin == 0:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        elif spin % 2 == 0:
            money -= bet
            return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."
        else:
            money += bet
            return "You won! You gained " + str(bet) + " points for a current total of " + str(money) + " points."
    elif call == spin:
        money = money + bet * 35
        return "You won! You gained " + str(bet * 35) + " points for a current total of " + str(money) + " points."
    else:
        money -= bet
        return "You lost. You lost " + str(bet) + " points for a current total of " + str(money) + " points."

print(coin_flip("heads!", 2))
print(cho_han("Odd", 3))
print(draw_cards(4))
print(roulette("even", 5))