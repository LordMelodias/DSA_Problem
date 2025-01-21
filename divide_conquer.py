def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2

        # Split the array into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        # Merging process
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Test the function
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)



'''
Divide and Conquer Technique (Merge Sort Example)
Definition: A method to solve problems by dividing them into smaller sub-problems, solving them independently, and combining their solutions.
Objective: Efficiently solve problems by breaking them down recursively.
Diagram:
css
Copy
Edit
[38, 27, 43, 3, 9, 82, 10]
     /               \
[38, 27, 43]    [3, 9, 82, 10]
   /   \          ...
'''