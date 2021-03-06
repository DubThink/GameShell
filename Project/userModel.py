__author__ = 'JoãoGabriel'
class User:
    def __init__(self, name, userData = None):
        self.name = name
        if(userData == None):
            self.score = 0
            self.currentStage = 1
            self.rightAnswers = []
            self.wrongAnswers = []
        else:
            self.retrieveData(userData)

    def retrieveData(self, userData):
        scoreLine = userData[0] #Line with the Score
        divide = scoreLine.split(": ")
        self.score = int(divide[1]) #Number, after the ": "

        stageLine = userData[1] #Line with the Current Stage
        divide = stageLine.split(": ")
        self.currentStage = int(divide[1]) #Number, after the ": "

        self.rightAnswers = []
        singleAnswer = ""
        open = False
        for char in userData[2]: #Line with the Right Answers
            if char != "'" and open:
                singleAnswer += char

            if char == "'" and not open:
                open = True
            elif char == "'" and open:
                open = False
                self.rightAnswers.append(str(singleAnswer))
                singleAnswer = ""

        self.wrongAnswers = [] #Line with the Wrong Answers
        singleAnswer = ""
        open = False
        for char in userData[3]: #Line with the Right Answers
            if char != "'" and open:
                singleAnswer += char

            if char == "'" and not open:
                open = True
            elif char == "'" and open:
                open = False
                self.wrongAnswers.append(str(singleAnswer))
                singleAnswer = ""


    def __repr__(self):
        return("Name: "+self.name+"\n"+
               "Score: "+str(self.score)+"\n"+
               "Current Stage: "+str(self.currentStage)+"\n"+
               "Right Answers: "+str(self.rightAnswers)+"\n"+
               "Wrong Answers: "+str(self.wrongAnswers)+"\n")