file = open("myFile.txt", "r")

str = file.read()

vowel_count = ''
for word in str:
    # if (i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
    if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
        vowel_count += ("'" + word + "'")
        vowel_count += 'start with a vowel\n'

print(vowel_count)
file.close()