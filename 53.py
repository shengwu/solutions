for i in range(10):
    print 2**len(filter(lambda x: x in 'TDLF', raw_input()))
