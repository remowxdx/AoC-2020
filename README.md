# Advent of Code 2020

These are my attempts to solve the [Advent of Code 2020](https://adventofcode.com/2020).

## [Day 1](https://adventofcode.com/2020/day/1)

OK, day 1 has been easy, 7 minutes to do part 1 and other 4 to do part 2.

The puzzle asked to find in a list of number two (or three) numbers that
added together give the result of *2020*.

For the first solution I simply ran two (or three) nested loops over the data
and checked if the result was 2020.

```
for first in data:
    for second in data:
        if first + second == 2020:
            return found

```

I did not worry about taking twice (or thrice) the same number (1010), also
I don't think it was clear if that was allowed.
And the algorithm also tries the couple of number twice.

After having found the solutions I tried to find a more general and elegant
solution.
After a bit of thinking, I came up with a recursive solution.
Also this solution doesn't worry about taking the same number more than
once, and the numbers are tried more than once in various orders.

The idea of the recursion is that you get the first number, and then you try
to find a (shorter) list of number that sums to 2020 minus that first number.
You stop when the length of the sum is zero.
If also the target is zero you are OK. If not the previous steps weren't
good.


```
def find_sum_eq(data, target, num):
    if num == 0:
# We are at the end of our search... if also target is 0
# we have found a good set of numbers
        if target == 0:
            return []
# Otherwise we are not on the good track
        else:
            return None

# Try for every number in list
    for n in data:
        r = find_sum_eq(data, target - n, num - 1)
        if r is None:
# This n is not good
            continue
        else:
            r.append(n)
            return n
```

To speed up thing we could test only data after the current n.

```
for index, n in enumerate(data):
    r = find_sum_eq(data[index:], target - n, num - 1)
```

And to speed up still more we could sort then numbers before looping
and stop the recursion once we get over 2020 (or below 0).

## [Day 2](https://adventofcode.com/2020/day/2)

This problem took me longer that it should have: 24 minutes for part 1 and
other 28 minutes for part 2.
The problem was easy to solve, but I made some mistakes in the parsing
of the strings... and reading the wording of the problem:

- it took me too much time to parse the policy part of the input
- I didn't realized that I left a space at the start of some passwords, thus
changing the indexing of the position of the letters.
- I didn't read the *"exactly one of these positions"* although it was emphasized.

My first solution is straightforward: simply split the lines of the input
to get the policy and the password (without the starting space!).

Then divide the policy to get the numbers and the letter.
For the Part 1, simply count how many times the letter appears in the password,
check if this number is not outside the policy range.
For Part 2 (the **real** policy!) just count the times the letter appears
in the first or second position, and return valid if it is *exactly* one.

After finding the right solutions, I refactored a little the algorithm:
now the check_password functions return a **1** or **0** instead of
**True** or **False**, so that I can create a list of **1**s and **0**s
and then just take the sum of the numbers in the list.

## [Day 3](https://adventofcode.com/2020/day/3)

Ok, Part 1 took me 22 minutes, Part 2 5.

Part 1 took longer because I thought that the *right* and *down* were
variable so I didn't hard coded them.
Also (and more time was sank here) my first solution was wrong and I didn't
understand why.
After too much time I discovered that it was because I left the '\n'
character at the end of each line reading the input from the file.
I will edit the scaffolding code, because I think that this problem will
show itself again.

I think that nothing particular goes on here:

- `dx` and `dy` in the function `count_trees` are resp. *right* and *down*
- the repeating pattern is simulated by the modulo (`x % width`)

In reality I expected that the second part wanted the slope with the minimum
number of tree encountered.

After finding the solutions I didn't know what to do to make something different.
After some thinking I decided to make the function `count_trees` parallel.
Also here nothing spectacular: now `count_trees` goes line by line updating
the tree count for each slope. The counting is done only if
`y % (down of slope)` is `0`.

## [Day 4](https://adventofcode.com/2020/day/4)

Part 1 took 25 minutes, Part 2 32.

This are the kind of problems which I like less: much parsing and many rules.

The implementation is straightforward: parse the passports in a list of
dicts (Maps) and then check that they have "all" required fields for part 1.
And also check that the value of the fields is valid for part 2.
As always I had problems parsing the strings...

For part 2 I decided to not use regular expression, so I worked with only
standard string method.

After finding the solution, I changed the function to check the validity
of the field to use regular expressions. 
I created a `dict` with the field as index, and a tuple with the regular
expression and the limits of the field as values.
Looking at it, I don't know which method is better...

My third attempt is using exceptions to validate passwords:
instead of returning `True` or `False` the functions validating
the passports raise Exceptions. I also changed where the validation
happens: now the validation is done during the parsing of the passports.
When there is an exception, we add the passport with a field 'valid',
that is then checked and counted.

## [Day 5](https://adventofcode.com/2020/day/5)

Good, 12 minutes for part 1 and 9 for part 2.

Contrary to the yesterday's problem, I liked this one.

What I immediately realized, was that "F", "B", "R", "L" are only another
way to write the seat number in binary: "F" means `0`, "B" means `1`, "L"
means `0` and "R" means `1`.

So the problem is *really easy* to solve: just transform the binary
number in base 10 and you have your seat ID.

```
# Gives the seat ID, given the code on the boarding pass
def seat_ID(code):
    id = 0
    for c in code:
        id *= 2 # Advance to the next exponent
        # If character in code correspond to a 1, just add one
        if c == 'B' or c =='R':
            id += 1
        # If character in code correspond to a 0, do nothing
    return id
```

Then you just have to find the maximum in your
boarding passes list.

For Part 2 I created an array of seats starting with `False` for
the free seats, then filled with `True` for every boarding pass.
Then I saw that in the middle of the seat list, there was only one free
seat, so I followed the array to find the first occupied seat and
then to the first with a free seat.

```
started = False  # In the front of the plane all seats are free
for id, seat in enumerate(s):
    if started == False and seat == True:
        # Here we found the first occupied seat
        started = True
    if started == True and seat == False:
        # Here we found the first free seat after the free on the front
        return id

```
Initally I created an array with all the seat IDs, but didn't use that.

## [Day 6](https://adventofcode.com/2020/day/6)

Today it took me 15 minutes to do Part 1 and 11 for Part 2.

For Part 1 I created an array with all the answer not already answered by
people in the same group.
The method is similar to what I did in Day 4 with the passports.
Then I summed the length of the answers of each group.

For Part 2, I followed the same spirit as Part 1, but I created an
array of 26 `True` values, one for each letter, then for each person
I set the array to `False` for each letter that was not `yes`.
That gives an array with a `True` only for the letters that have
been answered by all people in the group.

Finally I counted the `True`s in th entire array of groups.

## [Day 7](https://adventofcode.com/2020/day/7)

Sheesh, 52 minutes for Part 1 and 14 for Part 2.

I confirm that I don't like to parse those strings...
Took me forever to see that I left spaces around some of the words... and
I sprinkled `.strip()` everywhere!

Well the basis of today's puzzle is **recursion**!

I painfully parsed the rules in a `dict` where the keys are the bag
types and each contains a `dict` where the keys are the type of the
inner bags and as value have the number of bags:

```
rules = {
    'light red': {'bright white': 1, 'muted yellow': 2},
    ...
}
```

For Part 1, I wrote the function `find_bag()`, which takes the
parsed rules, the starting bag, the current bag and the target
bag. The recursion stops when we find the target bag (`current == target`).
Because we don't want repetitions, I return a `set` with the starting bag type.

Then we find the bags for each of the inner bag, adding into the result
set (use `update`, because `union` leaves the set unchanged!
*RTFM and save time!*).

For Part 2 another recursive function that counts the inner bags:
`count_bags` takes the rules and the starting bag.
`count` starts from 1 because it is the bag itself, then we add the
counts for all the inner bags.

From the result we subtract 1 because the *shiny gold* bag doesn't count.

After finding the solutions, I modified the parsing twice:

- first `split`ting the line in words and looking at the indices to
find bag types and quantities
- then using regular expression.

The `find` and `count` algorithms stayed the same.


## [Day 8](https://adventofcode.com/2020/day/8)

Part 1 took me 29 minutes, but Part 2 47 minutes!

Part 2 took so long because I forgot to restart the console after
each modification of the boot program... So after finding the
solution I added this `restart()` method, just to remember.

I actually liked this puzzle, it reminded me of last year puzzles.
Part 1 went more or less without problems, I created the `Console` class,
that is simulating the console.
It has some methods:

- one method to load the code (`decode()` initially, that then I
changed to `load()`)
- a `restart()`method to restart the console (after modifications!!!)
- an `execute()` method to execute one instruction
- a `step()` method to manage the actual instruction execution (raise
exceptions, keep track of already executed instruction, ...)
- a `run()` method to run the program
- and finally a `modify()` method to toggle an instruction between
`jmp` and `nop`

This class raises the appropriate `ConsoleException`s while running:

- `ConsoleError` for programming errors (should never raise)
- `ConsoleInfiniteLoop` when an infinite loop is detected
- `ConsoleTerminated` when the program successfully terminates

With these class and exceptions, the puzzle is pretty straightforward
just `run` the console and catch the appropriate exceptions.

## [Day 9](https://adventofcode.com/2020/day/9)

Part 1 done in 30 minutes and Part 2 in 10.

Here, like in yesterday's puzzle, I wrote a `class` to be the `XMAS`
cypher. The constructor shuold be given the data and the length of
the preamble.

The method for part 1 is `is_number_valid()` that takes the index of
the number that we want to check and gives `True` or `False`.
We just iterate over the length of the message (excluding the preamble)
until we find the *invalid* number.

For part 2 I wrote the `find_contiguous_set(_slow)()` method that
given a number, returns the list of contiguous numbers that sum up
to the given target.

It works by taking the first two numbers, summing them and see if they
are good. If not the first three numbers, then first four, etc.
Then repeats excluding the first number, then the second etc.

This method is slow but it worked.

After finding the solution, I sped up things first by `break`ing the
loop if the sum exceeds the target (there are no negative numbers!),
and then by having a running sum so that we must not always calculate
the sum of the previous numbers.

While writing the comment an idea sparked in my mind:
I could expand the running sum idea by also shrinking the interval
when it was too big so that it isn't necessary to start from
0 every time, but only shrinking until the running sum is bigger
than the target, then growing the interval again.

So i rewrote the `_fast()` method. You must pay attention to the order
in which you update the start/end index and the running sum:
if adding to the interval or removing from the interval!

## [Day 10](https://adventofcode.com/2020/day/10)

Part 1 done in 18 minutes and Part 2 in ?? minutes.

Part 2 is "??" because I've been interrupted and I think in reality
it was more something like 30 minutes of thinking/programming.

Part 1 is pretty straighforward: transform strins to numbers,
sort the list of adapters, compute the differences and count them in `r`.
Took more time than necessitate, because I sorted before transforming to
numbers... (1, 10, 11, ..., 100, ..., 199, 2, 20, ...)

Part 2 took also more time than needed because I struggled (and I still
haven't found) to find a way to calculate the ways you can arrange `n`
consecutive joltages. But after some time, I saw that at maximum we have 5
consecutive joltages and I counted them by hand and hard coded in `a`.
Then the algorithm just multiplies the `a` of the length of the consecutive
joltages.

## [Day 11](https://adventofcode.com/2020/day/11)

Part 1 completed in 41 minutes, Part 2 in 11,

For this puzzle I made a class `WaitingArea` that simulates... the 
waiting area!
Its methods are:

`seat(x, y)`
:  gives the status of the `(x, y)` position.

`occupied_neighbors(x, y)`
:  counts the occupied seats around the position `(x, y)`.
   Loops thru -1, 0, +1 for `dx` and `dy`, checks that it is not self,
   check that we are not out of the waiting area and counts
   the occupied seats it encounters.

`count_occupied()`
: gives the number of occupied seats in the waiting area

`step()`
: computes the next round. Creates a list `next_step` where we add
  the new computed status of the seats. At the end we set `floor` property
  to `next_step`. Also we keep track if something changes, so that we
  know when to stop iterating.

Almost the same for Part 2, but we use the `real_` methods.

`real_occupied_neighbors(x, y)`
:  now iterates thru the 8 directions `(-1, -1), (0, -1), ...` that are left-up
   up, right-up, ..., check if position is in waiting area, if it's a seat
   count if occupied, otherwise continue in the same direction.

Now it is a little slow, I think it's due to the use of strings in the
`floor` property of the class. If I find the time I'll try using only
lists. Or maybe a `dict`.

## [Day 12](https://adventofcode.com/2020/day/12)

Ok, 17 minutes for Part 1 and 12 for Part 2.

This has been fairls easy. I think I had no problems.

In Part 1, I created the class `Ship`, that has a `pos`ition and a 
`dir`ection, that are tuples with `x` and `y` coordinates (vectors).
I added a `char_to_dir` property to transform the `N`, 
`S`, `E` and `W` characters to vectors.
Then `turn_left()`,  `turn_right()` and `parse_command()` are self explanatory
(I think).
The `step()` method does the right action. It's all easy and enough clear,
maybe it is clearer if I rewrite it using vectors.

Part 2 is the same as Part1, only the methods are prefixed with `waypoint_`
and the is `waypoint` property.

After having found the solutions, I effectively rewrote it using a `Vector`
class. I don't know if it is clearer. I moved the Vector class to the
'tools.py' file, because it could come handy in the future.

## [Day 13](https://adventofcode.com/2020/day/13)

Day 13 Part 2 has been tough... Part 1 done in 17 minutes, Part 2 in
8... hours! I reality after 2 hours I got interrupted (relatives), and
it took me about 30 minutes to get to the solution after the interruption.

Part 1 is relatively easy: once you see that for each bus `line`, the departure
after the `after` timestamp is `departure = ((after // line) + 1) * line`,
you just check which line comes first after `after`.

Part 2 is a bit more complicated: well... let me just say that my algorithm
works, but it is just by chance.
I wrote the `combine()` function that given two lines, finds, in my intentions,
a *virtual* line with ID and offset that respect the ID and offset
of the given lines. Then just `combine()` this line with the next.

The simple (and wrong) `combine()` version is this:


```
def combine(l1, l2):
    b1, d1 = l1
    b2, d2 = l2
    n1 = 1
    while True:
        t = n1 * b1 - d1
        if (t + d2) % b2 == 0:
                return b1 * b2, t
        n1 += 1
```

`l1` and `l2` are the tuples with bus ID and wanted delay for two bus lines.
We compute every *good* starting timestamp for `l1` with:
`t = n1 * b1 - d1` and check if it is good also for line `l2`.
If it's good, return the *virtual* bus ID and delay.

The problem is that it is not the returned *virtual* line: the formula to find the
timestamp (`ts = l[0] + n * l[1]`).
Then I played with modulo / + / - / ... to find the right result.

I have to find the **right** way to do it.

Ok this is the (more) correct way to do it:

```
def combine(l1, l2):
    # Here is the bus line data
    b1, o1 = l1
    b2, o2 = l2

    # Find the d: instead of advancing from the timestamp to the
    # departure time, we advance from the previous departure time to
    # timestamp   (n-1)th depart. <--d-->  T <--o-->  n-th departure
    d1 = b1 - o1
    d2 = b2 - o2

    n1 = 1
    while True:

        # Compute the n-th timestamp
        t = n1 * b1 + d1

        # Check if the timestamp also works for line l2
        if (t + d2) % b2 == 0:

            # Compute the virtual line data:
            b3 = b1 * b2      # I think it shoud be gcm(b1, b2), but b's are prime

            # Go back form d to o
            n3 = t // b3 + 1 
            o3 = b3 * n3 - t
            return b3, o3
        n1 += 1
```

