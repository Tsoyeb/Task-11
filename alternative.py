# This program will make each alternate character or word an uppercase string or a lower case string.

user_string = input('Please enter a word/sentence of your choice: ')
choice = input('Do you wish to make every other character capital or every word? type Y for character or any key for word: ')
words= user_string.split() 
result=''

# This code will make every 2nd character lowercase
if choice.lower()== 'y':
    for word in words:
        pos = 0
        for c in word:
            if(pos + 1) % 2 == 0:
                result += c.lower()
            else:
                result += c.upper()
            pos += 1
        result +=' '
    
    print(result)

# This code will make every 2nd word lowercase
else:
    for i in range(0,len(words)):
        if (i + 1) % 2== 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()

    print(' '.join(words))




