def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
    return elements

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    my_list = []
    for i in range(0,n):
        val = int(input("Enter element: "))
        my_list.append(val)

    # num = input("Enter number of elements: ")
    # data = map(int, num.split(','))
    # print(list(data))

    print(f"The original list is: {my_list}")
    result = bubble_sort(my_list)
    print(f"The smallest elements is: {result[0]}, The largest elements is: {result[-1]} ")