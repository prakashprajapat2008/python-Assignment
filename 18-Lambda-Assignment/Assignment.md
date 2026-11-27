# Python Assignment: Lambda Functions


**Total Questions:** 10

## Instructions

-   Solve every question using a `lambda` function.
-   Use `print()` to display the result.
-   Do not use a regular function (`def`) to solve these questions.
-   Use the given sample values first. You may try your own values after
    that.

------------------------------------------------------------------------

## Questions

### 1. Add Two Numbers

Create a lambda function that accepts two numbers and returns their sum.

**Sample values:** `10`, `20`\
**Expected output:** `30`

**Your output:**

```python 
add = lambda a, b: a + b
print(add(10, 20))

=>

30

 ```


### 2. Find the Square

Create a lambda function that accepts one number and returns its square.

**Sample value:** `6`\
**Expected output:** `36`

**Your output:**

```python 
add = lambda a: a * a
print(add(6))

=>

36

 ```

 
### 3. Find the Cube

Create a lambda function that accepts one number and returns its cube.

**Sample value:** `3`\
**Expected output:** `27`

**Your output:**

```python 
add = lambda a: a ** a
print(add(3))

=>

27

 ```


### 4. Check Even or Odd

Create a lambda function that accepts a number and returns `"Even"` if
the number is even, otherwise returns `"Odd"`.

**Sample value:** `7`\
**Expected output:** `"Odd"`

**Your output:**

```python 
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(7))

=>

"Odd"

 ```


### 5. Find the Greater Number

Create a lambda function that accepts two numbers and returns the
greater number.

**Sample values:** `45`, `32`\
**Expected output:** `45`

**Your output:**

```python 
greater = lambda a, b: a if a > b else b
print(greater(45, 32))

=>

45

 ```


### 6. Convert Celsius to Fahrenheit

Create a lambda function that accepts a temperature in Celsius and
converts it to Fahrenheit.

Use this formula:

`Fahrenheit = (Celsius * 9/5) + 32`

**Sample value:** `25`\
**Expected output:** `77.0`

**Your output:**

```python 
convert = lambda c: (c * 9/5) + 32
print(convert(25))

=>

77.0

 ```


### 7. Calculate the Length of a String

Create a lambda function that accepts a string and returns the number of
characters in it.

**Sample value:** `"Python"`\
**Expected output:** `6`

**Your output:**

```python 


=>



 ```


### 8. Convert a String to Uppercase

Create a lambda function that accepts a string and returns the string in
uppercase.

**Sample value:** `"hello world"`\
**Expected output:** `"HELLO WORLD"`

**Your output:**

```python 
uppercase = lambda text: text.upper()
print(uppercase("hello world"))

=>

"HELLO WORLD"

 ```


### 9. Find the Last Character

Create a lambda function that accepts a non-empty string and returns its
last character.

**Sample value:** `"Coding"`\
**Expected output:** `"g"`

**Your output:**

```python 


=>



 ```


### 10. Calculate the Final Price

Create a lambda function that accepts the original price and discount
percentage. Return the final price after applying the discount.

**Formula:**

`Final Price = Original Price - (Original Price * Discount / 100)`

**Sample values:** Original price = `1000`, Discount = `10`\
**Expected output:** `900.0`

------------------------------------------------------------------------

## Bonus Practice

Try solving Questions 1--10 again with different input values. Check
whether your lambda functions work correctly for those values too.
