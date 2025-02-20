class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []  # Initialize an empty stack to keep track of surviving asteroids

        for num in asteroids:  # Iterate through each asteroid in the list
            # While there are asteroids in the stack and the current asteroid is negative
            # and the top of the stack is positive (indicating a potential collision)
            while stack and num < 0 and stack[-1] > 0:
                diff = num + stack[-1]  # Calculate the result of the collision

                if diff < 0:
                    # If diff is less than zero, it means the current asteroid (num) is smaller
                    # So we pop the top element from the stack (the positive asteroid)
                    stack.pop()
                elif diff > 0:
                    # If diff is greater than zero, it means the top of the stack is smaller
                    # So we break out of the loop as the current asteroid survives
                    break
                else:
                    # If diff is equal to zero, both asteroids are equal and destroy each other
                    stack.pop()  # Remove the top element from the stack
                    break  # Exit the loop since both are destroyed
            
            else:
                # If we exit the while loop without a break, we check if num is not zero
                if num != 0:  # Only append non-zero asteroids to the stack
                    stack.append(num)

        return stack  # Return the remaining asteroids in the stack