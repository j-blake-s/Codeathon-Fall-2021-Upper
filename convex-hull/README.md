# Mapping Clusters

Mr. Nim wants to know if he should open a new store. He wants to make sure he
begins cornering his market, so he does not want to expand into new territory.
He wants his new store to be bounded by his existing stores.

# Formal Problem Statement

Given a list of $n$ 2D points, $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$,
determine if a point $(x,y)$ can be bounded by the polygon of some subset of points.

# Input

Note: This is a multiple problem set input. You will receive multiple sets of
problems. You will receive an integer, $k$, which will be the total number of
problems to solve. For each of the $k$ problems, you will receive an integer,
$n$, that will correspond to the number of stores in his network. These will be
coordinates with an $x$ and a $y$ floating point separated by a space. Then a
point that is the coordinates of the new store. And lastly a new line delimited
list of points making up his current network.

```
2
3
15.0 15.0
70.0 70.0
0.0 0.0
0.0 70.0
4
80.0 80.0
70.0 70.0
0.0 0.0
0.0 70.0
70.0 0.0
```

# Constraints

$$1 \leq k \leq 1024$$
$$3 \leq n \leq \text{TBD}$$
$$-50000 \leq x,y \leq 50000$$

# Output

```
Yes
No
```
