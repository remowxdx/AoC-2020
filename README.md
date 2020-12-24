# Advent of Code 2020

These are my attempts to solve the [Advent of Code 2020](https://adventofcode.com/2020).

## [Day 1](https://adventofcode.com/2020/day/1)

OK, day 1 has been easy, 7 minutes to do part 1 and other 4 to do part 2.

The puzzle asked to find in a list of number two (or three) numbers that
added together give the result of *2020*.

For the first solution I simply ran two (or three) nested loops over the data
and checked if the result was 2020.

```py
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


```py
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

```py
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

```py
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

```py
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


```py
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

```py
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

## [Day 14](https://adventofcode.com/2020/day/14)

Part 1 done in 35 minutes, Part 2 in 21. I thought it would have taken me
less time to solve this puzzle...

This puzzle likes bitwise operations. I created a class `Memory` that
implements the operations described in the puzzle:

- `set_mask()` that sets the mask
- `set_mem()` that sets the memory applying the mask.
- `exec()` just interpret the input execute the right `set_` operation.

To set the n-th bit to 1 of `value`, we bitwise "or" the value with a number
that is all `0`s except the n-th that is a `1`.

To set the n-th bit to 0 of `value`, we bitwise "and" the value with a number
that is all `1`s except the n-th that is a `0`.
To find that number, we have to compute a number with all `1` (36 `1`) and
"xor" it with the number that is all `0`s except the n-th that is a `1`.

For Part 2, the mask is divided into three lists with the index of the `0` bit,
`1` bit and `X` bit.
Then in the address the bits that are `1` in the mask, are set to `1` .
Then with the *floating* bits we recursively set those address bits to `1` and `0`,
and write to the memory addresses.

## [Day 15](https://adventofcode.com/2020/day/15)

Ok, Part 1 in 32 minutes, Part 2 in 11 minutes.

For this puzzle, I simply coded the rules and let the program go to the
end: for Part 1 and also for Part 2.

The "difficult" part was to keep track of the previous element
(`prev` and `is_new`) before updating it, in the `numbers` dict.

In Part 2 the computation took a bit of time, but not too much.
I think I'll find a way to do it faster... if there is such a way.

... and I still haven't find a faster way...

## [Day 16](https://adventofcode.com/2020/day/16)

Well, 36 minutes for Part 1 and 1 hour and 14 minutes for Part 2.
This puzzle made me sweat!

Part 1 has not given me particular problems, as always the toughest part has
been to parse the input.
Really I should find something better than `split`ting strings.

From the input, I built a `dict` containing:

- `rules` as a `dict` that has as keys the field name and as values a list of pairs
of numbers that are the limits of the intervals,
- `my ticket` as a list of values and
- `nearby tickets` as a list of lists of values

Then the functions:

- `in_interval()` that returns if a `value` is in the given `interval`
- `in_one_interval()` that say if the `value` is in at least one of the `intervals` given
- `validates_one_rule()` that says if the value validates at least one of the
given `rules`
- `get_invalid_values()` that returns the invalid values in the given `ticket`.

Then Part 1 is only a matter of chaining together the invalid values
of all the tickets.

Then comes **Part 2**!

Eventually it is not so difficult, but I started towards a path that was
very inefficient and full of little details that I couldn't all right.

Then I found the *right way*:

- First create a list of valid ticket, i.e. ticket that do not have the invalid
value of Part 1.
- Then build a list which for each numerical field (in the order of the tickets)
has all the named fields (from the rules)
- Then loop thru all numerical field indexes, analysing every rule for every 
ticket. If we find that the rule is invalid for a ticket, remove that named
field from the possible fields for that numerical field.
- At last loop thru the possible fields, if for a numerical field there is only
one possible named field, remove that named field from all the other numerical
field possibilities.

That shoud live you with the named field for each numerical field.

Multiply the value of our ticket where the named field starts with 'departure'
and we are done.


## [Day 17](https://adventofcode.com/2020/day/17)

Today 49 minutes for Part 1 and 9 minutes for Part 2.

Also for today I wrote a `class` for the dimensional `Pocket`:
it contains a python `set()` that keeps track of the active cubes.
A cube is a 3-tuple with its own coordinates.

In the constructor I set all cubes as inactive and parse the input to activate
the starting cubes.
I also generate the directions to the neighbors.

The `activate()` and `deactivate()` methods are self explanatory and simply
add resp. remove the tuple from the set of active cubes.
Similarly the `is_active()` method checks if the coordinates tuple is
in the set of active cubes.

The `count_active()` method gives the count of active cubes, that is 
the size of the set of active cubes.
`count_neighbors()` count the active neighbors of the given cube, using
the directions generated in the constructor (`dirs`).

`find_limits()` (or `bounding_box()` in the general version) returns a
list with the minimum and maximum coordinates of the
active cubes, it is the "bounding box" of the active cubes.

Finally the `cycle()` method does the work: it cycles through all the cubes
inside the bounding box and 1 further, counting the neighbors and
putting the coordinates in the `activate` or `deactivate` lists.

At the end cubes in the `activate` list are activated and those in the
`deactivate` list are deactivated.

To get the result we simply `cycle()` 6 times and count the active cubes.

For Part 2, I copied the `Pocket` class to an `HyperPocket` class
and "simply" added a fourth `w` coordinate everywhere.

After finding the solutions, I generalized the `Pocket` class, so
that now it takes an argument that gives the dimensions of the
energy grid.

Also now the `cycle()` method doesn't loop through all the cubes in the
bounding box (hopefully), but only through the neighbors of the active
cubes. And the active cubes themselves.

Still missing is the `__str()__` protocol.


## [Day 18](https://adventofcode.com/2020/day/18)

1 hour and 15 minutes and I don't know how much for Part2... I fell asleep
while doing Part 2!

It took me some time to realize how should the `evaluate` work. I
came many times near the right solution, always missing it.

At the end it works mostly like a calculator.
It reads the next character, keeps track of the last inserted number
(`prev_value`) and as it encounters an operation, it evaluates it as
soon as it has the next value.

But if there is an "`(`", we save the current `value` in a stack, evaluate to
the matching "`)`", pop the previous value from the stack and evaluate
the operation.

For Part 2, it's similar, but more complicated: we evaluate only the `+`
opreation, because the `*` operation and value are pushed on the stack and
will be evaluated only at the end (of the `line` or of the "`)`").
That is to respect the precedence.

And now the stack is really a stack of stack, with every stack containing a
stack for the values for the `*` operations to do at the end, instead of 
having only the value computed so far.


## [Day 19](https://adventofcode.com/2020/day/19)

Another long puzzle: 1 hour and 45 minutes for Part 1, and 25 minutes for
Part 2.

This was another parsing/evaluating puzzle, like the previous.
I already said that I have to find another way to parse the input:
maybe it has been done to help me! ;)

Part 1 took much time, because I suspect that
I implented the *significantly more difficult* way warned in Part 2.

Anyway, I parsed the `rules` in a `dict`, every rule is:

- the name of (another) rule
- a tuple that has as first member the type of the rule (`char`, `and`, `or`)
followed by:
  - a character ("`a`" or "`b`" if type is `char`) or
  - one or more subrules, e. g.  `('or', '42', ('and', '42', '8'))`

`and` rules are those that must be all matched in sequence, `or` rule are
those that at least one has to match.

Then there is the `check()` function that does the checking:
it takes the `message`, the `rule` to be matched and the set of `rules`.
It returns a list that says how many character have been matched.
E. g. if it returns `[3, 5]`, it means that under some `or` rules 3 characters of
the message are matched instead under some other `or` rule 5 character are matched.

If it doesn't match returns the empty list (`[]`).

```py
def check(message, rule, rules):
    # Check if we are still in the message
    if len(message) == 0:
        return []
        
    # If rule is not a tuple, it is a rule name:
    # Check that named rule!
    if type(rule) != tuple:
        return check(message, rules[rule], rules)

    # print('Check', message, rule) # Debugging

    # If rule is a character, check if it correspond with what
    # is in the message. If ok return that we have matched one character
    if rule[0] == 'char':
        if message[0] == rule[1]:
            return [1]
        # Character doesn't match
        return []

    # We must match all the rules in sequence:
    if rule[0] == 'and':
        s = []  # This will be the return list
        # Check if first rule matches
        r1 = check(message, rule[1], rules)

        # Build a sub rule for the rest of the sequence
        if len(rule) > 2:
            subrule = ('and', *list(rule[2:]))
            # print(subrule)  # Debugging !

            # This was the hardest part to figure out!
            # For every matched length of the first rule, add every
            # matched length of the remaining rule of the sequence
            for l1 in r1:
                # Check if the sub rule matches
                rn = check(message[l1:], subrule, rules)
                # For all l1 add every ln
                for ln in rn:
                    s.append(l1 + ln)
        else:
        # The sequence has only one case (i. e. is not a sequence)
            s = r1
        return s

    # We must match at least one rule in the list:
    if rule[0] == 'or':
        r = []
        # For every rule in the list...
        for i in range(1, len(rule)):
            # ... simply add all the matched length to the result
            r.extend(check(message, rule[i], rules))
        return r

```

With this done, Part 2 is easy: just `update_rules()` as said
and `count` the valid messages.

I have had also some problems at the end, because for Part 2
we can have that the message matches multiple lenghts.
We must accept the result if at least one of the matched length
is equal to the length of the message.


## [Day 20](https://adventofcode.com/2020/day/20)

Well, another hard puzzle, at least for me.
54 minutes for Part 1, and at least 2 hours and a half for Part 2.
I think this was the longest program to solve a puzzle.

The idea here is to build a dict of the tiles (`get_tiles()`), indexed by the tile number.
Every tile has a `raw` image corresponding to the input and an `img` image
without the borders (for Part 2).

Then we build (`get_borders()`) another dict, indexed by the `minimum` of a tuple
with the border transformed to two numbers, by treating it as a binary
digit, with "`#`" meaning `1` and "`.`" meaning 0, and the corresponding
flipped number (implemented in `pixels_to_num()`).
While computing the borders, we add to the corresponding tile the `top`,
`left`, `bottom` and `right` borders.

In Part 1 I *"simply"* find which tiles are at the border of the whole
image, by checking to how many tiles each tile border matches.
If it is only one, we are on the image border. Then to find the
corner, we find the tiles that have two external borders.

For Part 2 much of the work went into implementing functions to
rotate and flip tiles, by rotating and flipping images (`img`) and borders.
Also be aware that when we rotate or flip borders, some of the tuples that
represent the borders have to be swapped.

Also much work went in the `build_image()` function, that analyses the tiles
and stitches them togheter, by rotating and flipping them as needed:

1. The process starts from a corner tile, we find the tile with a border 
corresponding to the corner right border.
2. By rotating the new tile, we move that border on the left.
3. If the border are not in the same direction, we flip the tile vertically
4. We add the tile to the image. And continue to the next tile in the row.
5. At the end of the row, we start a new row by finding a tile with a border that
correspond to the bottom border of the first tile of the previous row.
6. Again by rotating and flipping, we move that border on the top and add the tile
to the image.
7. We continue to the end of the image.

Then we check for monster in the image. We analyse every pixel of the image
to see if it correspond to the monster. If not we rotate/flip the image,
until we find some monster.

Finally we count the "`#`" in the image.


## [Day 21](https://adventofcode.com/2020/day/21)

Today 1 hour and 12 minutes for Part 1 and 12 minutes for Part 2.

At the beginning I struggled to understand the description of the puzzle:
I couldn't make up my mind around the problem.
Then I "clicked"... I saw what was meant and how to solve the problem.

The trick is to find for each food which ingredients aren't contained.
Those ingredients can not possibly contain the food's allergens.

While parsing the puzzle input, I built the list of ingredients, the list
of allergens the list of food with the ingredients and the allergens that
it contains.

Then we go food for food and add the list of ingredients that it
doesn't contain.
With that list, we remove from the allergens of the food, the ingredients
that are not in that food.

It's not easy to understand (for me) and it's harder to explain...

Then we search the allergens list for allergen that can be
in only one ingredients, remove that ingredient from the other allergens
and save it in the `definitive` dict.

From there we go through the list of ingredients, and if they are not
in the allergens list, we count how many times they come up
in the food list.

For Part 2, we sort the "inverted" dict (dict with keys and values swapped),
and join the ingredients.


## [Day 22](https://adventofcode.com/2020/day/22)

It took me 20 minutes for Part 1 and, 2 hours and 20 minutes for
Part 2, dinner included.

Here I *simply* (I really like this word!) simulated the game
using a list of two list to simulate my and the crab's deck.
Part 1 is straightforward, but Part 2 gave me some headache:
I didn't understand what game meant in relation with the first
rule of *Recursive Combat*.
I included sub games in the main game: all the decks combinations
went into the same
history, so that meant that if two different sub games
had the same card configuration, it counted as already played
and made player 1 the winner.

But the right way was to have the decks history only matter
for the current playing sub game.

Once understood that, the solution was found.


## [Day 23](https://adventofcode.com/2020/day/23)

51 minutes for Part 1 and, well... ehm... 2 hours and something
for Part 2.

I solved Part 1 with the `Cup` and `Cups` classes, I implemented
a beautiful linked list in python, with that fantastic
circular disposition. And it worked great!

But then Part 2... the linked list is *somewhat* inefficient:
to find the `current - 1` cup, it had to search through the
whole *one million* long circular linked list of cups, and
it would have taken 39 day to get to the solution.

So after spending too much time to try to find a way to
predict the positions of the cups without simulating all
of the steps, I finally implemented it with a dict, which has
the cup values as keys and the next cup as value.

The algorithm is the same, but finding the `current - 1` cup
is way faster.


## [Day 24](https://adventofcode.com/2020/day/24)

Today 28 minutes for Part 1 and 23 for Part 2.

This puzzle has gone almost painless, only at the start I had to 
think a little on the way to follow.

And the way is this: we simply compute for every tile the coordinates of the center,
looking at the tiles, we see that they are organized in rows that are
alternating, i. e. the center of a tile
of a row is aligned with the border of the tiles of the rows above and below.

The `x` (or `e`) is increased by `2` while going `e` and increased by `1`
while going `ne` or `se`, and decreased accordingly for the west-directions.

The `y` (or `n`) is increased by `1` while going `ne` or `nw` and
decreased by `1` while going `se` or `sw`.

In reality the tiles are a little vertically stretched, because the
(euclidean) `y` should be &#8730;3.

Flipping means adding or removing the tile from the set of black `tiles`.

For Part 2, for every day we go through the set of black `tiles`, counting
the black neighbors and adding the neighboring white tiles to the set of
white tiles. If the flipping rules apply, we add the tile to the tiles to flip.

Then we go through the white tiles set, basically doing the same as above:
counting the black neighbors and adding to tiles to flip if the rules apply.

Finally we effectively flip the tiles that have to be flipped.


