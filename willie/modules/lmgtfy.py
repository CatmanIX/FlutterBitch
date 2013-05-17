"""
lmgtfy.py - Willie Let me Google that for you module
Copyright 2013, Dimitri Molenaars http://tyrope.nl/
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net/
"""
import urllib

def issue(willie, trigger):
    """Let me just... google that for you."""
    #No input
    if not trigger.group(2):
        return willie.say('http://google.com/')
    encoded = urllib.urlencode(dict(q=trigger.group(2)))
    willie.say('http://lmgtfy.com/?' + encoded)
issue.commands = ['lmgtfy','lmgify','gify','gtfy']
issue.rule = '^dye(\s*)(.*)'
issue.priority = 'medium'

if __name__ == '__main__':
    print __doc__.strip()

