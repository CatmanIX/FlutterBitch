"""
countdown.py - Willie Countdown Module
Copyright 2011, Michael Yanovich, yanovich.net
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net
"""

import datetime


def generic_countdown(willie, trigger):
    """
    .countdown <year> <month> <day> - displays a countdown to a given date.
    """
    text = trigger.group(2)
    if not text:
        willie.say("Please use correct format: .countdown 2012 12 21")
        return willie.NOLIMIT
    text = trigger.group(2).split()
    if text and (text[0].isdigit() and text[1].isdigit() and text[2].isdigit()
            and len(text) == 3):
        diff = (datetime.datetime(int(text[0]), int(text[1]), int(text[2]))
                - datetime.datetime.today())
        willie.say(str(diff.days) + " days, " + str(diff.seconds / 60 / 60)
                   + " hours and "
                   + str(diff.seconds / 60 - diff.seconds / 60 / 60 * 60)
                   + " minutes until "
                   + text[0] + " " + text[1] + " " + text[2])
    else:
        willie.say("Please use correct format: .countdown 2012 12 21")
        return willie.NOLIMIT
generic_countdown.commands = ['countdown']
generic_countdown.priority = 'low'


if __name__ == '__main__':
    print __doc__.strip()
