## See tests:

[here](solutions/README.md)


# Mapping Clusters

Arnold needs to find the minimum area that contains the polygon created by any
3,4,5... points.  He wants to make sure that a gas station is not only a certain
distance from each other, which he has another algorithm for, but he wants to
make sure that he has a certain average cover of area per gas station. Any three
gas stations chosen should make an area that is included. What is the minimum
area he needs to consider?

# Formal Problem Statement

Given a list of $n$ 2D points, $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$,
determine the area in units squared that is the minimum area needed to cover all
points without concavities(corners that bend inwards).

# Input

You will receive an integer, $n$, that will correspond to the number of stores
in his city. These will be coordinates with an $x$ and a $y$ floating point
separated by a space. These coordinates are a new line delimited list of points
making up his current city buildings.

```
3
70.0 70.0
0.0 0.0
0.0 70.0
```

```
4
0.0 0.0
0.0 70.0
70.0 0.0
70.0 70.0```

# Constraints

$$3 \leq n \leq \text{TBD}$$

$$-50000 \leq x,y \leq 50000$$

# Output
$$0 \leq x \leq 2^31$$

```

# Output

Output the area of containing all of the points.
