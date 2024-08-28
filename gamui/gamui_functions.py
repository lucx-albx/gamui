"""
This file it's used by the gamui.py module for the functions that had been developed for 
implemets extra functionallity that are helpfull for the correct function and checkin method
of the gamui module.
"""

#? --- START FUNCTIONS --- ?#
#! -- START FUNCTION THAT CHECK NEGATIVE NUMBER -- !#
def is_negative_number(num : int | float) -> bool:
    if num != None:
        if num >= 0:
            return False
        else:
            return True
    else:
        return False
#! -- END FUNCTION THAT CHECK NEGATIVE NUMBER -- !#
#? --- END FUNCTIONS --- ?#