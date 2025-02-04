# Taking input
input_list = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))

subarrays = []

# Iterate through all possible subarrays of length 3
for i in range(len(input_list) - 2): # Ensure we have at least 3 elements
 subarray = input_list[i:i + 3] # Extract subarray of length 3
 if sum(subarray) == target:
  subarrays.append(subarray)

# Display the results
print("Valid subarrays of length 3 with the target sum:",subarrays)