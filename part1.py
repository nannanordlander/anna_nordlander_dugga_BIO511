# Part 1 of dugga -- Loop and If/else

# Create list of input data: 
numbers = [15, -5, -12, 7, 10, 7, 10, -7, 3, -10, 4]

# task 1a: Identify all numbers with an absolute value greater than 10 and print the sum of those numbers.
sum_abs_above_10 = 0 # making a variable to hold the sum
for n in numbers: # loop through each number in the list
    if abs(n) > 10: # check if the absolute value of the number is greater than 10
        sum_abs_above_10 += n # if it is, add it to the sum
    else: 
        pass # if not, do not add it to the sum
print("The sum of numbers with absolute value greater than 10 is:", sum_abs_above_10)

# task 1b: Build and print a list of the cubes (n^3) of all negative numbers in numbers. 
cubes_neg = [] # making an empty list to hold the cubes
for n in numbers: # loop through each number in the list
    if n < 0: # check if the number is negative
        cubes_neg.append(n ** 3) # if it is, calculate its cube and add it to the list
    else: 
        pass # if not, do not add it to the list
print("The cubes of all negative numbers are:", cubes_neg)

# task 1c: Scan left-to-right and print the first repeated absolute value (treat x and -x as the same); if none, print "No duplicates". 
seen = [] # making an empty list to hold the seen absolute values
first_dup = None # variable to hold the first duplicate
for n in numbers: # loop through each number in the list
    abs_n = abs(n) # get the absolute value of the number
    if abs_n in seen: # check if the absolute value has been seen before
        first_dup = abs_n # if it has, set it as the first duplicate
        break # exit the loop
    else: 
        seen.append(abs_n) # if not, add it to the seen list.
print("The first repeated absolute value is:", first_dup if first_dup is not None else "No repeats") # print the result if first_dup has been found






