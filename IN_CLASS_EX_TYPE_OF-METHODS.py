class Fraction:

#----------------------------------------INITIALIZER---------------------------------------------------------

    def __init__(self,num,den):
        self.num = num #Instantiates Numerator
        self.den = den #Instantiates Denomirator

#----------------------------------------RETURN FRACTION----------------------------------------------------

    def get_fraction(self):
        return self.num,self.den #return numerator and denomirator as a tuple.
    
#----------------------------------------SOLVE FRACTION------------------------------------------------------
    
    def get_decimal(self):
        return self.num / self.den #Returns decimal equivalent of the fraction.
    
#---------------------------------------FIND HCF----------------------------------------------------------------

    @staticmethod
    def find_HCF(numerator, denominator):
        factors_of_numerator = []  # Initialize an empty list to store factors of numerator
        factors_of_denominator = []  # Initialize an empty list to store factors of denominator

         # Find all factors of the numerator
        for factor in range(1, numerator + 1):
            if numerator % factor == 0:
                factors_of_numerator.append(factor)

        # Find all factors of the denominator
        for factor in range(1, denominator + 1):
            if denominator % factor == 0:
                factors_of_denominator.append(factor)

        # Iterate from the largest possible index to 0 to find the highest common factor
        for highest_factor_index in range(len(factors_of_numerator) - 1, -1, -1):
            if factors_of_numerator[highest_factor_index] in factors_of_denominator:
                return factors_of_numerator[highest_factor_index]  # Return the highest common factor

        return None  # If no common factor is found, return None (though in practice, 1 should always be a common factor)
    
#----------------------------------------SIMPLIFY THE FRACTION--------------------------------------------------

    def simplify(self):
        
        HCF = self.find_HCF(self.num,self.den)
        self.num = self.num // HCF
        self.den = self.den // HCF

        return self.get_fraction()

#----------------------------------------ADD FRACTIONS-----------------------------------------------------------

    def __add__(self,f):

        if self.den == f.den :
            self.num = self.num + f.num
            return self.get_decimal()
        else:
            self.num = (self.num * f.den) + (f.num * self.den)
            self.den = self.den * f.den
            return self.get_decimal()

#-----------------------------------------COMPARE FRACTIONS------------------------------------------------------

    def __gt__(self,f):
        decimal1 = self.get_decimal()
        decimal2 = f.get_decimal()
        if decimal1 > decimal2:
            return True
        else:
            return False
            
#-----------------------------------------CLIENT CODE---------------------------------------------------------

f1 = Fraction(4,16)
f2 = Fraction(3,2)
print(f2 > f1)
print(f1.simplify())
print(f1 + f2)


