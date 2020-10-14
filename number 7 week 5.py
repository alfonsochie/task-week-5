def words_into_integers(list):
    a=[]
    for words in list:
        a.append(len(words))
    return a
words=['hy','my','name','is','alfonso']
print(words_into_integers(words))