#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    list_rsu = []
    [list_rsu.append(sentence + '!') for sentence in sentence_list]
    print(list_rsu)
    return list_rsu
make_exclamation(["Hello", "I'm doing great", "Python is fun"])