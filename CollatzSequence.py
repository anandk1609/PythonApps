def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print("Enter number:")
num = int(input())

while num != 1:
    print(num)
    num = collatz(num)

print(num)