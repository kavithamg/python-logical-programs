# using native method to remove duplicated  from list
def rem_dup_arr(elements):
    res = []
    for i in elements:
        if i not in res:
            res.append(i)
    return res

# using list comprehension to remove duplicated  from list
def rem_dup_list_comp(elements):
    res = []
    [res.append(i) for i in elements if i not in res]
    return res

if __name__ == '__main__':
    n = int(input("Enter number of elements : "))
    my_list = []
    for i in range(0, n):
        val = int(input("Enter element: "))
        my_list.append(val)

    result = rem_dup_arr(my_list)
    print(f"The original list is: {my_list}")
    print(f"The list after removing duplicates: {result}")