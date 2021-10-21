#!/usr/bin/env python3
# Moving 1 and 0's to opposite sides of the array
# Author: Lyssette Williams


arr = [1,0,1,0,0,1,0,1]

def minMoves(arr):   # Write your code here
# declaring variables and setting them all to zero
    score0 = 0
    score1 = 0
    num0 = 0
    num1 = 0
    swapcount = 0
    for i in range(len(arr)):  #first loop counts all the ones and zeros to determine
        if arr[i] == 0:        # which way the program swaps, want to swap to the 'heavier'side  
            if i - num0 > 0:    # so there are less swaps overall 
                score0 += i - num0 # score0 = how many times you swap all 0s to the left
            num0 += 1
        else:
            if i - num1 > 0:
                score1 += i - num1 #score1 - how many times you swap all the 1s to the left
            num1 += 1      
    swap_num = 0
    score = score0
    num_to_swap = num0
    if score0 > score1: # this chooses the smaller of the two scores and sets the variables accordingly 
        num_to_swap = num1
        score = score1
        swap_num = 1     
    index = 1  #initializing/setting up starting conditions, not starting at index 0
    while index < len(arr) and swapcount < num_to_swap: #this loop starts from the left and moves all the chosen number to the left side
        swapped = False  #second part is optimizaiton to break out of the loop #does this by finding number that matches the type and walking backwards until it's all the way to the left
        while index > 0 and arr[index] == swap_num and arr[index - 1] != swap_num: #!= is not equal -  looking at the current index and the number to the left of it (-1) determining the swap number and if they have to swap
            temp = arr[index] #these are the swap, putting current index value into a temp variable
            arr[index] = arr[index - 1] #replacing current index value with the one to the left of it
            arr[index - 1] = temp # replacing the value to the left with the temp value
            index -= 1 # walks the index left
            swapped = True # check to let us know we did a swap
        if swapped: #if we've done a swap 
            swapcount += 1     # adds 1 to the swap count so we can exit the loop early
        index +=1          #walking the index to the right so we can start the loop over again (next element in the array)
    return score  #returns the score calculated in the first section of the code

print(score)    