import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all the fractions in the expression, including signs
        fractions = re.findall('[+-]?\\d+/\\d+', expression)
        
        # Initialize numerator and denominator of the result
        numerator = 0
        denominator = 1
        
        # Process each fraction
        for fraction in fractions:
            # Extract numerator and denominator
            num, denom = map(int, fraction.split('/'))
            
            # Calculate the new numerator and denominator for the result
            numerator = numerator * denom + num * denominator
            denominator *= denom
        
        # Calculate GCD to simplify the fraction
        common_divisor = gcd(abs(numerator), denominator)
        
        # Simplify the fraction
        numerator //= common_divisor
        denominator //= common_divisor
        
        # Return the result as a string
        return f"{numerator}/{denominator}"
