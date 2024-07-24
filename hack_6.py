"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
 

    if not result:  # Si la lista está vacía
        return ["0"]
    else:  # Si la lista no está vacía
        return [str(i+1) if i % 2 == 0 else "-" for i in range(len(result))]
    


    #...
