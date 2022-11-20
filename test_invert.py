from invert import invert
from invert_int import invert_int

# def test_invert_string():
#     inverted = invert('Marian')
#
#     assert inverted == 'nairaM'
#
# def test_invert_int():
#     try:
#         invert(1234)
#     except:
#         assert (3 == int('3'))
def add_num(a,b):
    return a + b


def test_add_number():
    assert add_num(5,5) == 10

def test_add_number_neg():
    assert add_num(-9,5) == -4

def test_add_number_divided():
    assert add_num(25/5,5) == 10

def test_add_number_mulitply_bullshit():
    assert add_num(5*5, 5) == 10

test_add_number()
test_add_number_neg()
test_add_number_divided()
test_add_number_mulitply_bullshit()



#
#
#
# invert_int(2019)
