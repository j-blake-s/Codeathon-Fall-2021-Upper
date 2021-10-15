Kicked Outta Vegas
==================

Problem Statement
-----------------
Tired of sitting around doing nothing in the Pacific Islands, Biskit decided to book a flight out to try his hand in Las Vegas. To the surprise of everyone, Biskit turns out to be quite a card shark, with the ability to remember every card that has been played in a round. After winning every other game in the house, he shifts his focus to the new game of Hidden Kings, where two players compete to beat the other according to an unknown ranking system. In this game, each player receives $n$ cards labelled $1$ through $n$, and in each round, both players pick a card to play. A scorekeeper then looks at the hidden ranking system and announces which card wins the round. After all cards have been played, each player picks the card they believe to be the highest ranked overall, at which point the hidden ranking system is announced and the player who picked the highest card is deemed the winner. As in all classy card games, ties are broken by a game of rock-paper-scissors.

Input Format
------------
The first line contains an integer $n$ and all remaining lines each are of the form "$i$ > $j$" or "$i$ < $j$" where $i$ and $j$ are integer card values and the comparison symbol denotes which card is higher ranked in the hidden ranking.

### Restrictions
* $1 \leq n \leq 2^20$
* $1 \leq i,j \leq n$ for each $i,j$

Output Format
-------------
With each item on a separate line, output the sorted list of cards which are most likely to win in the final pick. These are the ones which beat the most other cards (noting that if $a$ beats $b$ and $b$ beats $c$, then $a$ also beats $c$).

Sample Explanations
-------------------

# Sample 0

In this sample, 4 beats 2, 5, and 6. The main contenders are 3, which beats 9 and 1; 10, which beats 8 and 9; and 7, which beats 1 and 8. However, 4 is the only card which is known to beat three other cards.

# Sample 1

In this sample, 12 beats 3, 4, and 5, more than any other card in the deck.

# Sample 2

No explanation

# Sample 3

In this sample, 13 beats 1, 18, and 17 while 14 beats 2, 7, and 20. Since this is a tie, both are outputted.
