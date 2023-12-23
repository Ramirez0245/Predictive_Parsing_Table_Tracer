"""
About: Given the following CFG and the Predictive Parsing table. A program to trace input strings 
(1) a=(a + a )*a$  , (2) a=a*(a-a)$  ,  (3) a=(a+a)a$ . Shows the content of the stack after each match.
Before              After
S-->aW              S-->aW       
W--> = E            W--> = E    
E--> E+T            Q--> +TQ
E--> E-T            Q--> -TQ    Q--> Lamda
E--> T              E--> TQ
T--> T*F            R--> *FR
T -->T/F            R -->/FR    R--> Lamda
T-->F               T-->FR
F-->a               F-->a 
F--> ( E )          F--> ( E )
"""

def main():
    word1 = "a=(a+a)*a$"
    word2 = "a=a*(a-a)$"
    word3 = "a=(a+a)a$"
    word = word2

    stack = []
    stack.append('$')
    stack.append('S')
    state = stack.pop()

    read = word[0]
    word = word[1:]
    conditon = False

    while 1:
        match state:
            case "S":
                stack.append("W")
                stack.append("a")
            case "W":
                stack.append("E")
                stack.append("=")
            case "E":
                if read == "a" or read == "(":
                    stack.append("Q")
                    stack.append("T")
                else: 
                    break
            case "Q":
                if read == "+":
                    stack.append("Q")
                    stack.append("T")
                    stack.append("+")
                elif read == "-":
                    stack.append("Q")
                    stack.append("T")
                    stack.append("-")
                elif read == ")" or read == "$":
                    pass
                else: 
                    break
            case "T":
                if read == 'a' or read == '(':
                    stack.append("R")
                    stack.append("F")
                else: 
                    break
            case "R":
                if read == "+" or read == '-' or read == ')' or read == '$':
                    pass
                elif read == '*':
                    stack.append('R')
                    stack.append('F')
                    stack.append('*')
                    print('The stack: ')
                elif read == '/':
                    stack.append('R')
                    stack.append('F')
                    stack.append('/')
                else: 
                    break
            case "F":
                if read == 'a':
                    stack.append('a')
                elif read == '(':
                    stack.append(')')
                    stack.append('E')
                    stack.append('(')
                else: 
                    print('inside break?')
                    break

        state = stack.pop()

        if read == state:
            print('Word matched. Current stack ')
            print('The stack is')
            print(stack)
            print('\n')
            if len(stack) < 1:
                print('inside len(word)?')
                conditon = True
                break
            read = word[0]
            word = word[1:]
            state = stack.pop()

    if conditon:
        print("word accepted!")
    else:
        print("word not accepted")


# __name__ special variables
if __name__ == '__main__':
    main()