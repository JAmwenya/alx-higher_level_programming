#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    if (len(sentence) == 0):
        my_tuple = (len(sentence), None)
        return(my_tuple)
    else:
        my_tuple = (len(sentence), sentence[0])
        return (my_tuple)
