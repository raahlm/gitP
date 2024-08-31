names = ['fatima', 'r', 'usman', 'r']
occurrences = [i for i, x in enumerate(names) if x == 'r']

# Get the index of the second occurrence
second_r_index = occurrences[1] if len(occurrences) > 1 else None

print(second_r_index)

