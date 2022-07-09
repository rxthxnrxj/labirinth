import re
import numpy as np


def load_words():
    l={}
    audDict="./static/cmudict.txt"
    with open(audDict, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    l[key] = re.findall(r"[A-Z]+",val)
    return l
final_dict=load_words()


def all_terms():
    terms=[]
    audDict="./static/cmudict.txt"
    with open(audDict, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    terms.append(re.findall(r"[A-Z]+",val))
    return terms
all_terms=all_terms()


terms=[]

print("All the terms taken considered: ")
print(all_terms)

for term in all_terms:
    for t in term:
        if t not in terms:
            terms.append(t)

print("\nUnique phoenetics from all words: ")

print(terms)