# Array Sum HackerRank Challenge

Here is my solution and explanation for the [Array Sum Challenge](https://www.hackerrank.com/challenges/simple-array-sum).

## The Challenge

The prompt is very straightforward, and what we have is:

```
Print the sum of the array's elements as a single integer.
```

## The Solution

All we have to do is add together all of the elements of an array.  This can be done as follows:

```
def simpleArraySum(n, ar):
    numbers=0
    answer = sum([int(i) + numbers for i in ar])
    return answer
```

Our sum method takes in the number of elements in the array as n and the array as ar. We define a variable `numbers` as 0. Then our `answer` is the sum the integer of a given element in ar added to our `numbers` variable.  So we add together each element as we land on it.  