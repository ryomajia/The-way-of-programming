__author__ = 'juliajia'


def test_queue():
    from day3 import queue
    a = queue("test")
    a.pop()
    assert (a.errormessage=="error")
    a.push(4)
    assert (a.size()==1)
    assert (a.front()==4)
    assert (a.back()==4)
    a.push(2)
    assert (a.size()==2)
    assert (a.front()==2)
    assert (a.back()==4)
    a.pop()
    assert (a.size()==1)
    assert (a.front()==2)
    assert (a.back()==2)

if __name__=='__main__':
    test_queue()