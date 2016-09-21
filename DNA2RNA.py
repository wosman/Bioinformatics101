from termcolor import colored
import sys

# print colored('hello', 'red'), colored('world', 'green')



# This program will transcribe a sequence of DNA entered by the user into RNA
# You will have to pip install termcolor

def transcribe(dna):
    print colored('Attempting to transcribe your deoxyribonucleic acid sequence into a ribonucleic acid sequence.', 'yellow')
    return dna.replace('T','U')

print colored('Please enter your sequence of DNA:', 'blue')
print colored('e.g. ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC', 'magenta')
dna = raw_input()
rna = ''
rna = transcribe(dna)
print colored('Your transcribed sequence is:', 'red') + colored(rna, 'green')
print colored('Thank you', 'cyan', attrs=['reverse','blink'])

