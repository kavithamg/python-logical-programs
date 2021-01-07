def rem_char_str(data, char_data):
    val = ''
    for i in data:
        if i != char_data:
            val = val + i
    return val

if __name__ == '__main__':
    data = input("Enter your string: ")
    char_data = input("Enter your character to remove from your string: ")
    print(f"The original string is: {data}")
    print(f"The string after removing character: {rem_char_str(data, char_data)}")