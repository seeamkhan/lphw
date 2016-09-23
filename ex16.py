from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."
new_inputs_list = [
    raw_input("line 1: "),
    raw_input("line 2: "),
    raw_input("line 3: ")
]
new_inputs_str = '\n'.join(new_inputs_list)
print "I'm going to write those to the file."
target.write(new_inputs_str)

print "And finally, we close it"
target.close()