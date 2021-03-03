def vowel():
    f = open('myFile.txt', 'r')
    lines = f.readlines()
    vowel_count = ''
    for i in lines:
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' \
                or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U':
            vowel_count += ("'" + i + "'" + "It is start with vowels'\n")
    print(vowel_count)


vowel()


