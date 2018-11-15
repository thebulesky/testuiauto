import unittest

import commands
class TSCache(object):

    def __init__(self):

    # suit initial

        print("case %s" % self)


    def doRequest(self):
        comm ="curl -I -s -x  localhost:8080 http://111111.cn/index.html"

        output =commands.getoutput(comm)
        rt =output.split("\r\n") [0]

        return rt



if __name__ =='__main__':

    #print  dir(TestTSCache)
    unittest.main()