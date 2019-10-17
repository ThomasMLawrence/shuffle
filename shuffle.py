#Michael Lawrence
#CS350
#915247432
#Professor Lund
#Hw 2 program

import random
import time


def main():
    A = []
    length = [1000, 2000, 3000, 4000, 5000, 6000]
    for i in range(0, len(length)):
        for i in range(0, 10): 
            total += generate_list(length[i], A)
            A.clear()        
        print "The average shuffle time for a length of " + length[i] + " was " + total/10.0 + " seconds."

def generate_list(length, A[]):
    for i in range (0, length):
        A.append(random.randint(0, 10000)

    start = time()
    shuffle(length, A)
    total = (time() - start)
    return total

def shuffe(length, A []):
    for i in range (0, length):
        j = random.randint(0, length)
        A[i], A[j] = A[j], A[i] 

if __name__ == '__main__':
    main()
