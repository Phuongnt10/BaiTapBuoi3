def hcf (nr,dr):
        nr,dr=abs(nr),abs(dr)
        r = nr%dr
        while (r != 0):
            nr=dr
            dr = r
            r =nr % dr
        return(dr) 
       
class Fraction:
    def __init__(self,nr,dr=1):
        if dr==0:
            raise ZeroDivisionError("Mẫu số không hợp lệ")
        if dr < 0:
            self.nr=nr*-1
            self.dr=dr*-1
        else:
            self.nr=nr
            self.dr=dr
        self._reduce()

   
    def __repr__(self):
        ##return "0" if self.nr == 0 else str(self.nr) if self.dr == 1 else f"{self.nr}/{self.dr}"
        if self.nr == 0:
            return "0"
        elif  self.dr == 1:
            return str(self.nr)
        else:
            return f"{self.nr}/{self.dr}"     


    def _reduce(self):
        re=hcf(self.nr, self.dr)
        if re:
            self.nr=int(self.nr/re)
            self.dr=int(self.dr/re)   
 
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)
        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

fr = Fraction(1, 3)
other = Fraction(5)
print(fr, other)

print()

print(fr + other)
print(fr - other)
print(fr * other)
print(fr / other)

print()

fr = Fraction(1, 2)
print(fr + 1)
print(fr - 1.5)
print(fr * 2)
print(fr / 2)