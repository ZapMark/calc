#Calculator program designed for a raspberry pi
#Created by Mark Osborn


################################################################################################################################


#First defined function takes list input and turns any elements that are within parentheses into a another list within original list
#Used for formatting to properly go through order of operations starting with parentheses
def paren(uin):
    length = len(uin)
    end = 0
    #run through each element of the list
    while length > end:
        #checks for first case of closed parentheses
        if uin[end] == ")":
            #moves backwards from closed parentheses
            for start in range(end, -1, -1):
                #Detects adjacent open parentheses
                if uin[start] == "(":
                    #Replaces "(" element with a list of what was stored within paretheses
                    uin[start] = uin[start+1:end]
                    #Run through remaining list that stored parentheses information and remove them
                    for k in range(end, start, -1):
                        uin.pop(k)
                    #Adjust value of end to continue the loops
                    end = start
                    #Adjust the value of length to represent the updated length
                    length = len(uin)
                    break
        end += 1
    return uin

#Take a user string input, turn to properly formatted list
#formats numbers so instead of 2 elements like '5' and '6' it will make it '56' for math
def userIn():
    uinstr = input("go ")
    #convert the input string to a list
    uin = list(uinstr)
    length = len(uin)
    
    return uin

#def checkInputs()
    #Check for inputs that go beyond type 1 inputs

#def allowableInput()
    #Checks to make sure input is a legal math statement
    #Will do this first as to avoid crashes
    #No divide by zero
    #Num open and closed parentheses are equal
    #Each +, -, x, / all have a corresponding number before and after
    #Having 2 operations in a row (3+-4)

#def abort()
    #Use if allowableInput() is false and it will kill the program and notify the user

uin = userIn()
#uin = paren(uin)
print(uin)