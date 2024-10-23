
list1 = [12,3,4,17,7,3,9,0,1,23]
list2 = [4,1,2,19,6,4,23,4,11,15]


def cluster(list1,list2):

    set1 = set(list1)
    set2 = set(list2)

    s_union = set1.union(set2) # birleşim
    s_intersection = set1.intersection(set2) # kesişim
    s_difference1 = set1 - set2 # fark (set1-set2) 
    s_difference2 = set2 - set1 # fark (set2-set1)

    print(f"1. liste: {list1}")
    print(f"2. liste: {list2}")
    print(f"iki listenin birlesimi : {s_union}")
    print(f"iki listenin kesişimi : {s_intersection}")
    print(f"1.listeden 2.liste farki : {s_difference1}")
    print(f"2.listeden 1.liste farki : {s_difference2}")


cluster(list1,list2)