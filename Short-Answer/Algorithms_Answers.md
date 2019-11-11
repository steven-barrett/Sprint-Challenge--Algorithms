#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python  altogether ((O(n^4)))  time complexity
    a = 0 # O(1)
    while (a < n * n * n): #(O(n^3))
      a = a + n * n  # (O(n^1))
```

b)

```Altogether its O(n^2) time complexity
    sum = 0 (O(1))
    for i in range(n):  (O(n))
      j = 1   Order 1
      while j < n: (O(n))
        j *= 2   (O(1))
        sum += 1 (O(1))
```

c)

```Altogether O(n) time complexity
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

f = n-story divided by 2 to start mid way to test the egg drop. EggDrop(f) if the egg breaks we reduce f by 1 and try again until the egg doesn't break. If it doesn't break
on the initial drop we increase f by 1 until it does break. At the end we know exactly what f is when the egg breaks. (???How do we determine when an egg breaks???)

I think the time complexity is O(n) as it depends on how many stories (n-story) that gets passed in
