'''
Created on 14.10.2015

@author: stefan
'''
import demos
import logging
import time

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    
    start = time.time()
    demos.loop_demo()
    duration = time.time() - start
    print "Duration:", duration