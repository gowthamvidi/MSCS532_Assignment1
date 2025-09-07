
# Initializing Array
random_array = [19, 99, 53, 25, 46] 

# logic to sort array
for i in range(1, len(random_array)):
        temp = random_array[i]
        j = i - 1
        while j >= 0 and random_array[j] < temp:
            random_array[j + 1] = random_array[j]
            j = j - 1

        random_array[j + 1] = temp    
