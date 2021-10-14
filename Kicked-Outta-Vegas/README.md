Kicked Outta Vegas
==================

Problem Statement
-----------------
Tired of sitting around doing nothing in the Pacific Islands, Biskit decided to book a flight out to try his hand in Las Vegas. To the surprise of everyone, Biskit turns out to be quite a card shark, with the ability to remember every card that has been played in a round. After winning every other game in the house, he shifts his focus to the new game of Hidden Kings, where two players compete to beat the other according to an unknown ranking system. In this game, each player receives $n$ cards labelled $1$ through $n$, and in each round, both players pick a card to play. A scorekeeper then looks at the hidden ranking system and announces which card wins the round. After all cards have been played, each player picks the card they believe to be the highest ranked overall, at which point the hidden ranking system is announced and the player who picked the highest card is deemed the winner. As in all classy card games, ties are broken by a game of rock-paper-scissors.

Input Format
------------
The first line contains an integer $n$ and all remaining lines each are of the form "$i$ > $j$" or "$i$ < $j$" where $i$ and $j$ are integer card values and the comparison symbol denotes which card is higher ranked in the hidden ranking.

### Restrictions
* $1 \leq n \leq 2^24$
* $1 \leq i,j \leq n$ for each $i,j$

Output Format
-------------
With each item on a separate line, output the sorted list of cards which are most likely to win in the final pick. These are the ones which beat the most other cards (noting that if $a$ beats $b$ and $b$ beats $c$, then $a$ also beats $c$).

(TODO handle cards played against themselves)