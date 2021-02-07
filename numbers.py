from data import * 

# Number represents iterations of calling parameter
# Reverse recursion with limited depth

ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
# ...


# For validation
def money(x):
  return x + ['1$']

# execute 3 time money function with initial param [] (no money)
assert THREE(money)([]) == ['1$','1$','1$']
assert ONE(money)([]) == ['1$']

# because outer function is cumulative THREE(TWO) is 2^3 = 8 
assert THREE(TWO)(money)([]) == ['1$','1$','1$','1$',     '1$','1$','1$','1$']

# The same as FALSE logically
ZERO = lambda f: lambda x: x

# Work zero hours you get no money
assert ZERO(money)([]) == []
# 3^0 is 1, still don't understand how!
# Just return money VS just return []
assert ZERO(THREE)(money)([]) == ['1$']
assert THREE(ZERO)(money)([]) == []

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

assert SUCC(ZERO)(money)([]) == ['1$']
assert SUCC(THREE)(money)([]) == ['1$','1$','1$','1$']
assert SUCC(SUCC(ZERO))(money)([]) == ['1$','1$']

ADD = lambda x: lambda y: y(SUCC)(x)

assert ADD(ONE)(ONE)(money)([]) == ['1$','1$']
assert ADD(TWO)(THREE)(money)([]) == ['1$','1$','1$','1$','1$']

MUL = lambda x: lambda y: lambda f: y(x(f))

assert MUL(TWO)(THREE)(money)([]) == ['1$','1$','1$','1$','1$','1$']

# Predecessor is excercise in logic that we can calculate it but impractival
PRED_T = lambda a: CONS(SUCC(CAR(a)))(CAR(a))

pred_three = THREE(PRED_T)(CONS(ZERO)(ZERO))
assert CAR(pred_three)(money)([]) == ['1$','1$','1$']
assert CDR(pred_three)(money)([]) == ['1$','1$']

PRED = lambda a: CDR(a(PRED_T)(CONS(ZERO)(ZERO)))

assert PRED(THREE)(money)([]) == ['1$','1$']
# 0 predecessor is 0
assert PRED(ZERO)(money)([]) == []

SUB = lambda x: lambda y: y(PRED)(x)

assert SUB(THREE)(ONE)(money)([]) == ['1$','1$']

ISZERO = lambda n: n(lambda f: FALSE)(TRUE)

assert ISZERO(THREE)('1$')(None) == None
assert ISZERO(ZERO)('1$')(None) == '1$'

# Will blow up because eagerly executing both branches
FACT = lambda n: ISZERO(n)\
  (ONE)\
  (MUL(n)(FACT(PRED(n))))

LAZY_TRUE = lambda x: lambda y: x()
LAZY_FALSE = lambda x: lambda y: y()
ISZERO = lambda n: n(lambda f: LAZY_FALSE)(LAZY_TRUE) 

FACT = lambda n: ISZERO(n)\
  (lambda: ONE)\
  (lambda: MUL(n)(FACT(PRED(n))))

assert FACT(THREE)(money)([]) == ['1$','1$','1$',     '1$','1$','1$']

