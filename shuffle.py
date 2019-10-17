#Michael Lawrence
#CS350
#915247432
#Professor Lund
#Hw 2 program

import random
import time
import string

def shuffle(length, A):
    for i in range(0, length):
        j = random.randint(0, length - 1)
        #gets the index of a random cell
        A[i], A[j] = A[j], A[i] 
        #swaps the i cell with a random cell in the list
        #this ensures that every cell gets swapped 

def generate_list(length, A):
    random.seed(None)
    for i in range(0, length):
        A.append(random.randint(0, 10000))
        #appends random ints to the list at the quantity that has been passed in

def main():
    A = []
    #A will be filled with random ints
    length = [1000, 2000, 3000, 4000, 5000, 6000]
    #different lengths are used to test efficiency
    for i in range(0, len(length)):
        total = 0
        for j in range(0, 10): 
            #each length is tested ten times to get an average
            generate_list(length[i], A)
            start = time.time()
            shuffle(length[i], A)
            total += (time.time() - start)
            #gets the start and end time to run shuffle and builds total
            A.clear()        
            #clears the list to do it again
        print ("With an input size of {}\nthe average shuffle time for 1000 items was {} seconds.\n".format(length[i], (total/10.0)/(i + 1)))
        #the time to shuffle 1000 items shows the relationship between the different shuffles
        #this will help show the O() of the algorithm
        #for instance if it is O(n^2) then the time to shuffle 1000 items should double
        #if the size goes from 1000 to 2000

if __name__ == '__main__':
    main()
