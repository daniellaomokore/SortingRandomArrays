#@author Daniella-O

##Task: Create a random 100 x 100 array, sort the odd rows in decsending order and even rows in ascending order
##Do this with two different sorting algorithms without using inbuilt functions and find the running times for the different sorting algorithms
#

import numpy as np
import random
import timeit

array=[[random.randint(1,101) for i in range (100)] for j in range(100)] #create 100x100 random array with random values
print("Unsorted Array:")
print(array)



def BubbleSort(array, ascending): 
    if not ascending: 
        
        for j in range(len(array)): #itterate through columns of the array
            
            for a in range(len(array) - j - 1): #itterate through rows of the array
               
                if (array[a] < array[a+1]): #if right element in the list is greater than left element.. swap elements
                        
                        d = array[a] #swapping of values
                        array[a] = array[a+1]
                        array[a+1] = d
                        
    if ascending: #for the odd rows sort in ascending order
    
        for j in range(len(array)): #itterate through columns of the array
                
            for a in range(len(array) - j - 1): #itterate through rows of the array
                
                if (array[a] > array[a+1]): #if left element in the list is greater than right element.. swap elements
                        
                        d = array[a] #swapping of values
                        array[a] = array[a+1]
                        array[a+1] = d 
                                            

def QuickSort(array, ascending): 
    
    if ascending:
            
            length = len(array) #calculate length of array
            if length <=1 :    #if length of array is less that or equal to one
                return array   #this skips array that have a length of one or zero
            else:      #only continuing for arrays greater than one
                pivot = array.pop() #define your pivot , the pop removes and returns last element
            
            itemsGreater = []  #create two empty list that items are moved to after being compared to pivot point
            itemsLower = []
            
            for item in array:    
                if item > pivot:  
                    itemsGreater.append(item)#add items from array that are bigger than the pivot to the empty list
                else:
                    itemsLower.append(item)  # add items small that pivot to other empty list
                    
            return QuickSort(itemsLower, ascending) + [pivot] + QuickSort(itemsGreater, ascending) #
            
    else:   
                length = len(array)
                if length <=1 :
                    return array
                else:
                    pivot = array.pop()
            
                itemsGreater = []
                itemsLower = []
            
                for item in array:
                    if item < pivot:
                        itemsGreater.append(item) #add items from unsorted array that are bigger than the pivot to the empty list
                    else: 
                        itemsLower.append(item)  # add items small that pivot to other empty list
                    
                return QuickSort(itemsLower,ascending) + [pivot] + QuickSort(itemsGreater,ascending)



print(" Array Sorted using Bubble Sort:")

def arrayOneTime(array): 
    a = array.copy() #create an unsorted copy of the 100x100 array
    for i in range(len(a)):     
        BubbleSort(a[i], i%2>0)  
    return(a)   #return the sorted array

print(arrayOneTime(array)) #display the array sorted with bubblesort

print("Array Sorted using Quick Sort:") 
def arrayTwoTime(array):
    a2 = array.copy()  #create an unsorted copy of the 100x100 array
    for i in range(len(a2)): 
        a2[i]= QuickSort(a2[i], i%2>0)
    return(a2) #return the sorted array

print(arrayTwoTime(array)) #display the array sorted with quicksort 

#t = timeit.timeit(lambda: BubbleSort(Array[i], i%2>0) , number=10)
t = timeit.timeit('arrayOneTime(array)', globals=globals(), number=10) #measure execution time of bubblesort 
print("Running time of BubbleSort is: ", t) # display the running time for bubble sort

t2 = timeit.timeit('arrayTwoTime(array)', globals=globals(), number=10) #measure execution time of quicksort 
print("Running time of QuickSort is: ", t2) #display the running time for quicksort

