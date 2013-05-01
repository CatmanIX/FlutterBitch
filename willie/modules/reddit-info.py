"""
reddit-info.py - Willie Reddit module
Author: Edward Powell, embolalia.net
About: http://willie.dftba.net

This module provides special tools for reddit, namely showing detailed info about reddit posts
"""

import praw
import re

def setup(willie):
    regex = re.compile('(?:(?:https?://)?(?:www.)?)?(?:(?:(?:np\.)?reddit\.com/(?:(?:r/[_\-A-Za-z\d]+/comments)|(?:tb)))|redd\.it)/([_\-A-Za-z\d]+)')
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
    try:
        author = s.author.name
    except AttributeError:
        author = "14[deleted]"
    if s.over_18:
        message = '05[NSFW] ' + message + ' 05[NSFW]'
        #TODO implement per-channel settings db, and make this able to kick
    message = message +' | ' + str(s.ups-s.downs)+' points (04+'\
                      +str(s.ups)+'|12-'+str(s.downs)+') | '+str(s.num_comments)\
                      +' comments | Posted by '+author
    #TODO add creation time with s.created
    willie.say(message)

rpost_info.rule = '.*(?:(?:https?://)?(?:www.)?)?(?:(?:(?:np\.)?reddit\.com/(?:(?:r/[_\-A-Za-z\d]+/comments)|(?:tb)))|redd\.it)/([_\-A-Za-z\d]+)'

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
