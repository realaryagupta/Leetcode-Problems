class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []

        for char in num:
            # k > 0 so that we will only pop until k is more than 0
            # and stack means that we will check stack must not be empty
            # stack[-1] > char means that we will check the topmost element is more than char or not 
            while k > 0 and stack and stack[-1] > char:
                # decrease k 
                k = k - 1
                # pop because we found that topmost value of stack will be more than char so this will break the monotonic increasing stack
                stack.pop() 
            # adding char after popping greater elements
            stack.append(char)

        # slice the stack to remove the last k elements if any, as they are the largest remaining digits
        stack = stack[:len(stack) - k]  
        
        # join the characters in the stack to form the final number string,
        # and convert to int to remove any leading zeros before converting back to str
        res = "".join(stack)  
        
        return str(int(res)) if res else "0"
