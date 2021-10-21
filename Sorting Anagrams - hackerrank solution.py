#!/usr/bin/env python3
# Sorting anagrams
# Author: Lyssette Williams

# Write your code here
def funWithAnagrams(text):
    sorted_text = [] #list/array 
    for word in text: #text is array provided
        sorted_text.append(sorted(word))   
 #makes a copy of provided array, with each word sorted alphabetically
 #sorting the individual letters within the word
 #reason to keep a copy, if two words are anagrams they'll match exactly when sorted
 #makes checking easier in the next loop  
    for i in range(len(text)-1,-1,-1): #walks backward end of the array to the start
        for j in range(i): #starts at 0 works it's way to i, through the whole loop
            if sorted_text[i] == sorted_text[j]: #if i and j have matching sorted versions
                text.pop(i) #we delete it
                break #we end the inner loop
    text.sort()#anagram free array in text and sorts the whole array
    return text            










if __name__ == '__main__':