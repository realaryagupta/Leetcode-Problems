class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def bckspc(string):
            stack = []
            for i in string:
                if i == "#":
                    try:
                        stack.pop() 
                    except IndexError:  
                        pass  
                else:
                    stack.append(i)
            return ''.join(stack)  

        return (bckspc(s) == bckspc(t)) 
