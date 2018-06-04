import re
import collections

def my_words():
    with open('textic.txt', encoding='utf-8') as f:
        text = f.read()
    symbols = ''',.:;()?!*'"\|/[]}—{«»@#$%~`^&1234567890'''
    words = [i.strip(symbols) for i in text.split()]
    return words

def main(words):
    d = {word: len(word) for word in words}
    for k, v in d.items():
        word = k
        count = v
        print('{}_{}'.format(word, count))

if __name__ == "__main__":        
    main(my_words())
