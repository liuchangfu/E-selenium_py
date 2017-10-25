from  count import Count

class CountTest():
    def test_add(self):
        try:
            j = Count(2,3)
            add = j.add()
            assert (add == 6),'ERROR'
        except AssertionError as msg:
            print(msg)
        else:
            print('Pass!')

mytest= CountTest()
mytest.test_add()