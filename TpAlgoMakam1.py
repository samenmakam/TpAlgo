"""MAKAM SAMEN SAMUEL

La classe Fraction permet de représenter des fractions mathématiques. Elle possède un constructeur qui prend un numérateur et un dénominateur en paramètres. La classe offre également une méthode pour afficher la fraction sous forme de chaîne de caractères et une méthode pour vérifier si deux fractions sont égales. Le programme crée quatre instances de la classe Fraction avec différentes valeurs et imprime leur représentation à l'écran.

"""


class Fraction :
    def __init__(self,num, den,):
        assert den > 0
        self.num = num
        self.den = den
    def __str__(self):
        if self.den == 1 :
            
            return str(self.num)
        else :
            return (str(self.num) + "/" + str(self.den))
    def __egalite__(self,other) :
        if self.num*other.den == self.den * other.num :
            return True
        else :
            return False
   
F1,F2,F3,F4 = Fraction(3,4) , Fraction(-8,1) , Fraction(2,3), Fraction(21,28)
print(F1)
print(F2)
print(F3)
print(F4)

print(F1.__egalite__(F3))
print(F2.__egalite__(F3))
print(F4.__egalite__(F4))
print(F4.__egalite__(F2))



