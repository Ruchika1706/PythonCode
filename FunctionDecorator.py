def test(fun):
    def wrapper():
        print "Hi"
        print fun("Ruchika")
        print "Bye"
    return wrapper()

@test
def fun(name):
    return name