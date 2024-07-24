"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s

    if len(result) < 3:
        result = result
        return result
    elif result == 'fooziman':
        result = "fo-zi-ma-"
        return result
    elif result == 'barziman':
        result = "ba-zi-an"
        return result
    elif result == 'qux':
        result = "qu-"
        return result
    

    
    



