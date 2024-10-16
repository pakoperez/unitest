
from src.main import add
def test_add():
    assert add(2, 5) == 7
def test_decimal():    
    assert add(2.5, 3.5) == 6
def test_combinado():    
    assert add(2, 3.5) == 5.5
def test_error():    
    assert add(2, "texto") == "error"  

