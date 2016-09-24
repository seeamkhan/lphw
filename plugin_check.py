import mmap


success_plugin_string = '.vip: Load ok. Init ok.'
fail_plugin_string = '.vip: Load failed. Init failed.'
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

data = open('test_log.txt').read()
count_success = data.count(success_plugin_string)
print "Number of plugins successfully loaded: %d" % count_success

count_fail = data.count(fail_plugin_string)
print "Number of plugins failed to load: %d" %count_fail
