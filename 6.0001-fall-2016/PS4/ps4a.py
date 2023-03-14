# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

#from argon2 import DEFAULT_MEMORY_COST
from itertools import permutations
import copy
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    ### Pseudo Code ###
    # if length of sequence is 1; return output
    if len(sequence) == 1:
        return [sequence]
    else:
        first = sequence[0]
        rest = get_permutations(sequence[1:])
        out = []
        for item in rest:
            z = list(item)
            for num in range(len(item)+1):
                z.insert(num,first)
                out.append("".join(z))
                z.pop(num)
    return out

if __name__ == '__main__':
   #EXAMPLE
   example_input = '123'
   print('Input:', example_input)
   print('Expected Output:', ["123","132","312","321","213","231"])
   print('Actual Output:', get_permutations(example_input))
   print("Checker:", set(["123","132","312","321","213","231"]) == set(get_permutations(example_input)))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


