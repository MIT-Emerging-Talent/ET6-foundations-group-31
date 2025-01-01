#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module that gives a grade.

Module contents:
    - my_grade: gives the equalevent grade for a 4.0 scale GPA.
Created on xx xx xx
@author: Raneem Rami
"""
def my_grade (average: float) -> str:
    """ Gives the grade (A,B,B+,C,D,F) and a grade description for a 4.0 scale GPA.
    Parameters:
        average: float, your GPA to get it evaluated to your grade, must not be greater than 4.0
        
    Returns -> str: your final grade and its description
        
    Raises:
        AssertionError: if argument is not a float
        
    Examples:
    >>> my_grade(3.6)
    'Excellent (A)'

    >>> my_grade(3.0)
    'Very Good (B+)'

    >>> my_grade(2.9)
    'Good (B)'

    >>> my_grade(1.9)
    'Basic (D)'

    >>> my_grade(0.0)
    'Fail (F)'
    """
    assert isinstance(average, float), "input must be a float"
    assert average <= 4.0, "input must not be greater than 4.0"

    if 3.6 <= average <=4.0:  # Excellent (A) for GPA from 3.6 to 4.0
        return "Excellent (A)"

    if 3.0 <= average < 3.6:  # Very Good (B+) for GPA from 3.0 to 3.5
        return "Very Good (B+)"

    if 2.8 <= average < 3.0:  # Good (B) for GPA from 2.8 to 3.0
        return "Good (B)"

    if 2.0 <= average < 2.8:  # Satisfactory (C) for GPA from 2.0 to 2.8
        return "Satisfactory (C)"

    if 1.6 <= average < 2.0:  # Basic (D) for GPA from 1.6 to 2.0
        return "Basic (D)"

    if 0.0 <= average < 1.6:  # Fail (F) for GPA less than 1.6
        return "Fail (F)"
