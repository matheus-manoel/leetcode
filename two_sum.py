'''
Dado um array de números inteiros e um número
alvo, retorne os índices dos dois
números que somados resultam no número alvo.

Assuma que sempre haverá solução e que você
não pode usar o mesmo elemento duas vezes.
 

Exemplo 1:

Entrada: nums = [2,7,11,15], alvo = 26
Saída: [2,3]

Exemplo 2:

Entrada: nums = [3,2,4], alvo = 6
Saída: [1,2]
Exemplo 3:

Entrada: nums = [3,3], alvo = 6
Saída: [0,1]
'''

def two_sum(nums, target):
    nums_index = {}

    for i, num in enumerate(nums):
        nums_index[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_index and i != nums_index[complement]:
            return [i, nums_index[complement]]


print(two_sum([2,7,11,15], 26))
