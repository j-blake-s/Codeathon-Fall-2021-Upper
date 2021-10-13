# Schedule Showdown

Alice, a Computer Science major, is arguing with Bob, an Electrical Engineering
major about who has the harder degree program. Their friend Eve overhears the
argument and proposes a simple test: whichever one of them can take the most
classes this semester must have the harder degree.

Help Alice and Bob settle their argument by determining the schedule for each
of them which contains the most classes, then seeing which schedule has the
greater number classes. Note that the Registrar will not allow students to
register for classes which occur at overlapping times, however the registrar
does not account for travel time, so a student *can* register for a class which
ends exactly at the same time as another which they are registered for begins.

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
* $1 \leq A \leq 2^18 - 1$
* $1 \leq B \leq 2^18 - 1$


## Output

The first line of your output should be one of three possible strings depending
on who has the busiest possible schedule:

* `Alice` if Alice has the schedule with the most classes.
* `Bob` if Bob has the schedule with the most classes.
* `Tie` otherwise if both have an equal number of classes.

The second line of your output should be the number of classes the busier
person has in their schedule.

## Examples

### Example 1

Input:

```
3
07:00 08:10
09:00 09:50
10:00 12:30
2
08:00 09:00
10:00 11:00
```

Output:

```
Alice
3
```

Explanation:

Alice has 3 possible classes she could register for. Since none of them
overlap, her busiest possible schedule would be to register for all three
classes.


Bob has 2 possible classes he could register for, neither of which overlap.
Even though he can take all of them, his busiest schedule is only 2 classes.

3 is more than 2, so Alice must have the more difficult major, hence our output
is `Alice`, followed by `3`, the number of classes in her busiest schedule.

### Example 2

Input:

```
5
08:00 09:15
09:00 10:15
10:30 11:30
14:00 15:15
16:00 16:45
6
11:00 11:45
11:30 12:30
11:55 13:00
12:30 14:30
16:00 18:00
18:30 20:00
```

Output:

```
Tie
4
```

Explanation:

Alice has 5 possible classes she could register for, but some of them overlap.
She must choose between the `09:00 10:15` class and the `9:45 11:30` class,
since the latter starts before the former ends. Alice has two busiest possible
schedules, being:
* `08:00 09:15`, `10:30 11:30`, `14:00 15:15`, `16:00 16:45`
* `09:00 10:15`, `10:30 11:30`, `14:00 15:15`, `16:00 16:45`



Bob has 6 possible classes, but two of them overlap: he can't take both the
`11:00 11:45` and the `11:30 12:30` class, nor can he take both the `11:55
13:00` and `12:30 14:30` classes at once. Bob has three possible busiest
schedules, each with four classes:
* `11:00 11:45`, `11:55 13:00`, `16:00 18:00`, `18:30 20:00`
* `11:00 11:45`, `12:30 14:30`, `16:00 18:00`, `18:30 20:00`
* `11:30 12:30`, `12:30 14:30`, `16:00 18:00`, `18:30 20:00`

