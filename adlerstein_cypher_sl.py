#!/usr/bin/env python

import numpy as np
import random
import streamlit as st


def cypher_and_key(s):
    l=[]
    for i in nums:
        for j in nums:
            if i-j==s:
                l.append([i, j])
    return random.choice(l)


def get_key(val):
    for key, value in d.items():
        if val in value:
            return key
    return "key doesn't exist"


d = {'A':[0,-26],'B':[1,-25],'C':[2,-24],'D':[3,-23],'E':[4,-22],'F':[5,-21],
     'G':[6,-20],'H':[7,-19],'I':[8,-18],'J':[9,-17],'K':[10,-16],'L':[11,-15],
     'M':[12,-14],'N':[13,-13],'O':[14,-12],'P':[15,-11],'Q':[16,-10],'R':[17,-9],
     'S':[18,-8],'T':[19,-7],'U':[20,-6],'V':[21,-5],'W':[22,-4],'X':[23,-3],
     'Y':[24,-2],'Z':[25,-1]
    }


if __name__ == '__main__':
    st.title('Fire in Adlerstein Cypher')
    st.write('This cypher is composed of two encrypted words: a cypher and a key. The words are composed of letters only and exclude white-spaces. Example: CXEIIX and AZPBEG. Each letter in the alphabet is assigned to two numbers (a positive number ranging from 1 to 25, and a negative number ranging from -1 to -26). To find the hidden message, look up the number assigned to each letter in both words. For example: [2,23,4,8,8,23] and [0,25,15,1,4,6]. Each letter in the cypher must be subtracted by each letter in the key. Example: [2,-2,-11,7,4,17]. The resulting list of numbers can then be used to solve the message by looking up each number in the table. Example: 2=C, -2=Y, -11=P, 7=H, 4=E, 17=R.')
    st.write(d.items())
    
    st.write('__________________________________')
    #phrase = 'STREAMLIT'
    phrase = st.text_input('Enter a message (letters only, no spaces)').upper()

    nums = np.arange(-26, 25).tolist()

    cypher = ''
    key=''
    if all(elem in d.keys() for elem in list(phrase)) == True:
        for i in phrase:
            a = cypher_and_key(d[i][0])
            cypher = cypher + [k for k, v in d.items() if v[0] == a[0] or v[1] == a[0]][0]
            key = key + [k for k, v in d.items() if v[0] == a[1] or v[1] == a[1]][0]
    else: st.write('ERROR: The message must contain only letters.')
    
    
    st.write('Message: {}'.format(phrase))
    st.write('Cypher: {} | Key: {}'.format(cypher, key))


    st.write('__________________________________')
    in_cypher = st.text_input('Enter a cypher (letters only, no spaces). Example: CXEIIX').upper()
    in_key = st.text_input('Enter a key  (letters only, no spaces). Example: AZPBEG').upper()


    message = ''
    for i,j in zip(in_cypher,in_key):
        num = d[i][0]-d[j][0]
        message = message+(get_key(num))

    st.write('Message: {}'.format(message))