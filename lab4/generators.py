#1
def generate_squares(n):
    for i in range(1, n+1):
        if i**2 <= n:
            yield i**2
n = int(input())
squares = generate_squares(n)

for square in squares:
    print(square, end=" ")

#2
def even_generator(n):
    for i in range(1, n):
        if i%2 == 0:
            yield i
n = int(input())
evens = even_generator(n)
for even in evens:
    print(even, end=" ")

#3
def divisiblse_generator(n):
        for i in range(1, n):
            if i%3 == 0 or i%4 == 0:
                yield i
n = int(input())
divs = divisiblse_generator(n)
for div in divs:
    print(div, end= " ")

#4
def generate_squares(a,b):
    for i in range(1, b+1):
        if i**2 <= b and i ** 2 >= a:
            yield i**2

a,b = map(int, input().split())
squares = generate_squares(a,b)

for square in squares:
    print(square, end=" ")

#5
def reverse(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
revs = reverse(n)
for rev in revs:
    print(rev, end=" ")
