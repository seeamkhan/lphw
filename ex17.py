from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying for %s to %s" % (from_file, to_file)

in_file = open(from_file)
out_file = open(to_file)
in_file_data = open(from_file).read()
print in_file_data
print "The input file is %d bytes long." % len(in_file_data)

# Check if the output file exist.
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL+C to abort."
raw_input()

out_file_data = open(to_file, 'a').write('\n'+in_file_data)
print "Alright, all done."

out_file.close()
in_file.close()