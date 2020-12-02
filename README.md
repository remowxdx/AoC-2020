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

