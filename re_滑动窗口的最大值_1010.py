class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()       #这是一个双边队列，有栈和队列的性质
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:   
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:               #如果滑动窗口的下一个0位置的元素的前一个位置，即i-k,是最大的那个元素，这说明现在的窗口已经离开之前的最大元素了，因此需要去除掉deque的队首元素
                deque.popleft()                        #上述之后会进入while， 例如原来是 3 12 ， 现在是 1 2  新的窗口尾进入5，  3<5,因此 deque去掉3， 1 <5,所以duque变成 【5】
            while deque and deque[-1] < nums[i]:   # deque的第0个位置 只记录窗口的最大元素，一开始deque第0个是nums的第0个元素，如果nums的第一个元素大于第0个，就去掉deque的第0个再append第一个
                deque.pop()                       #热锅不大于，则直接append,仍然保证了deque第0个是最大的,res每次只记录deque的第0个。
            deque.append(nums[i])
            res.append(deque[0])
        return res
