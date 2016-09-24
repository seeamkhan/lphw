def add(a, b):
    print "Adding %d and %d" % (a, b)
    return a+b

def sub(a, b):
    print "Subtracting %d from %d" %(b, a)
    return a-b

def mult(a, b):
    print "Multiplying %d and %d" %(a, b)
    return a*b

def div(a, b):
    print "Divide %d and %d" % (a, b)
    return a/b


print "Let's do match with some functions."
age = add(50, 25)
height = sub(60, 30)
weight = mult(10, 7)
iq = div(50, 2)

print "Age: %d \n Height: %d \n Weight: %d \n IQ: %d" % (age, height, weight, iq)

print "Here is the puzzle:"
what = add(age, sub(height, mult(weight, div(iq, 2))))
print "That becomes %d. Can you do it by hand?" % what