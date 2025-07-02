"""

"""
class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st1 = {"cars": st1[0], "name": st1[1]}
        self.st2 = {"cars": st2[0], "name": st2[1]}
        
    def turngreen(self):
        if self.st1["cars"] == 0 and self.st2["cars"] == 0:
            return None

        if self.st1["cars"] > self.st2["cars"]:
            name = self.st1["name"]
            self.st1["cars"] = 0
            return name

        elif self.st2["cars"] > self.st1["cars"]:
            name = self.st2["name"]
            self.st2["cars"] = 0
            return name

        else:
            return None