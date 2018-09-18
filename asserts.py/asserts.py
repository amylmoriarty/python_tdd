x = 2
y = 1

assert x<y, "{0} should be less than {1}".format (x,y)

print(x+y)

def number_of_evens(numbers):
    return 0

def tests_are_equal (actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format (expected, actual)
    
def test_not_equal(c,d):
    assert c!=d, "Did not expect {0} but got {1}".format (c,d)
    
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format (collection, item)