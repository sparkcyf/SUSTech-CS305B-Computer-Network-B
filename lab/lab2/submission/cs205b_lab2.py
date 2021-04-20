
def HiPython():
    print("hi, I’m programing in \"python\"")


def find_max_min(list):
    list_max = max(list)
    list_min = min(list)
    return list_max, list_min

class cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        return self.name + " meow"