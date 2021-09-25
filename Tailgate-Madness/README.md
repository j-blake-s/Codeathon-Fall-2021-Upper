Tailgate Madness
===============

Problem Statement
-----------------
Tonight is game night, and Kenny knows his sequence of tailgates will be wild. As the responsible person he is, he also wants to make sure he can find a sober driver to get him to the game when the clock hits 7. Kenny has $n$ tailgates that he wants to get to (labeled by integer IDs), and in order to help him plan, he gives each of them a score in $m$ categories. His schedule consists of a new formula every 5 minutes, which tells him how to assign an overall score to each tailgate. Each time the formula changes, he ranks the tailgates according to the given formula from least to greatest (ties broken in order of ID) and goes to the one which ranks $i$ steps above the current one (the step after the highest ranking tailgate returns to the lowest ranking). Determine the last stop on Kenny's crazy sequence of $k$ tailgates, so he knows where he needs to find a sober driver.

Input Format
------------
The first line has three space separated integers, $n$, $m$, and $k$.

The next $k$ lines each have a formula (described shortly) and an integer step size $i$, space separated.
Formulas are composed of single character variables interspersed with + symbols.
In the score lists (described next), variable $a$ corresponds to the first score, then $b$, $c$, and so on.
The formula value is the sum of each of these scores.

The remaining $n$ lines each have $m$ space separated integer scores for a tailgate. Tailgate IDs are assigned in order starting from 0 for the first.

### Restrictions
* $1 \leq n \leq 2^14$
* $1 \leq m \leq 8$
* $1 \leq k \leq 2^20$
* For each step $i$, $0 \leq i < 2^31$
* For each score $s$, $0 \leq s \leq 2^24$ (note that any possible formula will be less than the standard max int $2^31-1$)

Output Format
-------------
One line with the ID of the tailgate where Kenny ends up.
