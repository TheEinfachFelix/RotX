from msilib.schema import Binary


abc = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

class rot:
    def __init__(self, input, rot = 0, array = abc, multi = 2) -> None:
        self.input = input 
        self.rot = rot
        self.out = ""
        self.dicti = array
        self.multiplier = multi#set this to 1 if you want to ignore lower and higer case of the input(dont use this with the default array)
        if self.rot == "*":
            self.rot = 0
            self.all()
        else:
            self.rot = int((self.rot - 1) * self.multiplier)
            print(self.convert(self.rot))

#finds the position of an element in an array
    def finder(self, array, tofind) -> int:
        for element in range(len(array)):
            if array[element] == tofind:
                return element
        return False

#does the magic
    def convert(self, rot) -> str:
        self.out = ""
        for i in self.input:
            partout = self.finder(self.dicti,i) + rot
            #print(partout)
            while partout >= len(self.dicti):
                partout -= len(self.dicti)
            #print(partout)
            self.out += self.dicti[partout]
        return self.out

#prints all posibilitis
    def all(self) -> None:
        for i in range(int(len(self.dicti)/self.multiplier)+1):
            print("Rot " + str(i+1) + " : " + self.convert(self.rot))
            self.rot += self.multiplier

if __name__ == '__main__':
    rot("olbalnpialzrlpulohbzhbmnhilu",20) 
    
# "Alle_Affen_essen_Bananen"
# input("Bitte String zum convertieren eingeben:")
    