def minSum(num, k):
    # Write your code here
    num_set = list(set(num))
    num_set.sort()
    num.sort()
    max_num = num_set[-1]
    print(max_num)
        
    for i in range(k):
        if i > len(num) -1 :
            return sum(num)
    
        if max_num in num:
            max_num_indx = num.index(max_num)
        else:
            num_set.pop(num_set.index(max_num))
            max_num = num_set[-1]
            max_num_indx = num.index(max_num)

        if max_num > num[-1]:
            num.append(math.ceil(num.pop(max_num_indx)/2))
        else:
            num.append(math.ceil(num.pop()/2))

    return sum(num)


def minSum(num, k):
    # Write your code here
    num_set = list(set(num))
    num_set.sort()
    num.sort()
    max_num = num_set[-1]
    
    print(max_num)
        
    for i in range(k):
        if max_num > num[-1]:
            if max_num in num:
                max_num_indx = num.index(max_num)
                num.append(math.ceil(num.pop(max_num_indx)/2))
            else:
                try:
                    num_set.pop(num_set.index(max_num))
                except:
                    max_num = num[]
                max_num = num_set[-1]
                max_num_indx = num.index(max_num)
                max_num = num[-1]
                num.append(math.ceil(num.pop()/2))
            
        else:
            num.append(math.ceil(num.pop()/2))  
            
                    

    return sum(num)