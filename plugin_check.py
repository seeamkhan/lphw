import mmap


plugin_string = ".vip: Load ok. Init ok."
not_a_plugin_string = "Go to hell."

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

print "Counting Load ok and Init ok."
data = open('test_log.txt').read()
count = data.count(plugin_string)
print "Number of successfull plugins: %d" % count