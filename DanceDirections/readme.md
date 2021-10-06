Derek the Disco Dancer has given you a list of directions so that you can dance like a Disco star! However, some of the instructions are very long, and you want to know how far you will end up from where you start. Find the Manhattan distance (x displacement + y displacement) from your starting spot to your ending spot after performing all of the instructions. Before each list of instructions, you start back at the middle of the gym, facing north.

The first line contains $t$, the number of test cases. $t$ test cases follow. Each test case starts with a number $n$, followed by $n$ dance instructions. 

One type of instruction consists of N, S, E, or W, (north, south, east, or west) a space, followed by a number $s$, the number of steps to move in that direction.

Another type consists of CW or CCW, (clockwise and counter clockwise) a space, followed by a number $s$, the number of degrees to turn (for this instruction type, $s$ will always be evenly divisible by 90).

The last type consists of F or B, (forward and backward) a space, followed by a number $s$, the number of steps to move in the direction that you are currently facing based on your rotation.