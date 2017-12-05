import tkinter as tk

from tkinter import ttk
from tkinter import messagebox as mBox

from finitestatemachine import RegexMachine

class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Finite State Automata")
        self.regexMachine = RegexMachine()
        self.createWidgets()
        self.setPadding()

        self.statesRepresentationText = []

        self._infoMsgBox("Welcome to Manny's Regex Machine. Please remember to write"+
        " correct regular expressions using *, |, ( or ). These are the only supported tokens"+
        " other than normal characters. Also please refrain from doing the following regexes:\n"+
        "(ab|ab) - Combining two characters with an |\n"+
        "f*w* - Placing two tokens with * back to back.\n\n" + "Please click the console you used to open the project and click on the app again.")
        self.win.mainloop()


    def createWidgets(self):
        # INFO
        # REGEX
        # Regex Label
        self.regexLabel = ttk.Label(self.win, text="Enter your Regex: ")
        self.regexLabel.grid(column=0, row=0)

        # Regex Box
        self.regexValue = tk.StringVar()
        self.regexBox = ttk.Entry(self.win, width=12, textvariable=self.regexValue)
        self.regexBox.grid(column=1, row=0)

        # EXPRESSION
        # Expression Label
        self.expressionLabel = ttk.Label(self.win,
                                    text="Enter your expression to evaluate: "
                                    )
        self.expressionLabel.grid(column=0, row=1)

        # Expression Box
        self.expressionValue = tk.StringVar()
        self.expressionBox = ttk.Entry(self.win, width=12, textvariable=self.expressionValue)
        self.expressionBox.grid(column=1, row=1)
        #BUTTON
        self.action = ttk.Button(self.win, text="Evaluate", command=self.clickMe)
        self.action.grid(column=0, row=2, columnspan=4)




    # Button Click Event Function
    def clickMe(self):

        self.regexMachine.mapRegex(self.regexValue.get())
        isCorrect = self.regexMachine.evaluate(self.expressionValue.get())
        self.clearStatesRepresentationText()
        logMessages = self.regexMachine.getLogInfoList()
        offset = 3
        for logmsg in logMessages:


            msgLabel = ttk.Label(self.win,
                                        text=logmsg
                                        )
            msgLabel.grid(column=0, row=offset, columnspan=4)

            self.statesRepresentationText.append(msgLabel)
            offset = offset + 1

        if isCorrect:
            self._infoMsgBox("The expression '" + self.expressionValue.get()
                            + "' passed the regex '"
                            + self.regexValue.get() + "' evaluation.")
        else:
            self._infoMsgBox("The expression '" + self.expressionValue.get()
                            + "' did not pass the regex '"
                            + self.regexValue.get() + "' evaluation.")



    def clearStatesRepresentationText(self):
        for i in range(0, len(self.statesRepresentationText)):
            label = self.statesRepresentationText[i]
            label.destroy()

    # Set Paddings
    def setPadding(self):
        for child in self.win.winfo_children():
            child.grid_configure(padx=8, pady=4)

    # Displays a Message Box
    def _errorMsgBox(self, errorMsg):
        mBox.showerror('ERROR','HELP')

    def _infoMsgBox(self, msg):
        mBox.showinfo("Evaluation", msg)
