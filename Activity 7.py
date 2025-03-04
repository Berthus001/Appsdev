User_Input = input("Enter a string: ")
substring_counter =  input("Enter the substring to find: ")
index = User_Input.find(substring_counter)

if index !=-1:
    print(f"The substring \'{substring_counter}\' is found at the  {index}")
else:
    print("The substring is not found in the index")