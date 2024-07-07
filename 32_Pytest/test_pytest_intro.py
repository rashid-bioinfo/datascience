# It is used to test methods written in pytest_intro.py file, 
# file: test_pytest_intro.py

import pytest_intro as pti
# To skip a particular function from being tested
import pytest
import sys

# @pytest.mark.skip(reason="I dont want to run this function at the moment")

# to skip test in case of a particular condition for example, do not test this method,
# if python version is different
# @pytest.mark.skipif(sys.version_info > (3,5), reason="This function need to be tested with lower version of python")
def test_calc_total():
    total = pti.calc_total(4,5)
    assert total == 9

def test_calc_mult():
    mult = pti.calc_mult(9,5)
    assert mult == 45