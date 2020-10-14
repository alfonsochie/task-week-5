def char_freq(string):
    freq = {key: 0 for key in string}
    for i in string:
        freq[i] += 1
    return freq


if __name__ == "__main__":
    print (char_freq("hello world"))
#example 2 below
    #print (char_freq("aaabbbcccdddeeefffffffgggggg"))