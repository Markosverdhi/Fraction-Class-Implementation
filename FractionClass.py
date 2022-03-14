try:
    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n
    class Fraction:
        def __init__(self, top, bottom):
            self.num = int(top//gcd(top,bottom))
            self.den = int(bottom//gcd(top,bottom))
            if self.den < 0:
                self.num = -(self.num)
                self.den = abs(self.den)

        def show(self):
            print("{:d}/{:d}".format(self.num, self.den))

        def __str__(self):
            return "{:d}/{:d}".format(self.num, self.den)

        def __eq__(self, other_fraction):
            first_num = self.num * other_fraction.den
            second_num = other_fraction.num * self.den

            return first_num == second_num

        def __add__(self, other_fraction):
            new_num = self.num * other_fraction.den \
            + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return (new_num // gcd(new_num, new_den)) / (new_den // gcd(new_num, new_den))

        def get_num(self):
            return self.num

        def get_den(self):
            return self.den

        def __sub__(self, other_fraction):
            new_num = self.num * other_fraction.den - self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

        def __mul__(self, other_fraction):
            new_num = self.num * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num // gcd(new_num,new_den), new_den//gcd(new_num, new_den))

        def __truediv__(self, other_fraction):
            return Fraction(self.num * other_fraction.den // gcd(self.num * other_fraction.den,
            self. den * other_fraction.num), self. den * other_fraction.num // gcd(self.num *
            other_fraction.den,self. den * other_fraction.num))

        def __gt__(self, other_fraction):
            comparable = self.__truediv__(other_fraction)
            return comparable.num > comparable.den

        def __ge__(self, other_fraction):
            comparable = self.__truediv__(other_fraction)
            return comparable.num >= comparable.den

        def __lt__(self,other_fraction):
            comparable = self.__truediv__(other_fraction)
            return comparable.num < comparable.den

        def __le__(self, other_fraction):
            comparable = self.__truediv__(other_fraction)
            return comparable.num <= comparable.den

        def __ne__(self, other_fraction):
            comparable = self.__truediv__(other_fraction)
            return comparable.num != comparable.den

        def __radd__(self, other_fraction):
            new_num = self.num * other_fraction.den \
            + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

        def __iadd__(self, other_fraction,variable):
            new_num = self.num * other_fraction.den + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            variable = Fraction(new_num,new_den)
            return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

        def __repr__(self):
            return f"Fraction({str(self.num)},{self.den})"
except TypeError:
    print('Either Numerator or Denominator is not an int')

#__radd__ is a method that allows for addition between classes, even if one of the functions does not have an __add__ function.
#This is helpful when you are working with multiple different classes and need to add multiple objects together.


class Fraction2:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        if self.den < 0:
            self.num = -(self.num)
            self.den = abs(self.den)


#__iadd__ is used to both add two values and assign the sum of them a variable at the same time.
#It basically does the same thing as the += operator. Assigning doesn't happen if the thing is immutable, such as strings, numbers and tuples.

 #__repr__ is used to show a string representation of the object in question, but the difference between it and __str__ is that
 #the __str__ function is meant to be easy to be read by others, like when a user would interact with the code. __repr__ is more
 #for the use of the programmer.
