Terra and Beast Boy are looking at two similar mazes. Thanks to Beast Boy, he has a bird's eye view of both mazes (the perspective shown in the input). Terra chooses the maze at the top of the view, Beast Boy chooses the maze at the bottom of the view. Beast Boy wants to have a race where they both start at the same starting coordinates in their respective mazes. Terra notices that not all starting spots lead to an exit in both mazes. To see how many ways this could go wrong, she wants to know how many starting spots there are where one of them can escape from those starting coordinates in their respective maze, but the other can not. Open spots are shown as "." walls are shown as "#". To "escape" a starting spot must eventually connect to an open space on the right side of the maze

# Input Format

The first line contains  and , the dimensions of the board.

The next  lines are each of length  describing the first maze.

There is then a blank line, then  more lines each of length  describing the second maze.

# Constraints

The maze will only contain "." (representing open space) and "#" representing wall

# Output Format

Output the number of starting spaces that can be chosen where only one of them can escape from that point.