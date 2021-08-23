x = [2, 6, 8, 9, 10, 11, 12, 13, 14, 15]

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        return sorted_v[midpoint]
    
    else:
        lo = midpoint - 1
        hi = midpoint 
        return (sorted_v[lo] + sorted_v[hi]) / 2
    

#5 inicio das execuções
print(median(x))

print(sum(x) / len(x))
 

