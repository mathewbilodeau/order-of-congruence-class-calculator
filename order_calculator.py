class CongruenceClass():
    def __init__(self, unit, modulus):
        self.unit = unit
        self.modulus = modulus
        self.exponent = 1

        
    def __str__(self):
        return "[" + str(self.unit) + "]^" + str(self.exponent) + " (mod " + str(self.modulus) + ")"
    
        
def find_order(congruence_class):
    value = congruence_class.unit ** congruence_class.exponent
    reduced_value = value

    while (reduced_value >= congruence_class.modulus):
        reduced_value -= congruence_class.modulus
    
    print(str(congruence_class) + " = [" + str(value) + "]" + " = [" + str(reduced_value) + "]")
        
    if value % congruence_class.modulus == 1:
        print("The order is " + str(congruence_class.exponent) + "\n")
    else:
        congruence_class.exponent += 1
        find_order(congruence_class)
    

def main():
    while True:
        unit = int(input("Unit? "))
        modulus = int(input("Modulus? "))
        congruence_class = CongruenceClass(unit, modulus)
        find_order(congruence_class)


if __name__ == "__main__":
    main()
