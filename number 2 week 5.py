def translate(str):
    consonants='bcdfghjklmnpqrstvwxyz'
    print("".join(l+'o'+l if l in consonants else l for l in str))

string=input("Enter Any String: ")

translate(string)