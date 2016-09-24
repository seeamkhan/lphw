# with open("test_log.txt") as f:
#     for line in f:
#         if "test" in line:
#              print line


error = 'ERROR'
test = "test"
success_plugin_string = '.vip: Load ok. Init ok.'

def count_keywords(keywords):
    data = open('test_log.txt')
    count = 0
    for line in data:
        if keywords in line:
            count =  count+1
            # print line
    print "Found %d '%s' in the file." % (count, keywords)

count_keywords(test)
count_keywords(error)
count_keywords(test)