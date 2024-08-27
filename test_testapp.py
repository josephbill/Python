import pytest
from testapp import add,divide

def test_add():
    # assert calltomethodtobetested
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_divide():
    assert divide(10,2) == 5
    with pytest.raises(ValueError):
        divide(10,0)



# assert : this is a statement from pytest that checks on a condition and returns true if the test pass , and false 
# if it fails