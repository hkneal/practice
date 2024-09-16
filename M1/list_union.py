list1 = [1,3,5,6,8,7]
list2 = [2,4,5,7,8]

def get_union(lst1, lst2):
    my_union = sorted(list(set(lst1).union(set(lst2))))  #Returns all unique from both
    return my_union

def get_matches(lst1, lst2):
    my_matched = sorted(list(set(lst1) & set(lst2)))  #Returns all matches that are in both lists
    return my_matched


if len(list1) > len(list2):
    matched = sorted([x for x in list2 if x in list1])
    print(matched)

print(get_union(list1, list2))
print(get_matches(list1, list2))