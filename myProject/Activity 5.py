def check_palindrome(num):
    str_num = str(num)
    reverse_str = str_num[::-1]

    if str_num == reverse_str:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not a palindrome")

num = int(input("Enter a number: "))
check_palindrome(num)
