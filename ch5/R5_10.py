#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_10.py
#       Description:
#           change init
#
#       Last Modified:
#           2014-06-26 17:08:36


from caesar import CaesarCipher


class NewCaesar(CaesarCipher):
    def __init__(self, shift):
        self._forward = ''.join(chr((i + shift) % 26 + ord('A'))
                                for i in range(26))
        self._backward = ''.join(chr((i - shift) % 26 + ord('A'))
                                 for i in range(26))
if __name__ == '__main__':
    cipher = NewCaesar(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
