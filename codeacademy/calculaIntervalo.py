# Calculando Intervalos com 
# Controle de Fluxo.

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif 90 > grade >= 80:
        return "B"
    elif 80 > grade >= 70:
        return "C"
    elif 70 > grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)