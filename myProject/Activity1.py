lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))
print(f"Prime numbers between {lower_bound} and {upper_bound} are: ")

for number in range(lower_bound, upper_bound + 1):
    if number < 2:
        continue
    if not any(number % i == 0 for i in range(2, int(number ** 0.5) + 1)):
        print(number)
