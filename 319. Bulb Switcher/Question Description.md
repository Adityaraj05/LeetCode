319. Bulb Switcher


There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/bd2da057-4034-4ee8-bc93-cd5eb314fd0d)



Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1
 

Constraints:

0 <= n <= 109


-----------------------------------------------------------------------------------------------------------========================================================================================================
![b](https://github.com/Adityaraj05/LeetCode/assets/118068294/811d92a3-42a6-4fa7-9b3d-99ea6d27b1b7)

