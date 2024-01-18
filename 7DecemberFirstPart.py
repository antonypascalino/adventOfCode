import functools
# 0 high card
# 1 pair
# 2 double pair
# 3 tris
# 4 full
# 5 poker
# 6 five-poker
ordered_hands = [[] for _ in range(7)]

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def evaluate(hand, bid):
    card_count = {}
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    if 5 in card_count.values():
        return hand, bid, 6
    elif 4 in card_count.values():
        return hand, bid, 5
    elif 3 in card_count.values() and 2 in card_count.values():
        return hand, bid, 4
    elif 3 in card_count.values():
        return hand, bid, 3
    elif 2 in card_count.values() and card_count.__len__() == 3:
        return hand, bid, 2
    elif 2 in card_count.values():
        return hand, bid, 1
    else:
        return hand, bid, 0


def add_hand(evaluated_hand):
    for hand in ordered_hands[evaluated_hand[2]]:
        if compare_hands(evaluated_hand[0], hand[0]) > 0:
            continue
        else:
            ordered_hands[evaluated_hand[2]].insert(ordered_hands[evaluated_hand[2]].index(hand), evaluated_hand)
            break
    else:
        ordered_hands[evaluated_hand[2]].append(evaluated_hand)


def compare_hands(hand1, hand2):
    for char1, char2 in zip(hand1, hand2):
        if char1 == char2:
            continue
        else:
            if cards.index(char1) > cards.index(char2):
                return 1
            else:
                return 0


while True:
    user_input = input()
    if user_input == "":
        break
    hand = user_input.split(" ")[0]
    bid = user_input.split(" ")[1]

    evaluated_hand = evaluate(hand, bid)
    add_hand(evaluated_hand)

all_hands = functools.reduce(lambda arr1, arr2: arr1 + arr2, ordered_hands)
print(all_hands)

winnings = 0

for hand in all_hands:
    print(all_hands.index(hand) + 1, hand[1])
    winnings += (all_hands.index(hand) + 1) * int(hand[1])
print(winnings)



