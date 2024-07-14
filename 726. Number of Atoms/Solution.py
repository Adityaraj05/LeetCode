class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = deque([defaultdict(int)])
        i = 0
        # If the character is '(', a new defaultdict(int) is pushed onto the stack. This dictionary will store counts of atoms inside the current parentheses.
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int)) # {'k':4 }; {'O':1, 'N':1} ; {'S':1, 'O':3}; 
                i += 1
            #If the character is ')', the top dictionary is popped from the stack into curr_map.The i index is incremented, and we look for any digits following the ')', which represent the multiplier for the counts inside the parentheses. 
            elif formula[i] == ')':
                curr_map = stack.pop() #{'S':1, 'O':3} ; {'O': 7, 'N': 1, 'S': 2}
                i += 1
                multiplier = [] #['2'], ['2']
                while i < n and formula[i].isdigit():
                    multiplier.append(formula[i])  # 2, 2
                    i += 1 
                multiplier = int(''.join(multiplier)) if multiplier else 1
                for atom, count in curr_map.items():
                    curr_map[atom] = count * multiplier # {'S':2, 'O':6}; {'O': 14, 'N': 2, 'S': 4}
                # These counts are added to the previous map on the stack
                for atom, count in curr_map.items(): #{'O': 1, 'N': 1, 'S': 2, 'O': 6} ; {'K': 4, 'O': 14, 'N': 2, 'S': 4}

                    stack[-1][atom] += count  # Adjusted map: {'O': 7, 'N': 1, 'S': 2} ; {'K': 4, 'O': 14, 'N': 2, 'S': 4}



            else:
                curr_atom = [formula[i]] # ['k'], ['O', 'N'] , ['S'], ['O']
                i += 1
                # checking the next char is in lower case or not if it is in lower case then we will append it with the current char, as to consider the one char .
                while i < n and formula[i].islower():
                    curr_atom.append(formula[i])
                    i += 1
                curr_atom = ''.join(curr_atom)
                # if next atom is digit then we will do append with all the char inside { }
                curr_count = [] 
                while i < n and formula[i].isdigit():
                    curr_count.append(formula[i]) # ['4'], ['3']
                    i += 1
                curr_count = int(''.join(curr_count)) if curr_count else 1

                stack[-1][curr_atom] += curr_count # {'k' : 4}{'O':1, 'N':1}{'S':1, 'O':3}


        # Finally sorted_map sorts the dictionary items by atom name. 

        sorted_map = sorted(stack[-1].items()) # sorted_map = [('K', 4), ('N', 2), ('O', 14), ('S', 4)]
        result = []
        for atom, count in sorted_map:
            result.append(atom)
            if count > 1:
                result.append(str(count)) # ['K', '4', 'N', '2', 'O', '14', 'S', '4']

        return ''.join(result) # K4N2O14S4
 
