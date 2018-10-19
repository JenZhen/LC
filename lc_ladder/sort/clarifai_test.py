#!/usr/local/bin/python3

import time

class HitCounter(object):

    def __init__(self, interval):
        # @interval is a number in milli-second (int type).
        self.initTime = int(time.time() * 1000)
        self.interval = interval
        self.ttl = 0
        self.hitList = []

    def hit(self):
        curTime = int(time.time() * 1000)
        self.ttl += 1
        self.hitList.append((curTime, self.ttl))

    def count(self):
        curTime = int(time.time() * 1000)
        tmpTime = curTime - self.interval
        # endTime = self.hitList[-1][0]
        if len(self.hitList) == 0:
            return 0
        endCnt = self.hitList[-1][1]
        # find exact start time in hitlist
        startCnt = None

        if tmpTime <= self.initTime:
            startCnt = 0
        else:
            startCnt = self._getStartTime(self.hitList, tmpTime)

        return endCnt - startCnt

    def _getStartTime(self, hitList, target):
        st, end = 0, len(hitList) - 1
        while st + 1 < end:
            mid = st + (end - st) // 2
            midTime = hitList[mid][0]
            if midTime < target:
                st = mid
            elif midTime > target:
                end = mid
            else:
                return hitList[mid][1]
        if hitList[end][0] <= target:
            return hitList[end][1]
        else:
            return hitList[start][1]

hc = HitCounter(1000)
count = hc.count()
print("%s: 0" %hc.count())
hc.hit()
time.sleep(0.5)
hc.hit()
print("%s: 2" %hc.count())
time.sleep(2)
print("%s: 0" %hc.count())

"""
t0 : 0
t1, hit()
---
t2, hit()
--
t3. count()
    t3 - interval

0,1,1.5,3,4,5
"""
