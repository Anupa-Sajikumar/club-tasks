n, m, a = map(int, input().split())
if m % a == 0:
    x = m // a
else:
    x = m // a + 1
if n % a == 0:
    y = n // a
else:
    y = n // a + 1
print(x * y)