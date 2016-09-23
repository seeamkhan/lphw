def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese." % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party."
    print "Get a blanket.\n"

print "We can just give the function number directly."
cheese_and_crackers(20, 30)

print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside it:"
cheese_and_crackers(5+9, 11+7)

print "And we can combine two variable and math:"
cheese_and_crackers(amount_of_cheese+5, amount_of_crackers+60)

print "We are now taking input from users:"
cheese_and_crackers(int(raw_input('amount of cheese: ')), int(raw_input('amount of crackers: ')))