import time
class RegexMachine:
    def __init__(self):
        self.statesDirectory = {}
        # Example:
        # self.statesDirectory = {0:{'0':0, '1':1},
        #                         1:{'0':2, '1':0},
        #                         2:{'0':1, '1':2}}
        self.logMessages = []
        self.initialState=0
        self.endState=0

    # Returns Boolean
    def evaluate(self, string):
        currentState = self.initialState
        print("Amount of states: %d" % len(self.statesDirectory))
        if len(self.logMessages) != 0:
            self.logMessages = []
        self.logMessages.append("-------------------------------")
        self.logMessages.append("States in given regex: \n")
        for stateKey in self.statesDirectory:
            self.logMessages.append("\t" + str(stateKey) + " : " + str(self.statesDirectory[stateKey]))
        self.logMessages.append("End State is: " + str(stateKey))
        self.logMessages.append("-------------------------------")


        print("End State is: " + str(stateKey))
        for char in string:
            try:
                self.logMessages.append("At state: " + str(currentState))
                currentState = self.statesDirectory[currentState][char]
                self.logInfo(currentState, True, char)
            except KeyError:
                self.logInfo(currentState, False, char)
                return False
        return currentState == self.endState


    def logInfo(self, stateNumber, isPassed, char):
        if isPassed:
            self.logMessages.append("State Passed: " + char)
        else:
            self.logMessages.append("State Failed: " + char)


    def getLogInfoList(self):
        return self.logMessages


    def mapRegex(self, regex):
        statesDirectory={}
        self.statesDirectory={}
        self.initialState=0
        self.endState=0

        stateKey = 0
        currentState = {}
        infDetector = []
        isRepeated = False
        #TODO: Cases for parentesis
        #TODO: Case for * when you have parentesis
        #REMEMBER THAT THERE CANT BE JUST ONE PARENTESIS
        # Goes through each character in the regex string
        for index in range(0, len(regex)):

            token = regex[index]

            # LINE CASE
            if token == '|':
                stateKey = stateKey - 1
                currentState = self.statesDirectory[stateKey]

            # START PARENTESIS CASE
            elif token == '(':
                # Parentesis is the first token in the regex, previous was parentesis or single char
                if len(currentState) == 0:
                    currentState = {}
                #Followed by *
                elif regex[index-1] == '*':
                    print()



            # END PARENTESIS CASE
            elif token == ')':

                if len(self.statesDirectory)-1 == stateKey:
                    stateKey=stateKey+1

                currentState = {}


            # ASTERISK CASE
            elif token == '*':

                # Single Char case
                if regex[index-1] != ')':

                    # Must obtain currentState again since we need to point all
                    # values to point to itself and find a value to move on from
                    # the state to another state
                    stateKey = stateKey - 1
                    currentState = self.statesDirectory[stateKey]
                    currentState[regex[index-1]] = stateKey

                #Parentesis Case
                else:
                    # Must obtain currentState again since we need to point all
                    # values to point to itself and find a value to move on from
                    # the state to another state
                    stateKey = stateKey - 1
                    currentState = self.statesDirectory[stateKey]

                    #Point to itself
                    for keyToken in currentState:
                        currentState[keyToken] = stateKey

            # CHARACTER CASE
            else:
                #Single char without parentesis
                if len(currentState) == 0:
                    currentState = {token: stateKey + 1} #Points to the next state
                    self.statesDirectory[stateKey] = currentState #Saves the state
                    stateKey=stateKey+1
                    currentState = {}
                #Char in parentesis
                else:
                    currentState[token] = stateKey + 1
        # ENDFOR

        # If it didn't end in a wildcard, add a ending state.
        # If it did end in a wildcard, the ending state will be the current state
        if regex[len(regex)-1] != '*':
            if len(self.statesDirectory)-1 != stateKey:
                self.statesDirectory[stateKey] = {}
            else:
                stateKey = stateKey + 1
                self.statesDirectory[stateKey] = {}


        self.endState = stateKey
        print("States in given regex: \n\n")
        for stateKey in self.statesDirectory:
            print(str(stateKey) + " : " + str(self.statesDirectory[stateKey]))

        print("End State is: " + str(stateKey))

    ############################################
    #           Case Definitions               #
    ############################################
