def filter_long_words(inputList, inputInteger):
    listOfWords = []

    for i in range(len(inputList)):
        if len(inputList[i]) > inputInteger:
            listOfWords.append(inputList[i])

    return listOfWords


inputListOfWords = ['hello', 'everyone', 'my', 'is', 'alfonso']
inputWordLength = 5

print(str(filter_long_words(inputListOfWords, inputWordLength)))