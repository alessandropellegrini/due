#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

def shift(spliceable, offset):
    return spliceable[offset:] + spliceable[:offset]


def caesar(key):
    shifted_lowercase = shift(string.lowercase, key)
    shifted_uppercase = shift(string.uppercase, key)
    shifted_letters = shifted_lowercase + shifted_uppercase
    
    encode_table = string.maketrans(string.letters, shifted_letters)
    decode_table = string.maketrans(shifted_letters, string.letters)

    def encode(string):
        'Encode message with key %d' % key
        return string.translate(encode_table)
    def decode(string):
        'Decode message with key %d' % key
        return string.translate(decode_table)
    return encode, decode

