# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100:
n = 0
for i in range(0,101):
  if i % 2 == 0:
    n += i
print(f"A soma dos números páres entre 1 e 100: {n}")
