def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
    return elements

# you can use this to sort if elements are already in sorted format
def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
            if not swapped:
                break
    return elements

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    my_list = []
    for i in range(0,n):
        val = int(input("Enter element: "))
        my_list.append(val)

    print(f"The original list is: {my_list}")
    result = bubble_sort(my_list)
    print(f"The list after sorting with bubble sort method:{result}")