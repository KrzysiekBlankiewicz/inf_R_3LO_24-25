numbers = [9,8,7,6,5,4,3,2,1,0]

def bubble_sort(numbers):
    for elem in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                v = numbers[i+1]
                numbers[i+1] = numbers[i]
                numbers[i] = v
    return numbers

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        elem = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > elem:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = elem
    return numbers

def quick_sort(numbers):
    if len(numbers) == 1:
        return numbers
    pivot = numbers[0]
    left = []
    right = []
    for elem in numbers:
        if elem >= pivot:
            right.append(elem)
        else:
            left.append(elem)
            
    return quick_sort(left) + quick_sort(right)


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def selection_sort(numbers):
    numbers = numbers.copy()
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

def bucket_sort(numbers):
    numbers = numbers.copy()
    bucket_count = len(numbers)
    mini, maxi = min(numbers), max(numbers)
    bucket_range = (maxi - mini) / bucket_count + 1
    buckets = [[] for _ in range(bucket_count)]
    for i in numbers:
        buckets[int((i - mini) / bucket_range)].append(i)
    numbers.clear()
    for j in buckets:
        j.sort()
        numbers += j
    return numbers

