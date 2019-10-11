#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The following snippet of pseudocode has a runtime of `O(n^3)`.

```python
    a = 0
    while (a < n * n * n):
      a = a + n * n
```

### Justification

The input in this snippet of pseudocode is n. For every value of n passed to the pseudocode, the while loop executes `n * n * n` times (which is equal to n^3). For input of size 2, the loop runs 2 * 2 * 2 times which is equal to 8 times (2^3); for input of size 3, it runs 3 * 3 * 3 times which is equal to 27 times (3^3).
Inside this loop, only one operation is performed. The runtime for the snippet can therefore be said to be `cubic`.

b) The snippet of code below has a runtime of `O(n log n)`. It is a `Logarithmic runtime`.

```
   sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

### Justification
The input in this pseudocode is n. When the snippet executes, the first for loop iterates `n` times and so we have O(n) for the for loop only. For every one of the n iterations, the while loop also runs. But unlike the outer for loop it only runs for fractions of the number of times making the runtime `Logarithmic`.


c)

## Exercise II
