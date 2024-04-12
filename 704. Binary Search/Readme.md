
Given a sorted array of n uniformly distributed values arr[], write a function to search for a particular element x in the array. 
Linear Search finds the element in O(n) time, Jump Search takes O(? n) time and Binary Search takes O(log n) time. 
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Interpolation constructs new data points within the range of a discrete set of known data points. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.
To find the position to be searched, it uses the following formula. 

// The idea of formula is to return higher value of pos
// when element to be searched is closer to arr[hi]. And
// smaller value when closer to arr[lo]

arr[] ==> Array where elements need to be searched

x     ==> Element to be searched

lo    ==> Starting index in arr[]

hi    ==> Ending index in arr[]

pos = lo + [(x-arr[lo])//(arr[hi]-arr[Lo])] *(hi-lo) }             
     

There are many different interpolation methods and one such is known as linear interpolation. Linear interpolation takes two data points which we assume as (x1,y1) and (x2,y2) and the formula is :  at point(x,y).

This algorithm works in a way we search for a word in a dictionary. The interpolation search algorithm improves the binary search algorithm.  The formula for finding a value is: K = data-low/high-low.

 
K is a constant which is used to narrow the search space. In the case of binary search, the value for this constant is: K=(low+high)/2.



![WhatsApp Image 2024-04-12 at 17 36 43_e04e260a](https://github.com/Adityaraj05/LeetCode/assets/118068294/6b08a6c8-0d82-40fa-ac65-df0041bb4dee)
