def makeforming(string):
    string = string.lower()
    vowel = ['a','e','i','o','u']
    consonant = ['c for c in letter if c not in vowel']
    exception = ['be','see','flee','knee','lie']

    if string.endswith('e'):
        if string in exception:
            return string + 'ing'
        else:
            string = string [:-1]
            return string + 'ing'

    elif string.endswith(('ie')):
        string = string[:-2]
        return string + 'ying'
    elif string [-1] in consonant and string [-2] in vowel and string [-3] in consonant:
        string += [-1]
        return string + 'ing'

    else:
        return string + 'ing'

word=['lie','see','move','hug']
for item in word:
    print (makeforming(item))
