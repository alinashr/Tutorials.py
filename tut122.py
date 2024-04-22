#wordcounter using dictionary

def counter(str):
    counts={}
    for char in str:
        counts[char]=str.count(char)
    return counts

print(counter("shrestha"))