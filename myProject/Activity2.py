number = int(input("Enter a number: "))
OriginalNumber = number
result = 0
Number_digit = len(str(number))
for digit in range(Number_digit):
    remainder = OriginalNumber % 10
    result += remainder ** Number_digit
    OriginalNumber //= 10
    continue

if result == number:
        print(f"{number} is an armstrong")
else:
    print(f"{number} is not an armstrong")