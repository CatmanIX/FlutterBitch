"""
emote.py - Flutterbitch ponymote poster program
Kopyleft 2013, The_Catman http://catmanix.github.io/

"""

def emote(willie, trigger):
    if not trigger.group(1):
        if not trigger.group(2):
            return
        willie.say('http://soarin.cytu.be/~cyzon/emotescraper/emotes/' + trigger.group(2) + '.png')
    willie.say('http://soarin.cytu.be/~cyzon/emotescraper/emotes/' + trigger.group(1) + '.png')
emote.commands = ['emote','ponymote','es']
emote.rule = '(?:\[\]\(/([a-zA-Z0-9-!:]*)(?: ".*")?\))|(?:\\\\\\\\([a-zA-Z0-9-!:]*)(?: ".*")?)'
emote.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
