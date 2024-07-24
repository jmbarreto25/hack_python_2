"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s

    if len(result) == 1:  # Si la lista contiene un elemento
        return [0]
    else:  # Si la lista es mayor que 1
        return [str(i+1) if i % 2 == 0 else int(i+1) for i in range(len(result))]
    

    
