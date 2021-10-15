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
* $1 \leq n \leq 2^{14}$
* $1 \leq m \leq 8$
* $1 \leq k \leq 2^{20}$
* For each step $i$, $0 \leq i < 2^{31}$
* For each score $s$, $0 \leq s \leq 2^{24}$ (any formula evaluates to $\leq 2^{31}-1$)

Output Format
-------------
One line with the ID of the tailgate where Kenny ends up.

Sample Text
-----------

# Sample 0

In this sample, there is only one scoring metric, labelled $a$, so we are simply moving through a single ranking.

| Tailgate ID | 0 | 3 | 2 | 1 |
|-------------|---|---|---|---|
| Score $a$   | 1 | 5 | 7 | 8 |

Using this order, the path that Kenny takes is as follows. He ends at tailgate 1.

|    _    | _ | _ |    _    |         Comment         |
|:-------:|:-:|:-:|:-------:|:-----------------------:|
| __[0]__ | 3 | 2 |    1    |  Starting configuration |
| __[0]__ | 3 | 2 |    1    | Step 4 (wrap back to 0) |
|    0    | 3 | 2 | __[1]__ |          Step 3         |

# Sample 1

In this sample, we have multiple different ways to sort because there are 3 formula variables, $a$, $b$, and $c$. The table shows the 4 relevant scoring systems.

| Tailgate ID |  0 | 1 |  2 |  3 |
|:-----------:|:--:|:-:|:--:|:--:|
|  Score $a$  |  4 | 0 |  1 | 12 |
|  Score $b$  |  8 | 6 | 11 |  9 |
|  Score $c$  |  1 | 7 |  8 |  2 |
| Score $a+b$ | 12 | 6 | 12 | 21 |

Next, we show the order of tailgates under each scoring system, which will be used to step through in the last table.

|    Sort Order    | _ | _ | _ | _ |
|:----------------:|:-:|:-:|:-:|:-:|
|  Sorting on $a$  | 1 | 2 | 0 | 3 |
|  Sorting on $b$  | 1 | 0 | 3 | 2 |
|  Sorting on $c$  | 0 | 3 | 1 | 2 |
| Sorting on $a+b$ | 1 | 0 | 2 | 3 |

Finally, we align subsequent scoring systems so the current tailgate ID matches between the two and keep stepping under the different scoring system. Notice that although the first $a+b$ step does not match the $a+b$ sorting exactly, it is equivalent up to rotation.

|    _    |    _    |    _    |    _    | Comment           |
|:-------:|:-------:|:-------:|:-------:|-------------------|
| __[0]__ | 1       | 2       | 3       | Original ordering |
| &#8595; |         |         |         |                   |
|    0    |    3    | __[1]__ |    2    | Step 10 by $c$    |
|         |         | &#8595; |         |                   |
|    2    |    3    |    1    | __[0]__ | Step 1 by $a+b$   |
|         |         |         | &#8595; |                   |
| 2       | __[3]__ | 1       | 0       | Step 2 by $a+b$   |

# Sample 2

Following the example of the previous sample, we first calculate all the relevant formulas.

| Tailgate ID |  0 |  1 |  2 |  3 |  4 |  5 |  6 |
|:-----------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|     $a$     |  7 |  3 | 10 | 11 |  6 |  7 |  8 |
|     $b$     |  2 | 12 | 22 | 19 | 12 | 10 |  7 |
|     $c$     | 11 | 19 | 22 |  1 | 18 | 20 | 13 |
|    $a+b$    |  9 | 15 | 32 | 30 | 18 | 17 | 15 |
|    $a+c$    | 18 | 22 | 32 | 12 | 24 | 27 | 21 |
|    $b+c$    | 13 | 31 | 44 | 20 | 30 | 30 | 20 |
|   $a+b+c$   | 20 | 34 | 54 | 31 | 36 | 37 | 28 |

Then we rank the tailgates according to each formula.

| ID Sorting | _ | _ | _ | _ | _ | _ | _ |
|:----------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|     $a$    | 1 | 4 | 0 | 5 | 6 | 2 | 3 |
|     $b$    | 0 | 6 | 5 | 1 | 4 | 3 | 2 |
|     $c$    | 3 | 0 | 6 | 4 | 1 | 5 | 2 |
|    $a+b$   | 0 | 1 | 6 | 5 | 4 | 3 | 2 |
|    $a+c$   | 3 | 0 | 6 | 1 | 4 | 5 | 2 |
|    $b+c$   | 0 | 3 | 6 | 4 | 5 | 1 | 2 |
|   $a+b+c$  | 0 | 6 | 3 | 1 | 4 | 5 | 2 |

Finally, we step through the rankings to determine that Kenny will stop at tailgate 1.

|    _    |    _    | _ |    _    | _ |    _    |    _    |      Comment      |
|:-------:|:-------:|:-:|:-------:|:-:|:-------:|:-------:|:-----------------:|
| __[0]__ |    1    | 2 |    3    | 4 |    5    |    6    | Original Ordering |
| &#8595; |         |   |         |   |         |         |                   |
|    0    | __[1]__ | 6 |    5    | 4 |    3    |    2    |    29 by $b+a$    |
|         | &#8595; |   |         |   |         |         |                   |
|    5    |    1    | 2 |    0    | 3 | __[6]__ |    4    |    46 by $b+c$    |
|         |         |   |         |   | &#8595; |         |                   |
|    1    |    4    | 3 |    2    | 0 |    6    | __[5]__ |      1 by $b$     |
|         |         |   |         |   |         | &#8595; |                   |
|    6    |    2    | 3 | __[1]__ | 4 |    0    |    5    |     25 by $a$     |
|         |         |   | &#8595; |   |         |         |                   |
| __[6]__ |    2    | 3 |    1    | 4 |    0    |    5    |     46 by $a$     |
| &#8595; |         |   |         |   |         |         |                   |
|    6    | __[4]__ | 1 |    5    | 2 |    3    |    0    |     15 by $c$     |
|         | &#8595; |   |         |   |         |         |                   |
|    1    |    4    | 5 | __[2]__ | 3 |    0    |    6    |    44 by $c+a$    |
|         |         |   | &#8595; |   |         |         |                   |
|    5    | __[4]__ | 3 |    2    | 0 |    1    |    6    |    47 by $a+b$    |
|         | &#8595; |   |         |   |         |         |                   |
|    6    |    4    | 1 |    5    | 2 | __[3]__ |    0    |     18 by $c$     |
|         |         |   |         |   | &#8595; |         |                   |
|    4    |    5    | 2 |    0    | 6 |    3    | __[1]__ |   29 by $c+a+b$   |
