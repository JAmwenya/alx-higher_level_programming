#!/usr/bin/python3
def multiple_returns(sentence):
    my_sen = len(sentence)
    if (my_sen == 0):
        my_tuple = (my_sen, None)
        return(my_tuple)
    else:
        my_tuple = (my_sen, sentence[0])
        return (my_tuple)
