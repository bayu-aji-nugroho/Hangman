import random as rd

class Proses():
    finalData = []
    wrongpoint = 0
    vocab_list = [
    "Ability", "Absent", "Achieve", "Adventure", "Ambition", "Ancient", "Approve", "Arrange", "Atmosphere", "Balance",
    "Behavior", "Benefit", "Biology", "Border", "Bright", "Campaign", "Capable", "Celebrate", "Challenge", "Character",
    "Civilization", "Clever", "Comfort", "Commit", "Compete", "Complex", "Concern", "Condition", "Confidence", "Consider",
    "Construct", "Contact", "Content", "Creative", "Curious", "Debate", "Decide", "Declare", "Dedicate", "Defeat", 
    "Defense", "Deliver", "Demand", "Democracy", "Depend", "Describe", "Desire", "Determine", "Develop", "Difficult", 
    "Disagree", "Discover", "Diversity", "Divide", "Economy", "Education", "Effort", "Element", "Emotion", "Encourage",
    "Energy", "Engine", "Enjoy", "Environment", "Essential", "Establish", "Event", "Evidence", "Examine", "Experience", 
    "Experiment", "Explore", "Express", "Faith", "Famous", "Favor", "Fear", "Feature", "Focus", "Foreign", "Formal",
    "Fortune", "Freedom", "Function", "Future", "Gain", "General", "Goal", "Government", "Grace", "History", "Honor", 
    "Hope", "Human", "Hurry", "Idea", "Identity", "Ignore", "Imagine", "Improve", "Include", "Indicate", "Industry", 
    "Inspire", "Intend", "Invest", "Journey", "Justice"
    ]
    
    def __init__(self) -> None:
        self .__rand()

    def __rand(self):
        self.temporarydata = []
        while True:
            self.nomer = rd.randint(0, len(self.vocab_list) - 1)
            if self.nomer not in self.temporarydata:
                self.temporarydata.append(self.nomer)
                self.finalData.append(self.vocab_list[self.nomer])
                break
    
            

Proses = proses()
print(Proses.finalData)
