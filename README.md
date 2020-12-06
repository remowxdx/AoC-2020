# Advent of Code 2020

These are my attempts to solve the [Advent of Code 2020](https://adventofcode.com/2020).

## [Day 1](https://adventofcode.com/2020/day/1)

OK, day 1 has been easy, 7 minutes to do part 1 and other 4 to do part 2.

The puzzles asked to find in a list of number two (or three) numbers that
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
Also this solutions doesn't worry about taking the same number more than
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
adn stop the recursion once we get over 2020 (or below 0).

## [Day 2](https://adventofcode.com/2020/day/2)

This problem took me longer that it should have: 24 minutes for part 1 and
other 28 minutes for part 2.
The problem was easy to solve, but I made some mistakes in the parsing
of the strings... and reading the wording of the problem:

- it took me too much time to parse the policy part of the input
- I didn't realized that I left a space at the start of the password, thus
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

After finding the solutions I didn't what to do to make something different.
After some thinking I decided to make the function `count_trees` parallel.
Also here nothing spectacular: now `count_trees` goes line by line updating
the tree count for each slope. The counting is done only if
`y % (down of slope)` is `0`.

## [Day 4](https://adventofcode.com/2020/day/4)

Part 1 took 25 minutes, Part 2 32.
This are the kind of problems which I like less: much parsing and many rules.
The implementation straightforward: parse the passports in a list of
dicts (Maps) and then check that they have "all" required fields for part 1.
And also check that the field's values are valid for part 2.
As always I had problems parsing the strings...

For part 2 I decided to not use regular expression, so I worked with only
standard string method.

After finding the solution, I changed the function to check the validity
of the field to use regular expressions. 
I created dict with the field as index, and a tuple with the regular
expression and the limits of the values.
Looking at it, I don't know which method I like more...

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

So the problem is *really* easy to solve: just transform the binary
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

