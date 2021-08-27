# https://projecteuler.net/problem=33
# Digit cancelling fractions

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator 
and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''


from fractions import Fraction


def main():

    calculated_list = []
    shortcut_list = []
    shortcut_reduced_list = []

    for numerator in range(10,100):
        for denonimator in range(10,100):
            if (numerator >= denonimator):
                continue

            # check to see if they have a digit in common
            numerator_list = [ char for char in str(numerator) ]
            denominator_list = [ char for char in str(denonimator) ]

            for n_elem in numerator_list:
                for d_elem in denominator_list:
                    if (n_elem == d_elem): # a common digit

                        modified_numerator = int(str(numerator).replace(n_elem, '', 1))
                        modified_denominator = int(str(denonimator).replace(d_elem, '', 1))
                        if (modified_numerator == 0) or (modified_denominator == 0):
                            continue  

                        reduced_modified_fraction = Fraction(modified_numerator, modified_denominator)
                        reduced_modified_numerator = reduced_modified_fraction.numerator
                        reduced_modified_denominator = reduced_modified_fraction.denominator
                        # reduced_modified_numerator, reduced_modified_denominator = reduceFraction(modified_numerator, modified_denominator)

                        correct_fraction = Fraction(numerator, denonimator)
                        correct_numerator = correct_fraction.numerator
                        correct_denominator = correct_fraction.denominator
                        # correct_numerator, correct_denominator = reduceFraction(numerator, denonimator)

                        # check for triviality
                        if ('0' in str(numerator)) or ('0' in str(denonimator)):
                            continue
            
                        if (reduced_modified_numerator != correct_numerator) or (reduced_modified_denominator != correct_denominator):
                            continue

                        shortcut_list.append((modified_numerator, modified_denominator))
                        shortcut_reduced_list.append((reduced_modified_numerator, reduced_modified_denominator))
                        calculated_list.append((correct_numerator, correct_denominator))


    num_product = 1
    den_product = 1
    for n, d in calculated_list:
        num_product *= n  
        den_product *= d 
    final_product_fraction = Fraction(num_product, den_product)

    print(f'Final Fraction: {final_product_fraction.numerator}/{final_product_fraction.denominator}')

    return()



if __name__ == "__main__":
    main()