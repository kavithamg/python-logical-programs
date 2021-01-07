def cnt_vow_cnt(data):
    vowels = 0
    consonants = 0
    specialChar = 0
    digit = 0
    for i in data:
        if ( (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') ):
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                vowels += 1
            else:
                consonants += 1
        elif (i >= '0' and i <= '9'):
            digit += 1
        else:
            specialChar += 1

    print("Vowels:", vowels)
    print("Consonant:", consonants)
    print("Digit:", digit)
    print("Special Character:", specialChar)

if __name__ == '__main__':
    data = input("Enter your string: ")
    cnt_vow_cnt(data)