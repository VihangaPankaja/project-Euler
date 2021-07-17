""" 
    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
*       High Card            Highest value card.
*       One Pair             Two cards of the same value.
*       Two Pairs            Two different pairs.
*       Three of a Kind      Three cards of the same value.
*       Straight             All cards are consecutive values.
*       Flush                All cards of the same suit.
*       Full House           Three of a kind and a pair.
*       Four of a Kind       Four cards of the same value.
*       Straight Flush       All cards are consecutive values of same suit.
*       Royal Flush          Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
*       2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the highest value wins; 
    for example, a pair of eights beats a pair of fives (see example 1 below). 
    But if two ranks tie, for example, both players have a pair of queens, 
    then highest cards in each hand are compared (see example 4 below); 
    if the highest cards tie then the next highest cards are compared, and so on.

    Consider the following five hands dealt to two players:

*       Hand	 	Player 1	 	    Player 2	 	        Winner
*       1	 	    5H 5C 6S 7S KD      2C 3S 8S 8D TD      
*                   Pair of Fives       Pair of Eights          Player 2
*       
*       2	 	    5D 8C 9S JS AC      2C 5C 7D 8S QH
*                   Highest card Ace    Highest card Queen      Player 1
*       
*       3	 	    2D 9C AS AH AC      3D 6D 7D TD QD
*                   Three Aces          Flush with Diamonds     Player 2
*       
*       4	 	    4D 6S 9H QH QC      3D 6D 7H QD QS
*                   Pair of Queens      Pair of Queens          Player 1
*                   Highest card Nine   Highest card Seven
*       
*       5	 	    2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
*                   Full House          Full House              Player 1
*                   With Three Fours    with Three Threes

    The file, poker.txt, contains one-thousand random hands dealt to two players. 
    Each line of the file contains ten cards (separated by a single space): 
    the first five are Player 1's cards and the last five are Player 2's cards. 
    You can assume that all hands are valid (no invalid characters or repeated cards), 
    each player's hand is in no specific order, and in each hand there is a clear winner.

?   How many hands does Player 1 win?
"""

from typing import Callable
from statistics import mode     # or can use max(iter, lambda x: iter.count(x))


def Royal_flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Royal Flush and who whould win

    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand

    Returns
    ----
        int: 0 if no Royal Flush or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    
    def is_RoyalFlush(card: list[str], suits: list[str]) -> bool:
        if not all(suits[0] == x for x in suits[1:]):       # check if all are in same suit
            return False
        
        if not all(['T' in card, 'J' in card, 'Q' in card, 
                    'K' in card, 'A' in card]):     # if all cards between 10 to A contains
            return False
        return True
    
    if is_RoyalFlush(hand['p1']['card'], hand['p1']['suit']):       # player 1 has
        if is_RoyalFlush(hand['p2']['card'], hand['p2']['suit']):   # also player 2 has
            return 0
        return 1
    
    elif is_RoyalFlush(hand['p2']['card'], hand['p2']['suit']):     # only player 2 has
        return 2
    return 0    # no players have


def Staight_flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Staight flush and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Staight flush or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_StraightFlush(card: list[str], suits: list[str]) -> bool:
        if not all(suits[0] == x for x in suits[1:]):       # ckeck if all are same suit
            return False
        
        if (card_values[max(card, key=lambda x: card_values[x])] 
            - card_values[min(card, key=lambda x: card_values[x])]) == 4:       # ckeck if cards are consecutive
            return True
        return False
    
    if is_StraightFlush(hand['p1']['card'], hand['p1']['suit']):        # player 1 has
        if is_StraightFlush(hand['p2']['card'], hand['p2']['suit']):        # also player 2 has
            
            if ((p1:= card_values[max(hand['p1']['card'], key=lambda x: card_values[x])])       # max of player 1
                > (p2:= card_values[max(hand['p2']['card'], key=lambda x: card_values[x])])     # max of player 2
                ):          # player 1 has bigger cards
                return 1
            elif p1 == p2: return 0     # both players have same
            return 2        # player 2 has bigger cards
        return 1
    
    elif is_StraightFlush(hand['p2']['card'], hand['p2']['suit']):      # only player 2 has
        return 2
    return 0        # no player has


def Four_of_a_kind(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Four of a kind and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Four of a kind or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_FourofaKind(card: list[str]) -> bool:
        if card.count(mode(card)) == 4:     # has 4 same valued cards
            return True
        return False
    
    if is_FourofaKind(hand['p1']['card']):
        if is_FourofaKind(hand['p2']['card']):
            if (card_values[mode(hand['p1']['card'])]       # value of same valued cards of player 1
                > card_values[mode(hand['p2']['card'])]):   # value of same valued cards of player 2
                return 1
            return 2
        return 1
    
    elif is_FourofaKind(hand['p2']['card']):
        return 2
    return 0


def Full_house(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Full house and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Full house or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_FullHouse(card: list[str]) -> bool:
        if card.count(mode(card)) == 3:     # has 3 same valued cards
            if len(set(card)) == 2:         # also has 2 same valued cards
                return True
            return False
        return False
    
    if is_FullHouse(hand['p1']['card']):
        if is_FullHouse(hand['p2']['card']):
            if (card_values[mode(hand['p1']['card'])] 
                > card_values[mode(hand['p2']['card'])]):
                return 1
            return 2
        return 1
    
    elif is_FullHouse(hand['p2']['card']):
        return 2
    return 0


def Flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Flush and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Flush or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def Straight(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Straight and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Straight or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def Three_of_a_kind(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Three of a kind and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Three of a kind or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def Twe_pairs(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Twe pairs and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Twe pairs or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def One_pair(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is One pair and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no One pair or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def High_card(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is High card and who whould win
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values


def count_poker_wins(hands: list[dict[str,dict[str,list[str]]]], player: int) -> int:
    """ returns how many hands wins a player for given poker hands

    Args:
    ----
        hands (list[dict[str,dict[str,list[str]]]]): all hands played
        player (int): player (1 or 2)

    Returns:
    ----
        int:
    """
    
    rank: list[Callable] = [
        Royal_flush, 
        Staight_flush,
        Four_of_a_kind,
        Full_house,
        Flush,
        Straight,
        Three_of_a_kind,
        Twe_pairs,
        One_pair,
        High_card
    ]
    
    def winner(hand) -> int:
        for i in rank:
            if (win:= i(hand)):
                return win
            
    return [winner(hand) for hand in hands].count(player)


if __name__ == '__main__':
    card_values: dict[str, int] = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
    
    ## proccess text file 
    with open('files\p054_poker.txt', 'r', encoding='utf-8') as f:
        hands = f.read().split('\n')
    
    def format_data(hand):
        hand = hand.split()
        hand = [tuple(card) for card in hand]
        return {
            'p1':{
                'card':[x[0] for x in hand[:5]],
                'suit':[x[1] for x in hand[:5]],
            },
            'p2':{
                'card':[x[0] for x in hand[5:]],
                'suit':[x[1] for x in hand[5:]]
            }
        }
    
    hands: list[dict[str,dict[str,list[str]]]] = [format_data(hand) for hand in hands]
    ######################

    print(count_poker_wins(hands, 1))
    