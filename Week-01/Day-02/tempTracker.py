import unittest


class TempTracker(object):

    
    def __init__(self):
        self.tempArray=[0]*111
        self.size = 0
        self.minTemp =111
        self.maxTemp = -1
        self.total = 0
        self.mean = None
        self.maxMode = 0
        self.mode = None

    def insert(self, temperature):
        self.tempArray[temperature]+=1
        self.size+=1
        if temperature<self.minTemp:
            self.minTemp=temperature
        if temperature>self.maxTemp:
            self.maxTemp=temperature
        self.total+=temperature
        if self.tempArray[temperature]>self.maxMode:
            self.maxMode=self.tempArray[temperature]
            self.mode=temperature

    def get_max(self):
        maxTemp=self.maxTemp
        if maxTemp==-1:
            return None
        return maxTemp

    def get_min(self):
        minTemp=self.minTemp
        if minTemp==111:
            return None
        return minTemp

    def get_mean(self):
        self.mean=float(self.total/self.size)
        return self.mean

    def get_mode(self):
        return self.mode

# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='maxTemp ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='minTemp ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='maxTemp ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='minTemp ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='maxTemp ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='minTemp ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='maxTemp ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='minTemp ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)