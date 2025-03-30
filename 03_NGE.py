def next_greater_element(arr):
    n = len(arr)  # Length of the input array
    result = [-1] * n  # Initialize the result array with -1 for all elements
    stack = []  # Stack to keep track of indices of elements

    # Iterate through the array from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements from the stack that are smaller or equal to the current element
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # If the stack is not empty, the top element is the next greater element
        if stack:
            result[i] = arr[stack[-1]]
        
        # Push the current index onto the stack
        stack.append(i)

    return result

# Example Usage
if __name__ == "__main__":
    # Input array provided by the user
    arr = [4, 5, 2, 25, 7]
    print("Input Array:", arr)
    print("Next Greater Element:", next_greater_element(arr))


