"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    lista= []
    if len(result) % 2 == 0:  # Si la lista es par
        for i in range (len(result)):
            lista.append(str(i+1))
        
        lista.reverse()
        result = lista
        return result
    else:
        for i in range (len(result)):
            lista.append(f"{result[i]}-{str(i+1)}")
          

        lista.reverse()
        result = lista
        return result

    
    
print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b",]))