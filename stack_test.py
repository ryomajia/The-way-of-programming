__author__ = 'juliajia'

def test_stack():
    from day2 import stack
    a = stack("test")
    a.pop()
    assert (a.errormessage=="error")
    a.push(4)
    assert (a.size()==1)
    assert (a.top()==4)
    a.push(2)
    assert (a.size()==2)
    assert (a.top()==2)
    a.pop()
    assert (a.size()==1)
    assert (a.top()==4)

