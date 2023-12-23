"""
About: Given the following CFG and the Predictive Parsing table. A program to trace input strings 
(1) (i+i)*i$  ,(2) i*(i-i)$   , (3) i(i+i)$ . Shows the content of the stack after each match.
Before               After
E --> E+T;           Q --> +TQ
E--> E- T;           Q--> -TQ;  Q--> Lamda 
E--> T;              E--> TQ;
T-->T*F;             R--> *FR;
T-->T/F;             R--> /FR;  R--> Lamda 
T-->F;               T--> FR;  
F-->i;               F--> i
F—>( E )             F—> ( E )
Table:
states	    i	    +	    -	    *	    /	    (	    )	    $
E	        TQ					                    TQ		
Q		            +TQ	    -TQ				                λ	     λ
T	        FR					                    FR		
R		            λ	    λ	    *FR	    /FR		        λ	    λ
F	        i					                    ( E )		
"""
def main():
    word1 = "(i+i)*i$"
    word2 = "i*(i-i)$"
    word3 = "i(i+i)$"
    word = word1

    stack = []
    stack.append('$')
    stack.append('E')


    read = word[0]
    word = word[1:]
    state = stack.pop()    
    conditon = False

    while 1:
        match state:
            case "E":
                #E -> TQ
                if read == "i" or read == "(":
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
                if read == 'i' or read == '(':
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
                if read == 'i':
                    stack.append('i')
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
                conditon = True
                break
            read = word[0]
            word = word[1:]
            state = stack.pop()

    if conditon:
        print("Word accepted!")
    else:
        print("Word not accepted")


# __name__ special variables
if __name__ == '__main__':
    main()