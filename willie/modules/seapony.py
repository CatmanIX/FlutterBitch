"""
Seapony.py - Seapony Module
Copyright 2009, Michael Yanovich, yanovich.net

http://willie.dftba.net
"""

import random

def seapony(willie, trigger):
    """.seapony makes seaponies"""
    willie.say("http://www.youtube.com/watch?v=26p9LxaebCw")
seapony.commands = ['seapony', 'seaponies']
seapony.priority = 'medium'

if __name__ == '__main__':
    print __doc__.strip()
