# Mapping Clusters

Mr. Nim wants to surround his town with a giant rubber band(that can be used to
contain water and fill it with water. He has the rubber band covered, and is now
trying to figure out how much water he needs. He needs you to figure out how
much water to pump. Remember, rubber bands do not form concavities. 

# Formal Problem Statement

Given a list of $n$ 2D points, $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$,
determine the area in units squared that is the minimum area needed to cover all
points without concavities.

# Input

You will receive an integer, $n$, that will correspond to the number of stores
in his city. These will be coordinates with an $x$ and a $y$ floating point
separated by a space. These coordinates are a new line delimited list of points
making up his current city buildings.

```3
70.0 70.0
0.0 0.0
0.0 70.0
```

```4
0.0 0.0
0.0 70.0
70.0 0.0
70.0 70.0```

# Constraints

$$3 \leq n \leq \text{TBD}$$ $$-50000 \leq x,y \leq 50000$$

# Output

```
Yes
No
```
