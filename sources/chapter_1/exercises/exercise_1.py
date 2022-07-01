import re

def sum_terms(A, B):
    menor = min(A, B, key=len)
    maior = B if menor == A else A
    regex = re.findall(r'[{}]'.format(menor), maior)
    found = ''.join(sorted(regex))
    menor = ''.join(sorted(menor))

    if menor in found:
        return menor
    return menor + '+' + maior