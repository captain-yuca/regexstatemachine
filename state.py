class State:
    def __init__(self):
        self.inputChars = []
        self.charsToCheckFor = []
        self.endState = None
    def checkState(self):
        for char in self.inputChars:
            #For each character in the string, check if they
            #match with one of them
            for schemeChar in self.charsToCheckFor:
                if char!=schemeChar:
                    return False
        return True
    def setCharsToCheckFor(self, chars):
        self.charsToCheckFor = chars
    def setEndState(self, endState):
        self.endState = endState
    def addCharToState(self, char):
        self.charsToCheckFor.append(char)
    def addString
