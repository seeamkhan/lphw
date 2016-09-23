# import argv function from sys module
from sys import argv

# unpack argv
script, filename = argv

# First read the initial entry of the file.
txt = open(filename)
print "Here is the initial contents of the file:"
print txt.read()
txt.close()

# Now enter new data in the file.
print "Press ENTER to continue editing the file."
raw_input()
txt = open(filename, 'a')
# txt.truncate()
# new_data_list = [
#     "\n"
#     "This is first new line.",
#     "This is second new line.",
#     "I don't know, if this is even working.",
#     "Let's see.."
# ]
# new_data = '\n'.join(new_data_list)
print "How many lines you need to enter: "
new_line_numbers = int(raw_input())
for i in xrange(new_line_numbers):
    new_data = raw_input('Write down the new contents here and press ENTER: ')
# print "Here your file %r:" %filename
# print "Now entering new contents in the file...."
    txt.write("\n"+new_data)
print "Writing new data has been completed."
txt.close()

# Read the file to see the new entries.
txt = open(filename)
print "Here is the updated contents of the file:"
print txt.read()
txt.close()