def circularArrayRotation(a, k, queries):
    rang = k % len(a)
    
    if rang != 0:
        for i in range(rang):
            a.insert(0, a.pop())
            
    final_arr = []
    
    for i in queries:
        final_arr.append(a[i])
            
    return final_arr