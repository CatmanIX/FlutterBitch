"""
lmgtfy.py - Willie Let me Google that for you module
Copyright 2013, Dimitri Molenaars http://tyrope.nl/
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net/
"""
import urllib

def googleit(willie, trigger):
    """Let me just... google that for you."""
    #No input
    if not trigger.group(2):
<<<<<<< HEAD
        return
    encoded = urllib.urlencode(dict(q=trigger.group(2)))
    willie.say('http://lmgtfy.com/?' + encoded)
issue.commands = ['lmgtfy','lmgify','gify','gtfy']
issue.rule = '^(?:bros?,?\.?)?\s*(do you even,?\.?|dye,?\.?)\s*((?:(?:.*)(?= bros?\??))|(?:(?:.*)(?=bros?\??))|(?:.*)(?=\?)|(?:.*))'
issue.priority = 'medium'
=======
        return willie.say('http://google.com/')
    willie.say('http://lmgtfy.com/?q='+trigger.group(2).replace(' ','+'))
googleit.commands = ['lmgtfy','lmgify','gify','gtfy']
googleit.priority = 'medium'
>>>>>>> 1e0cdcaeefa243980bb29c074456d5e33cf1abf5

if __name__ == '__main__':
    print __doc__.strip()

