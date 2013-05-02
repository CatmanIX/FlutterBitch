"""
reddit-info.py - Willie Reddit module
Author: Edward Powell, embolalia.net
About: http://willie.dftba.net

This module provides special tools for reddit, namely showing detailed info about reddit posts
"""

import praw
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def setup(willie):
    regex = re.compile('(?:(?:https?://)?(?:www\.)?(?:\w\w(?:\-\w\w))?)?(?:(?:reddit\.com/(?:(?:r/\w+/comments)|(?:tb)))|redd\.it)/(\w+)')
    if not willie.memory.contains('url_exclude'):
        willie.memory['url_exclude'] = [regex]
    else:
        exclude = willie.memory['url_exclude']
        exclude.append(regex)
        willie.memory['url_exclude'] = exclude

def rpost_info(willie, trigger):
    r = praw.Reddit(user_agent='phenny / willie IRC bot - see dft.ba/-williesource for more')
    s = r.get_submission(submission_id=trigger.group(1))
    
    message = s.title
    if s.is_self: message = message + ' (self.' + s.subreddit.display_name + ')'
    else: message = message + ' | /r/' + s.subreddit.display_name

    if s.author is not None:
        author = s.author.name
    else: author = '14[deleted]'

    if s.over_18:
        message = '05[NSFW] ' + message + ' 05[NSFW]'
        #TODO implement per-channel settings db, and make this able to kick

    rd = relativedelta(datetime.utcnow(),
        datetime.utcfromtimestamp(s.created_utc))
    time = 0
    units ='ms'

    if rd.microseconds:
        time = str(rd.microseconds / 1000)
    if rd.seconds:
        time = rd.seconds
        units = ' second'
    if rd.minutes:
        time = rd.minutes
        units = ' minute'
    if rd.hours:
        time = rd.hours
        units = ' hour'
    if rd.days:
        time = rd.days
        units = ' day'
    if rd.months:
        time = rd.months
        units = ' month'
    if rd.years:
        time = rd.years
        units = ' year'
    if time != 1 and units != 'ms':
        units = units + 's'

    votes = s.ups - s.downs
    points_plural = ''
    if votes != 1: points_plural = 's'
    
    comments_plural = '' 
    if s.num_comments != 1: comments_plural = 's'
         
    message = ('%s | %d point%s (04+%d/12-%d) | %d comment%s | Submitted %d%s ago by %s'
        % (message, votes, points_plural, s.ups, s.downs, s.num_comments, comments_plural,
        time, units, author))  

    willie.say(message)

rpost_info.rule = '.*(?:(?:https?://)?(?:www\.)?(?:\w\w(?:\-\w\w))?)?(?:(?:reddit\.com/(?:(?:r/\w+/comments)|(?:tb)))|redd\.it)/(\w+)'

def redditor_info(willie, trigger):
    """Show information about the given Redditor"""
    commanded = re.match(willie.config.prefix+'.*', trigger)
    r = praw.Reddit(user_agent='phenny / willie IRC bot - see dft.ba/-williesource for more')
    try:
        u = r.get_redditor(trigger.group(2))
    except:
        if commanded:
            willie.say('No such Redditor.')
        return
        #Fail silently if it wasn't an explicit command.
    
    message = '[REDDITOR] '+u.name
    if commanded: message = message + ' | http://reddit.com/u/'+u.name
    if u.is_gold: message = message + ' | 08Gold'
    if u.is_mod: message = message + ' | 05Mod'
    message = message + ' | Link: '+str(u.link_karma)+ ' | Comment: '+str(u.comment_karma)
    
    #TODO detect cake day with u.created
    willie.say(message)
#If you change this, you'll have to change some things above.
redditor_info.commands = ['redditor']

def auto_redditor_info(willie, trigger):
    redditor_info(willie, trigger)
#If you change the groups here, you'll have to change some things above.
auto_redditor_info.rule = '.*http(?:s)?://(?:www\.)?reddit\.com/u(ser)?/([\w-]+).*'
