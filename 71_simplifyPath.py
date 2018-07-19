class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        segments = path.split("/")
        for segment in segments:
            if segment == ".." and stack:
                stack.pop()
            elif segment != ".." and segment != "." and segment != '':
                stack.append(segment)
        return "/" + "/".join(stack)
