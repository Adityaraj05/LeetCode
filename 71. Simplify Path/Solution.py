class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
        # This line starts a loop that iterates over each character in the path string concatenated with a "/" character. The concatenation with "/" ensures that the loop will properly handle the last component of the path, as it relies on encountering "/" to identify the end of each component.
        for char in path + "/":
            #  This line checks if the current character being iterated over is a "/". If it is, it means the end of a component has been reached.
            if char == "/":
                #  This line checks if the current component being built (current) is "..", indicating a reference to the parent directory.
                if current =="..": 
                    # This line checks if the stack list is not empty. If it's not empty, it means there are components in the stack list that can be popped off to move up the directory structure.
                    if stack:
                        stack.pop()
                #  This line checks if the current component being built (current) is neither empty nor ".", indicating a valid directory or file name.
                elif current != "" and current != ".":
                    stack.append(current)
                # This line resets the current string to an empty string, preparing it for accumulating characters for the next component.
                current = ""
            # This line begins the block of code that executes if the current character being iterated over is not a "/".
            else:
                # This line appends the current character to the current string, effectively building up the current component of the path.
                current += char
                    
        return "/" + "/".join(stack)
