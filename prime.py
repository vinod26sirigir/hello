# Take input from the user
num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Check for factors from 2 up to num - 1
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        # If the loop finishes without finding a factor
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
