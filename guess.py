from random import randint

# Initialize total and num_additions to 0
total = 0
num_additions = 0

# Creating a while loop with a condition of total <= 1000
while total <= 1000:
    # Calling randint to get a random number between 1 and 10
    rand_num = randint(1, 10)
    # Adding the random number to the total
    total += rand_num
    # Increment the count by 1
    num_additions += 1
    # Display the total and the count
    print("Total:", total)
    print("Number of additions:", num_additions)

# Display
print("Done!")