def encryption(s):
    s = s.strip()
    rootOfLength = math.sqrt(len(s))
    (raw, column) = (math.floor(rootOfLength), math.ceil(rootOfLength))
    
    encrypted_string = ''
    
    if len(s) % column > 0:
        raw += 1
    
    for c in range(column):
        es = '' 
        for r in range(raw):
            i = (r * column) + c          
            if i < len(s):
                es += s[i]
        
        if c != (column - 1):
            encrypted_string += (es + ' ')
        else:
            encrypted_string += es
    
    return encrypted_string