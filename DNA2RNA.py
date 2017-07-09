from termcolor import colored

# This program will transcribe a sequence of DNA entered by the user into RNA
# You will have to pip install termcolor


def transcribe(dna):
    print colored('Attempting to transcribe your deoxyribonucleic acid sequence into a ribonucleic acid sequence.', 'yellow')
    return dna.replace('T','U')

print colored('Please enter your sequence of DNA below:', 'blue')
print colored('e.g. (exempli gratia) ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC', 'magenta')
dna = raw_input()
rna = transcribe(dna)
print colored('Your transcribed sequence is:', 'red') + colored(rna, 'green')
print colored('Thank you', 'cyan', attrs=['reverse','blink'])
