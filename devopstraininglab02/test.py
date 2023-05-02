#from DevOpsTrainingsLab02.src.__init__ import *
from .__init__ import *

def test_function_init():
    assert function_init() == 0

def test_print_age():
    assert "I am 38 years old" in print_age(38)
