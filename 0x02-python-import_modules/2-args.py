import sys

# Get the command-line arguments
arguments = sys.argv[1:]

# Calculate the number of arguments
num_args = len(arguments)

# Print the number of arguments and their values
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print(f"1: {arguments[0]}")
else:
    print(f"{num_args} arguments:")
    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")
