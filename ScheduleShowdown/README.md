# Schedule Showdown

Alice, a Computer Science major, is arguing with Bob, an Electrical Engineering
major about who has the harder degree program. Their friend Eve overhears the
argument and proposes a simple test: whichever one of them can take the most
classes this semester must have the harder degree.

Help Alice and Bob settle their argument by determining the schedule for each
of them which contains the most classes, then seeing which schedule has the
greater number classes. Note that the Registrar will not allow students to
register for classes which occur at overlapping times.

## Input

The input consists of the following, in order:

1. An integer $A$ indicating the number of classes Alice *could* register for,
   on its own line.
2. $A$ many lines, each containing a start time and end time (in that order,
   separated by a space) for a given class that Alice could register for. Times
   are given in `HH:MM` format, with 24-hour time.
3. An integer $B$ indicating the number of classes Bob *could* register for,
   on its own line.
4. $B$ many lines, each indicating the start and end time for a class Bob could
   register for.

The input is subject to the following constraints:

* No class time ever crosses midnight (each class starts and ends on the same
  day)
* Time zones don't exist
* No really, this problem isn't about date handling, drop the `dateutil` and
  step away from the keyboard
* $1 \leq A \leq 2^16$
* $1 \leq B \leq 2^16$


## Output

The first line of your output should be one of three possible strings depending
on who has the busiest possible schedule:

* `Alice` if Alice has the schedule with the most classes.
* `Bob` if Bob has the schedule with the most classes.
* `Tie` otherwise if both have an equal number of classes.

The second line of your output should be the number of classes the busier
person has in their schedule.

## Example

TODO

