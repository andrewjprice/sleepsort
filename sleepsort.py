import sys, ast
from typing import List
from threading import Thread
from time import sleep

class SleepSort(object):
    def __init__(self):
        pass
    
    def sort(self, nums: List[int]) -> List[int]:
        print('Sorting...')
        result = []
        for num in nums:
            thread = Thread(target=self.threading, args=(num, result))
            thread.start()
        while len(result) != len(nums): continue
        return result
    
    def threading(self, i, result):
        sleep(i)
        result.append(i)

if __name__ == '__main__':
    sleepsort = SleepSort()
    print(sleepsort.sort(ast.literal_eval(sys.argv[1])))