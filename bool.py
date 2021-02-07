# Boolean  

def TRUE(x):
  return lambda y: x

assert TRUE("first")("second") == "first"

def FALSE(x):
  return lambda y: y

assert FALSE("first")("second") == "second"

def NOT(x):
  return x(FALSE)(TRUE)

assert NOT(TRUE) == FALSE
assert NOT(FALSE) == TRUE

def AND(x):
  return lambda y: x(y)(x)

assert AND(TRUE)(FALSE) == FALSE
assert AND(FALSE)(TRUE) == FALSE
assert AND(FALSE)(FALSE) == FALSE
assert AND(TRUE)(TRUE) == TRUE

def OR(x):
  return lambda y: x(x)(y)

assert OR(TRUE)(FALSE) == TRUE
assert OR(FALSE)(TRUE) == TRUE
assert OR(FALSE)(FALSE) == FALSE
assert OR(TRUE)(TRUE) == TRUE

def XOR(x):
  return lambda y: AND(NOT(AND(x)(y)))(OR(x)(y))

assert XOR(TRUE)(FALSE) == TRUE
assert XOR(FALSE)(TRUE) == TRUE
assert XOR(FALSE)(FALSE) == FALSE
assert XOR(TRUE)(TRUE) == FALSE
