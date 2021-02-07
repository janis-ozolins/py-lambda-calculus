from bool import TRUE
from bool import FALSE

CONS = lambda a: lambda b: lambda s: s(a)(b)

data = CONS(1)(2)
assert data(TRUE) == 1
assert data(FALSE) == 2

CAR = lambda x: x(TRUE)
CDR = lambda x: x(FALSE)

assert CAR(data) == 1
assert CDR(data) == 2
