def max(a,b):
    if len(a)>=len(b):
        return a
    else:
        return b
def find_longest_word(list):
    max_word=max(list[0],list[1])
    i=2
    while i<len(list):
        max_word=max(max_word,list[i])
        i=i+1
    return len(max_word)
a=['hello','my','name','is','alfonso']
print(find_longest_word(a))
