def is_member(x,a):
    if x in a:
        return  True
    else:
        return False
def overlapping(list1,list2):
    for li in list1:
        if is_member(li,list2):
            return True
    else:
        return False
print(overlapping(['e','a','b'],['c','d','e','f']))
print(overlapping(['a','b','c'],['f','d','e']))