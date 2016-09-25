from sys import argv
import itertools
import mmap

script, filename = argv
data = open(filename).read()

success_plugin_string = '.vip: Load ok. Init ok.'
load_init_fail_plugin_string = '.vip: Load failed. Init failed.'
load_fail_plugin_string = '.vip: Load failed. Init ok.'
init_fail_plugin_string = '.vip: Load ok. Init failed.'

not_a_plugin_string = "Go to hell."
num_lines = sum(1 for line in open(filename))
print num_lines

# print "This is the first attempt for the string findings."
# f = open('test_log.txt')
# s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# if s.find(plugin_string) != -1:
#     print "Plugin loaded successfully."
# if s.find(not_a_plugin_string) != -1:
#     print("Something is wrong with this plugin.")


# print "Going for another solution."
# f = open('test_log.txt', 'r')
# lines = f.read()
# answer = lines.find(plugin_string)
# test = lines.find('test')
# print answer
# print test



# count_success = data.count(success_plugin_string)
# print "Number of plugins successfully loaded: %d" % count_success
#
# count_fail = data.count(fail_plugin_string)
# print "Number of plugins failed to load: %d" %count_fail

def count_keywords(keywords):
    error_list = []
    f = open(filename)
    count = 0
    for i, line in enumerate(f):
    # for line in f:
        if keywords in line:
            count =  count+1
            error_list.append(line)
            # print line
            print i, line
    print "Found %d '%s' in the file." % (count, keywords)
    print "Here's the error list: "
    print '\n'.join(error_list)

# count_keywords(success_plugin_string)
count_keywords(load_init_fail_plugin_string)
# count_keywords(load_fail_plugin_string)
# count_keywords(init_fail_plugin_string)