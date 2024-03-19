class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    #   This line creates a Counter object named count which stores the frequency of each task in the tasks list
        count = Counter(tasks) # [A->2,B->2,C->1,D->1]
        # Here, a list named maxHeap is created. It contains the negative frequencies of each task obtained from the count dictionary. Negative values are used because Python's heapq module creates a min-heap by default, and we want to create a max-heap.
        maxHeap = [-cnt for cnt in count.values()]
        # This line converts the maxHeap list into a max-heap. After this operation, the first element of the list will be the largest negative frequency.
        heapq.heapify(maxHeap)
        # Two variables are initialized: time, which will keep track of the total time taken, and q, which is a deque that will store pairs of [task_frequency, idle_time].
        time = 0
        q = deque()  #pairs of [-cnt , idleTime]
        while maxHeap or q:
            time +=1
            # Here, if maxHeap is not empty, the most frequent task's frequency is retrieved by popping the max value (which is the most negative value due to negation earlier). The frequency is then incremented by 1 and stored in cnt. If cnt is still non-zero after incrementing, it means there are remaining tasks of that type. So, [cnt, time + n] is appended to q, where time + n represents the time at which this task can be scheduled again (n being the cooling period).
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
                    # If there are tasks in q and the scheduled time of the first task in q is equal to the current time, it means this task can be executed again. So, its frequency (the first element of the pair) is pushed back into maxHeap, and the pair is removed from q.
            if q and q[0][1] == time:
                heapq.heappush (maxHeap, q.popleft()[0])
            # Finally, the total time taken for scheduling all tasks is returned.
        return time
