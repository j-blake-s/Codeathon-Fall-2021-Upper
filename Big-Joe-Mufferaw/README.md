Big Joe's Log Run
================

Problem Statement
-----------------
On a log run down to Quebec City, Big Joe Mufferaw sees that the raft is beginning to split. Most log drivers would just cut their losses instead of risking their lives for the run, but Big Joe isn't just any logger. He is, after all, the best man in Ottawa, so he devises a plan to run along the logs until he reaches the opposite corner where he can retie the raft. Given the layout of the logs in the raft, determine the route Big Joe should take to get there as fast as possible.

Listen [here](https://youtu.be/Ctx14x2HHao) for more tall tales of Big Joe.

Input Format
------------
* The first line has two space separated integers, $n$ $m$, where $n$ is the size of the raft in units and $m$ is the number of logs.
* The remaining $m$ lines have space separated $x_1$ $y_1$ $x_2$ $y_2$ coordinates of the start and end points for each log. Logs are referred to by their index in this list (starting from 0 for the first log).

### Restrictions
* Each log is exactly one unit in length (up to floating point precision).
* There will be exactly one log which begins at (0,0) and exactly one which ends at (1,1). These are guaranteed to be included in the resulting path.
* (TODO determine restrictions to ensure logs are somewhat evenly distributed in the space and not too close together)

Output Format
-------------
Output the sequence of logs that Big Joe will take to cross the raft