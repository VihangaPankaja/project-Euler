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
from statistics import mode, multimode     # or can use max(iter, key=lambda x: iter.count(x)) for mode


def Royal_flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Royal Flush and who would win
        Ten, Jack, Queen, King, Ace, in same suit

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
        
        return all(['T' in card, 'J' in card, 'Q' in card, 
                    'K' in card, 'A' in card])     # if all cards between 10 to A contains
    
    if is_RoyalFlush(hand['p1']['card'], hand['p1']['suit']):       # player 1 has
        if is_RoyalFlush(hand['p2']['card'], hand['p2']['suit']):   # also player 2 has
            return 0
        return 1
    
    elif is_RoyalFlush(hand['p2']['card'], hand['p2']['suit']):     # only player 2 has
        return 2
    return 0    # no players have


def Straight_flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Straight flush and who would win
        All cards are consecutive values of same suit,
        if both hands are Straight flush, player with most valued card wins
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Straight flush or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_StraightFlush(card: list[str], suits: list[str]) -> bool:
        if not all(suits[0] == x for x in suits[1:]):       # check if all are same suit
            return False
        
        return (card_values[max(card, key=lambda x: card_values[x])] 
            - card_values[min(card, key=lambda x: card_values[x])]) == 4       # check if cards are consecutive
    
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
    """ checks if the hand is Four of a kind and who would win
        Four cards of the same value,
        if both hands are Four of a kind, player with most valued same 4 card wins
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Four of a kind or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_FourofaKind(card: list[str]) -> bool:
        return card.count(mode(card)) == 4     # has 4 same valued cards
    
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
    """ checks if the hand is Full house and who would win
        Three cars are same value and other 2 cards also same value pair,
        if both hands are Full House, player with most valued same 3 cards wins

    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Full house or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_FullHouse(card: list[str]) -> bool:
        if card.count(mode(card)) == 3:         # has 3 same valued cards
            return len(set(card)) == 2          # also has 2 same valued cards
        return False
    
    if is_FullHouse(hand['p1']['card']):
        if is_FullHouse(hand['p2']['card']):
            if (card_values[mode(hand['p1']['card'])]           # value of same 3 cards of player 1
                > card_values[mode(hand['p2']['card'])]):       # value of same 3 cards of player 2
                return 1
            return 2
        return 1
    
    elif is_FullHouse(hand['p2']['card']):
        return 2
    return 0


def Flush(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Flush and who would win
        All cards of the same suit,
        if both hands are Flush, 
        player with most valued card wins,
        if those cards are same check for next most valued card and so on
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Flush or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_Flush(suit: list[str]) -> bool:
        return len(set(suit)) == 1          # all in same suit
    
    if is_Flush(hand['p1']['suit']):
        if is_Flush(hand['p2']['suit']):
            p1: list[str] = sorted(hand['p1']['card'], key=lambda x: card_values[x], reverse=True)     # sort by card values in descending order
            p2: list[str] = sorted(hand['p2']['card'], key=lambda x: card_values[x], reverse=True)
            
            for i in range(5):
                if p1[i] != p2[i]:
                    return {True:1, False:2}[card_values[p1[i]] > card_values[p2[i]]]       # which one has more value
            return 0                                                                        # if all same
        return 1
    
    elif is_Flush(hand['p2']['suit']):
        return 2
    return 0


def Straight(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Straight and who would win
        All cards are consecutive values,
        if both hands are Straight,
        check for most valued card
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Straight or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_Straight(card: list[str]) -> bool:
        return ((card_values[max(card, key= lambda x: card_values[x])] 
                 - card_values[min(card, key=lambda x: card_values[x])])  == 4        # is consecutive 5 cards
                        and len(set(card)) == 5)                                      # no same cards

    if is_Straight(hand['p1']['card']):
        if is_Straight(hand['p2']['card']):
            if ((p1:= card_values[max(hand['p1']['card'], key=lambda x: card_values[x])])          # max valued card of player 1
                > (p2:= card_values[max(hand['p2']['card'], key=lambda x: card_values[x])])):      # max valued card of player 2
                return 1
            elif p1 == p2:          # max valued cards are equal
                return 0
            return 2
        return 1
    
    elif is_Straight(hand['p2']['card']):
        return 2
    return 0


def Three_of_a_kind(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Three of a kind and who would win
        Three cards of the same value,
        if both hands are Three of a kind,
        player with most valued 3 same cads wins
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Three of a kind or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_TreeofaKind(card: list[str]) -> bool:
        return card.count(mode(card)) == 3
    
    if is_TreeofaKind(hand['p1']['card']):
        if is_TreeofaKind(hand['p2']['card']):
            return {True:1, False:2}[card_values[mode(hand['p1']['card'])] 
                                     > card_values[mode(hand['p2']['card'])]]       # which has higher value 3 cards
        return 1
    
    elif is_TreeofaKind(hand['p2']['card']):
        return 2
    return 0


def Two_pairs(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is Twe pairs and who would win
        Two different pairs,
        if both hands are Twe pairs,
        check for most valued pair,
        if those are same check next pair,
        if all of above are same check the other card
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no Twe pairs or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_TwoPair(card: list[str]) -> bool:
        return len(multimode(card)) == 2        # 2 modes ⟹ 2 pairs
    
    if is_TwoPair(hand['p1']['card']):
        if is_TwoPair(hand['p2']['card']):
            p1: list[str] = sorted(multimode(hand['p1']['card']), key=lambda x: card_values[x], reverse=True)       # sort values of 2 pairs
            p2: list[str] = sorted(multimode(hand['p2']['card']), key=lambda x: card_values[x], reverse=True)
            
            for i in range(2):
                if p1[i] != p2[i]:                                              # if values of pairs are different
                    return {True:1, False:2}[card_values[p1[i]] > card_values[p2[i]]]
            else:       # if pairs are similar
                p1 = [i for i in set(hand['p1']['card']) if i not in p1]        # find single card in hand
                p2 = [i for i in set(hand['p2']['card']) if i not in p2]        # find single card in hand

                if p1[0] != p2[0]:      
                    return {True:1, False:2}[card_values[p1[0]] > card_values[p2[0]]]                     # if single cards are different
            return 0                                                            # all card values similar
        return 1

    elif is_TwoPair(hand['p2']['card']):
        return 2
    return 0


def One_pair(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is One pair and who would win
        Two cards of the same value,
        if both hands are One pair,
        check for most valued pair,
        if those are same,
        check max valued card from others,
        if those are same,
        check next max valued card and so on
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 0 if no One pair or tie, 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    def is_OnePair(card: list[str]) -> bool:
        return card.count(mode(card)) == 2     # one pair
    
    if is_OnePair(hand['p1']['card']):
        if is_OnePair(hand['p2']['card']):
            if mode(hand['p1']['card']) != mode(hand['p2']['card']):
                return {True:1, False:2}[card_values[mode(hand['p1']['card'])] 
                                         > card_values[mode(hand['p2']['card'])]]                           # which has biggest in pair
            
            p1: list[str] = sorted([i for i in hand['p1']['card'] if i != mode(hand['p1']['card'])], 
                                    key=lambda x: card_values[x], reverse=True)                             # sorted cards without pair
            p2: list[str] = sorted([i for i in hand['p2']['card'] if i != mode(hand['p2']['card'])], 
                                    key=lambda x: card_values[x], reverse=True)
            
            for i in range(3):      # check other cards
                if p1[i] != p2[i]:
                    return {True:1, False:2}[p1[i] > p2[i]]
            return 0    # all cards are equal
        return 1
    
    elif is_OnePair(hand['p2']['card']):
        return 2
    return 0
    

def High_card(hand: dict[str,dict[str,list[str]]]) -> int:
    """ checks if the hand is High card and who would win
        Most valued card,
        if those are same check the next most valued card and so on
    
    Args
    ----
        hand (dict[str,dict[str,list[str]]]): hand
    
    Returns
    ----
        int: 1 if player 1 wins, 2 if player 2 wins
    """
    global card_values
    
    p1: list[int] = sorted([card_values[i] for i in hand['p1']['card']], reverse=True)       # sort descending order by card values
    p2: list[int] = sorted([card_values[i] for i in hand['p2']['card']], reverse=True)
    
    if p1 != p2:
        return {True:1, False:2}[p1 > p2]
    return 0


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
        Straight_flush,
        Four_of_a_kind,
        Full_house,
        Flush,
        Straight,
        Three_of_a_kind,
        Two_pairs,
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
    