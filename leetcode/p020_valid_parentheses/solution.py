class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(((())))"))
