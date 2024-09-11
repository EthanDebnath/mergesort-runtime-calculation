def recursiveMergeSort(inputList):
    if len(inputList) > 1:
        middleIndex = len(inputList) // 2  # Locate midpoint of the list
        leftSegment = inputList[:middleIndex]  # Split the list into left
        rightSegment = inputList[middleIndex:]  # and right segments

        recursiveMergeSort(leftSegment)  # Recursively sort the left segment
        recursiveMergeSort(rightSegment)  # Recursively sort the right segment

        leftPointer = rightPointer = mergedPointer = 0

        # Merge the sorted segments
        while leftPointer < len(leftSegment) and rightPointer < len(rightSegment):
            if leftSegment[leftPointer] < rightSegment[rightPointer]:
                inputList[mergedPointer] = leftSegment[leftPointer]
                leftPointer += 1
            else:
                inputList[mergedPointer] = rightSegment[rightPointer]
                rightPointer += 1
            mergedPointer += 1

        # Append remaining elements from the left segment, if any
        while leftPointer < len(leftSegment):
            inputList[mergedPointer] = leftSegment[leftPointer]
            leftPointer += 1
            mergedPointer += 1

        # Append remaining elements from the right segment, if any
        while rightPointer < len(rightSegment):
            inputList[mergedPointer] = rightSegment[rightPointer]
            rightPointer += 1
            mergedPointer += 1

# Test the recursive merge sort function
testList = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original list:", testList)
recursiveMergeSort(testList)
print("Sorted list:", testList)
