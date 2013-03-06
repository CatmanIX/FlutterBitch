"""
poni.py
	Outputs out a random My Littly Pony episode.

Copyright 2012, miggyb
Licensed under the WTFPL

/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */

"""

import random
import datetime as t
import re

def poni(willie, input):
  e = Episode()
  e.part = 0
  
  # no args
  if(input.group(2) is None):
    while(e.part != 1 and len(episodes) > 0):
      e = episodes.pop(random.randint(0, len(episodes)-1))

    return willie.say(e.out())

  epCode = re.compile("s\d{1,2}e\d{1,3}") # matches s#e# where the first # is 0-99, second # is 0-999

  # args starts with an epCode
  s = epCode.match(input.group(2))

  if s is not None:
    for i in range(len(episodes)):
      if episodes[i].epCode() == s.group(0):
        return willie.say(episodes[i].out())

  return  willie.say("Error...")
# 	if(s.group(0)[1] == 1 or s.group(0)[1] == 2):
#		while(e.part != 1 or e.season != int(r.group(0)[1])):
#                	e = random.choice(episodes)
#               return willie.say("s%de%d | %s | %s" % (e.season, e.number, e.name, e.url))


poni.commands = ['poni']
poni.priority = 'high'

poni.example = "'.poni' for a random mlp episode, '.poni 1' for a random episode in season one"


# random thing that documentation told me to put in
if __name__ == "__main__":
    print __doc__.strip()


#########################
# General My Little Pony episode information
#########################

class Episode:
  def __init__(self):
    self.season = 0                      # Season number
    self.number = 0                      # Episode number (within season)
    self.name = ""
    self.url = ""
    self.drinks = 0
  def epCode(self):
    return "s%de%d" % (self.season, self.number)
  def out(self):
    return "%s | %s | Drinks: %d" % (self.epCode(), self.name, self.drinks)
  feat = []                       # Featuring these characters
  tags = []                       # Tags for episode
  dsec = ""                       # Short, spoiler-free description
  ldesc = ""                      # Long, spoiler-filled description
  part = 1                        # Part 1 of N for multipart episodes
  writers = []                    # Writers of episode
# directors = ["James Wootton"]   # Directors (only one so far, future proofing)
  date = t.date(1, 1, 1)          # Original airdate



characters = [
  "Twilight Sparkle",     # 0
  "Rainbow Dash",         # 1
  "Fluttershy",           # 2
  "Rarity",               # 3
  "Applejack",            # 4
  "Pinkie Pie",           # 5
  "Applebloom",           # 6
  "Scootaloo",            # 7
  "Sweetie Belle",        # 8
  # More to come...
]

tags = [
  "Canterlot",            # 0
  "Ponyville",            # 1
  "Appleoosa",            # 2
  "Pilot",                # 3
  "Wedding",              # 4
  "Tree",                 # 5
  "Applebuckin"           # 6
  "Cloudsdale"            # 7
  # More to come...
]

writers = [
  "Lauren Faust",         # 0
  "Amy Keating Rogers",   # 1
  "Cindy Morrow",         # 2
  "Chris Savino",         # 3
  "Meghan McCarthy",      # 4
  "Charlotte Fullerton",  # 5
  "M. A. Larson",         # 6
  "Dave Polsky",          # 7
  "Merriwether Williams", # 8
]

episodes = []

#########################
# Specific episode data
#########################

# Template
#
# s0e0 = Episode()
# episodes.append(s0e0)
# s0e0.name = ""
# s0e0.season = 0
# s0e0.number = 0
# s0e0.feat = [ 0 ]
# s0e0.tags = [ 0 ]
# s0e0.desc = ""
# s0e0.ldesc = ""
# s0e0.writers = [ 0 ]
# s0e0.date = t.date(1, 1, 1)
# s0e0.url = ""
# s0e0.drinks = 0
# 

s1e1 = Episode()
episodes.append(s1e1)
s1e1.name = "Friendship is Magic, Part 1"
s1e1.season = 1
s1e1.number = 1
s1e1.feat = [ 0, 1, 2, 3, 4, 5 ]
s1e1.tags = [ 0, 1, 3 ]
s1e1.desc = "Twilight is sent on a mission to acquire friendship after warning Princess Celestia of a potential incoming danger"
s1e1.ldesc = "First part of the original two-parter pilot. Twilight Sparkle introduced as a nerdy, friendless pony that's more or less a graduate student for Princess Celestia. She finds something in an old book about Nightmare Moon, who is set to sink the world into Eternal Night(tm). Celestia tells her to go make some friends. Ponyville and the rest of the main characters introduced for the first time. Pinkie Pie throws a party to get her fix."
s1e1.writers = [ 0 ]
s1e1.date = t.date(2010, 10, 10)
s1e1.url = "http://www.youtube.com/watch?v=Zs-_YR63mFU&hd=1"
s1e1.drinks = 28

s1e2 = Episode()
s1e2.name = "Friendship is Magic, Part 2"
episodes.append(s1e2)
s1e2.season = 1
s1e2.number = 2
s1e2.part = 2
s1e2.feat = [ 0, 1, 2, 3, 4, 5 ]
s1e2.tags = [ 0, 1, 3 ]
s1e2.desc = "Friendship is "
s1e2.ldesc = "Second part of the pilot, Twilight learns about the Elements of Harmony which are hidden in the Everfree Forest. The mane six take turns showing off their inherent character qualities. Then there's a big boss fight at the end and then Nightmare Moon changes back into Princess Luna."
s1e2.writers = [ 0 ]
s1e2.date = t.date(2010, 10, 22)
s1e2.url = "http://www.youtube.com/watch?v=w8NTGwNYreA&hd=1"
s1e2.drinks = 25

s1e3 = Episode()
s1e3.name = "The Ticket Master"
episodes.append(s1e3)
s1e3.season = 1
s1e3.number = 3
s1e3.feat = [ 0, 1, 2, 3, 4, 5 ]
s1e3.tags = [ 1 ]
s1e3.desc = "Twilight receives two tickets to the Grand Galloping Gala and must decide what to do with the extra ticket"
s1e3.ldesc = "Twilight Sparkle receives two tickets to the Grand Galloping Gala from Princesss Celestia. Since Spike is not real people, she must decide what to do with the extra ticket. Her newlyfound friends act like dicks and emotionally manipulate her into returning both tickets. Celestia then gives her five extra tickets so they can all attend, except for Spike who remains a second-class citizen of Equestria."
s1e3.writers = [ 0, 1 ]
s1e3.date = t.date(2010, 10, 29)
s1e3.url = "http://www.youtube.com/watch?v=beTqsUuTMLA&hd=1"
s1e3.drinks = 31

s1e4 = Episode()
episodes.append(s1e4)
s1e4.name = "Applebuck Season"
s1e4.season = 1
s1e4.number = 4
s1e4.feat = [ 4 ]
s1e4.tags = [ 1, 6 ]
s1e4.desc = "Big Macintosh becomes injured right before Apple harvest starts so Applejack must buck all the apples by herself"
s1e4.ldesc = "Applejack must harvest an entire field of apples by herself since Big Macintosh has an injury. Her friends offer to help but none of them are good at manual labor and have no bucking experience. In contrast, everyone asks for Applejack's help with other stuff and she is incapable of saying no. Applejack learns a valuable lesson in time management."
s1e4.writers = [ 1 ]
s1e4.date = t.date(2010, 11, 5)
s1e4.url = "http://www.youtube.com/watch?v=JoXBk3NGtOQ&hd=1"
s1e4.drinks = 26

s1e5 = Episode()
episodes.append(s1e5)
s1e5.name = "Griffon the Brush-Off"
s1e5.season = 1
s1e5.number = 5
s1e5.feat = [ 5, 0 ]
s1e5.tags = [ 1, 7 ]
s1e5.desc = "Pinkie Pie becomes a third wheel as Rainbow Dash's Griffon friend from Flight School stops by for a visit"
s1e5.ldesc = ""
s1e5.writers = [ 2 ]
s1e5.date = t.date(2010, 11, 12)
s1e5.url = "http://www.youtube.com/watch?v=ETCCBL_pDYw&hd=1"
s1e5.drinks = 24

s1e6 = Episode()
episodes.append(s1e6)
s1e6.name = "Boast Busters"
s1e6.season = 1
s1e6.number = 6
s1e6.feat = [ 0 ]
s1e6.tags = [ 0 ]
s1e6.desc = "The Great and Powerful Trixie makes everypony butthurt over her larger-than-life personality" 
s1e6.ldesc = ""
s1e6.writers = [ 3 ]
s1e6.date = t.date(2010, 11, 19)
s1e6.url = "http://www.youtube.com/watch?v=ib0xumVVWCo&hd=1"
s1e6.drinks = 41

s1e7 = Episode()
episodes.append(s1e7)
s1e7.name = "Dragonshy"
s1e7.season = 1
s1e7.number = 7
s1e7.feat = [ 0 ]
s1e7.tags = [ 0 ]
s1e7.desc = ""
s1e7.ldesc = "The Mane Six must inform a sleeping dragon about zoning restrictions within the Ponyville town limits"
s1e7.writers = [ 4 ]
s1e7.date = t.date(2010, 11, 26)
s1e7.url = "http://www.youtube.com/watch?v=0gbxy46WP9U&hd=1"
s1e7.drinks = 19

s1e8 = Episode()
episodes.append(s1e8)
s1e8.name = "Look Before You Sleep"
s1e8.season = 1
s1e8.number = 8
s1e8.feat = [ 0 ]
s1e8.tags = [ 0 ]
s1e8.desc = "Rarity, Applejack and Twilight have a three-way Mexican standoff over who can force their personality on everpony else the best"
s1e8.ldesc = ""
s1e8.writers = [ 5 ]
s1e8.date = t.date(2010, 12, 3)
s1e8.url = "http://www.youtube.com/watch?v=YMaTZjjTI38&hd=1"
s1e8.drinks = 22

s1e9 = Episode()
episodes.append(s1e9)
s1e9.name = "Bridle Gossip"
s1e9.season = 1
s1e9.number = 9
s1e9.feat = [ 0 ]
s1e9.tags = [ 0 ]
s1e9.desc = "Ponyville engages in casual xenophobia. Literal and metaphorical witch hunt ensues."
s1e9.ldesc = ""
s1e9.writers = [ 1 ]
s1e9.date = t.date(2010, 12, 10)
s1e9.url = "http://www.youtube.com/watch?v=xOgYFPZx6SI&hd=1"
s1e9.drinks = 30

s1e10 = Episode()
episodes.append(s1e10)
s1e10.name = "Swarm of the Century"
s1e10.season = 1
s1e10.number = 10
s1e10.feat = [ 0 ]
s1e10.tags = [ 0 ]
s1e10.desc = "Equestria's commitment to biodegradable construction materials and organic farming practices are exposed as a viable attack vector"
s1e10.ldesc = ""
s1e10.writers = [ 6 ]
s1e10.date = t.date(2010, 12, 17)
s1e10.url = "http://www.youtube.com/watch?v=bDhoFaNNbyI&hd=1"
s1e10.drinks = 31

s1e11 = Episode()
episodes.append(s1e11)
s1e11.name = "Winter Wrap Up"
s1e11.season = 1
s1e11.number = 11
s1e11.feat = [ 0 ]
s1e11.tags = [ 0 ]
s1e11.desc = "Twilight faces an internal struggle as her desire to help Ponyville successfully transition from Winter to Spring is constrained by her ineptitude at blue collar labor."
s1e11.ldesc = ""
s1e11.writers = [ 2 ]
s1e11.date = t.date(2010, 12, 24)
s1e11.url = "http://www.youtube.com/watch?v=b4m1uDkS92o&hd=1"
s1e11.drinks = 23

s1e12 = Episode()
episodes.append(s1e12)
s1e12.name = "Call of the Cutie"
s1e12.season = 1
s1e12.number = 12
s1e12.feat = [ 0 ]
s1e12.tags = [ 0 ]
s1e12.desc = "Applebloom is frustrated with her lack of a cutie mark to the point of actually taking life advice from Rainbow Dash" 
s1e12.ldesc = ""
s1e12.writers = [ 4 ]
s1e12.date = t.date(2011, 1, 7)
s1e12.url = "http://www.youtube.com/watch?v=HsZf3vwnJzw&hd=1"
s1e12.drinks = 24

s1e13 = Episode()
episodes.append(s1e13)
s1e13.name = "Fall Weather Friends"
s1e13.season = 1
s1e13.number = 13
s1e13.feat = [ 0 ]
s1e13.tags = [ 0 ]
s1e13.desc = ""
s1e13.ldesc = ""
s1e13.writers = [ 1 ]
s1e13.date = t.date(2011, 1, 28)
s1e13.url = "http://www.youtube.com/watch?v=QsuuEyRn2OA&hd=1"
s1e13.drinks = 30

s1e14 = Episode()
episodes.append(s1e14)
s1e14.name = "Suited for Success"
s1e14.season = 1
s1e14.number = 14
s1e14.feat = [ 0 ]
s1e14.tags = [ 0 ]
s1e14.desc = "Rarity deviates from standard dress aesthetics in order to protect her friendship with the other mane six"
s1e14.ldesc = ""
s1e14.writers = [ 5 ]
s1e14.date = t.date(2011, 2, 4)
s1e14.url = "http://www.youtube.com/watch?v=shBzONopUQY&hd=1"
s1e14.drinks = 24

s1e15 = Episode()
episodes.append(s1e15)
s1e15.name = "Feeling Pinkie Keen"
s1e15.season = 1
s1e15.number = 15
s1e15.feat = [ 0 ]
s1e15.tags = [ 0 ]
s1e15.desc = ""
s1e15.ldesc = ""
s1e15.writers = [ 7 ]
s1e15.date = t.date(2011, 2, 11)
s1e15.url = "http://www.youtube.com/watch?v=3Mu5j0bHN2M&hd=1"
s1e15.drinks = 30

s1e16 = Episode()
episodes.append(s1e16)
s1e16.name = "Sonic Rainboom"
s1e16.season = 1
s1e16.number = 16
s1e16.feat = [ 0 ]
s1e16.tags = [ 0 ]
s1e16.desc = ""
s1e16.ldesc = ""
s1e16.writers = [ 6 ]
s1e16.date = t.date(2011, 2, 18)
s1e16.url = "http://www.youtube.com/watch?v=zXG7kaxB2jU&hd=1"
s1e16.drinks = 16

s1e17 = Episode()
episodes.append(s1e17)
s1e17.name = "Stare Master"
s1e17.season = 1
s1e17.number = 17
s1e17.feat = [ 0 ]
s1e17.tags = [ 0 ]
s1e17.desc = ""
s1e17.ldesc = ""
s1e17.writers = [ 3 ]
s1e17.date = t.date(2011, 2, 25)
s1e17.url = "http://www.youtube.com/watch?v=nrVB_pblgjA&hd=1"
s1e17.drinks = 25

s1e18 = Episode()
episodes.append(s1e18)
s1e18.name = "Show Stoppers"
s1e18.season = 1
s1e18.number = 18
s1e18.feat = [ 0 ]
s1e18.tags = [ 0 ]
s1e18.desc = ""
s1e18.ldesc = ""
s1e18.writers = [ 2 ]
s1e18.date = t.date(2011, 3, 4)
s1e18.url = "http://www.youtube.com/watch?v=dE-j2Lvjmuo&hd=1"
s1e18.drinks = 25

s1e19 = Episode()
episodes.append(s1e19)
s1e19.name = "A Dog and Pony Show"
s1e19.season = 1
s1e19.number = 19
s1e19.feat = [ 0 ]
s1e19.tags = [ 0 ]
s1e19.desc = ""
s1e19.ldesc = ""
s1e19.writers = [ 1 ]
s1e19.date = t.date(2011, 3, 11)
s1e19.url = "http://www.youtube.com/watch?v=_wPPrX9hXmc&hd=1"
s1e19.drinks = 19

s1e20 = Episode()
episodes.append(s1e20)
s1e20.name = "Green Isn't Your Color"
s1e20.season = 1
s1e20.number = 20
s1e20.feat = [ 0 ]
s1e20.tags = [ 0 ]
s1e20.desc = ""
s1e20.ldesc = ""
s1e20.writers = [ 0 ]
s1e20.date = t.date(2011, 3, 18)
s1e20.url = "http://www.youtube.com/watch?v=ST1df5s9SIo&hd=1"
s1e20.drinks = 24

s1e21 = Episode()
episodes.append(s1e21)
s1e21.name = "Over a Barrel"
s1e21.season = 1
s1e21.number = 21
s1e21.feat = [ 0 ]
s1e21.tags = [ 0 ]
s1e21.desc = ""
s1e21.ldesc = ""
s1e21.writers = [ 7 ]
s1e21.date = t.date(2011, 3, 25)
s1e21.url = "http://www.youtube.com/watch?v=Ys62xeriAk8&hd=1"
s1e21.drinks = 20

s1e22 = Episode()
episodes.append(s1e22)
s1e22.name = "A Bird in the Hoof"
s1e22.season = 1
s1e22.number = 22
s1e22.feat = [ 0 ]
s1e22.tags = [ 0 ]
s1e22.desc = ""
s1e22.ldesc = ""
s1e22.writers = [ 5 ]
s1e22.date = t.date(2011, 4, 8)
s1e22.url = "http://www.youtube.com/watch?v=vp19OMp-daI&hd=1"
s1e22.drinks = 22

s1e23 = Episode()
episodes.append(s1e23)
s1e23.name = "The Cutie Mark Chronicles"
s1e23.season = 1
s1e23.number = 23
s1e23.feat = [ 0 ]
s1e23.tags = [ 0 ]
s1e23.desc = ""
s1e23.ldesc = ""
s1e23.writers = [ 6 ]
s1e23.date = t.date(2011, 4, 15)
s1e23.url = "http://www.youtube.com/watch?v=teFQEMCuPl4&hd=1"
s1e23.drinks = 30

s1e24 = Episode()
episodes.append(s1e24)
s1e24.name = "Owl's Well That Ends Well"
s1e24.season = 1
s1e24.number = 24
s1e24.feat = [ 0 ]
s1e24.tags = [ 0 ]
s1e24.desc = ""
s1e24.ldesc = ""
s1e24.writers = [ 2 ]
s1e24.date = t.date(2011, 4, 22)
s1e24.url = "http://www.youtube.com/watch?v=zUNwDsXRPhs&hd=1"
s1e24.drinks = 25

s1e25 = Episode()
episodes.append(s1e25)
s1e25.name = "Party of One"
s1e25.season = 1
s1e25.number = 25
s1e25.feat = [ 0 ]
s1e25.tags = [ 0 ]
s1e25.desc = ""
s1e25.ldesc = ""
s1e25.writers = [ 4 ]
s1e25.date = t.date(2011, 4, 29)
s1e25.url = "http://www.youtube.com/watch?v=iXeghEPY-_w&hd=1"
s1e25.drinks = 30

s1e26 = Episode()
episodes.append(s1e26)
s1e26.name = "Best Night Ever"
s1e26.season = 1
s1e26.number = 26
s1e26.feat = [ 0 ]
s1e26.tags = [ 0 ]
s1e26.desc = ""
s1e26.ldesc = ""
s1e26.writers = [ 1 ]
s1e26.date = t.date(2011, 5, 6)
s1e26.url = "http://www.youtube.com/watch?v=acbGTumnU7I&hd=1"
s1e26.drinks = 19

########## SEASON 2 #############

s2e1 = Episode()
episodes.append(s2e1)
s2e1.name = "The Return of Harmony, Part 1"
s2e1.season = 2
s2e1.number = 1
s2e1.feat = [ 0 ]
s2e1.tags = [ 0 ]
s2e1.desc = ""
s2e1.ldesc = ""
s2e1.writers = [ 6 ]
s2e1.date = t.date(2011, 9, 17)
s2e1.url = "http://www.youtube.com/watch?v=8SMO1hPSWyY&hd=1"
s2e1.drinks = 29

s2e2 = Episode()
episodes.append(s2e2)
s2e2.name = "The Return of Harmony, Part 2"
s2e2.season = 2
s2e2.number = 2
s2e2.part = 2
s2e2.feat = [ 0 ]
s2e2.tags = [ 0 ]
s2e2.desc = ""
s2e2.ldesc = ""
s2e2.writers = [ 6 ]
s2e2.date = t.date(2011, 9, 24)
s2e2.url = "http://www.youtube.com/watch?v=7Fgjyz_E4_E&hd=1"
s2e2.drinks = 25

s2e3 = Episode()
episodes.append(s2e3)
s2e3.name = "Lesson Zero"
s2e3.season = 2
s2e3.number = 3
s2e3.feat = [ 0 ]
s2e3.tags = [ 0 ]
s2e3.desc = ""
s2e3.ldesc = ""
s2e3.writers = [ 4 ]
s2e3.date = t.date(2011, 10, 15)
s2e3.url = "http://www.youtube.com/watch?v=NY_oj_LjSo8&hd=1"
s2e3.drinks = 36

s2e4 = Episode()
episodes.append(s2e4)
s2e4.name = "Luna Eclipsed"
s2e4.season = 2
s2e4.number = 4
s2e4.feat = [ 0 ]
s2e4.tags = [ 0 ]
s2e4.desc = ""
s2e4.ldesc = ""
s2e4.writers = [ 6 ]
s2e4.date = t.date(2011, 10, 22)
s2e4.url = "http://www.youtube.com/watch?v=JFj4_600h8s"
s2e4.drinks = 33

s2e5 = Episode()
episodes.append(s2e5)
s2e5.name = "Sisterhooves Social"
s2e5.season = 2
s2e5.number = 5
s2e5.feat = [ 0 ]
s2e5.tags = [ 0 ]
s2e5.desc = ""
s2e5.ldesc = ""
s2e5.writers = [ 2 ]
s2e5.date = t.date(2011, 11, 5)
s2e5.url = "http://www.youtube.com/watch?v=jYjSgThLFx8&hd=1"
s2e5.drinks = 24

s2e6 = Episode()
episodes.append(s2e6)
s2e6.name = "The Cutie Pox"
s2e6.season = 2
s2e6.number = 6
s2e6.feat = [ 0 ]
s2e6.tags = [ 0 ]
s2e6.desc = ""
s2e6.ldesc = ""
s2e6.writers = [ 1 ]
s2e6.date = t.date(2011, 11, 12)
s2e6.url = "http://www.youtube.com/watch?v=gYYeJSv9JyQ&hd=1"
s2e6.drinks = 33

s2e7 = Episode()
episodes.append(s2e7)
s2e7.name = "May the Best Pet Win!"
s2e7.season = 2
s2e7.number = 7
s2e7.feat = [ 0 ]
s2e7.tags = [ 0 ]
s2e7.desc = ""
s2e7.ldesc = ""
s2e7.writers = [ 5 ]
s2e7.date = t.date(2011, 11, 19)
s2e7.url = "http://www.youtube.com/watch?v=Uk7NDBKuh3g&hd=1"
s2e7.drinks = 20

s2e8 = Episode()
episodes.append(s2e8)
s2e8.name = "The Mysterious Mare do Well"
s2e8.season = 2
s2e8.number = 8
s2e8.feat = [ 0 ]
s2e8.tags = [ 0 ]
s2e8.desc = ""
s2e8.ldesc = ""
s2e8.writers = [ 8 ]
s2e8.date = t.date(2011, 11, 26)
s2e8.url = "http://www.youtube.com/watch?v=_FjWpfmr0k8&hd=1"
s2e8.drinks = 23

s2e9 = Episode()
episodes.append(s2e9)
s2e9.name = "Sweet and Elite"
s2e9.season = 2
s2e9.number = 9
s2e9.feat = [ 0 ]
s2e9.tags = [ 0 ]
s2e9.desc = ""
s2e9.ldesc = ""
s2e9.writers = [ 4 ]
s2e9.date = t.date(2011, 12, 3)
s2e9.url = "http://www.youtube.com/watch?v=8TYaCjeYhdU&hd=1"
s2e9.drinks = 24

s2e10 = Episode()
episodes.append(s2e10)
s2e10.name = "Secret of My Excess"
s2e10.season = 2
s2e10.number = 10
s2e10.feat = [ 0 ]
s2e10.tags = [ 0 ]
s2e10.desc = ""
s2e10.ldesc = ""
s2e10.writers = [ 6 ]
s2e10.date = t.date(2011, 12, 10)
s2e10.url = "http://www.youtube.com/watch?v=0FhKPVhq8BA&hd=1"
s2e10.drinks = 30

s2e11 = Episode()
episodes.append(s2e11)
s2e11.name = "Hearth's Warming Eve"
s2e11.season = 2
s2e11.number = 11 
s2e11.feat = [ 0 ]
s2e11.tags = [ 0 ]
s2e11.desc = ""
s2e11.ldesc = ""
s2e11.writers = [ 8 ]
s2e11.date = t.date(2011, 12, 17)
s2e11.url = "http://www.youtube.com/watch?v=vTlyKWht2Aw&hd=1"
s2e11.drinks = 25

s2e12 = Episode()
episodes.append(s2e12)
s2e12.name = "Family Appreciation Day"
s2e12.season = 2
s2e12.number = 12
s2e12.feat = [ 0 ]
s2e12.tags = [ 0 ]
s2e12.desc = ""
s2e12.ldesc = ""
s2e12.writers = [ 2 ]
s2e12.date = t.date(2012, 1, 7)
s2e12.url = "http://www.youtube.com/watch?v=xBrDR_i5cQQ&hd=1"
s2e12.drinks = 20

s2e13 = Episode()
episodes.append(s2e13)
s2e13.name = "Baby Cakes"
s2e13.season = 2
s2e13.number = 13
s2e13.feat = [ 0 ]
s2e13.tags = [ 0 ]
s2e13.desc = ""
s2e13.ldesc = ""
s2e13.writers = [ 5 ]
s2e13.date = t.date(2012, 1, 14)
s2e13.url = "http://www.youtube.com/watch?v=pOQXE5-vUHo&hd=1"
s2e13.drinks = 25

s2e14 = Episode()
episodes.append(s2e14)
s2e14.name = "The Last Roundup"
s2e14.season = 2
s2e14.number = 14
s2e14.feat = [ 0 ]
s2e14.tags = [ 0 ]
s2e14.desc = ""
s2e14.ldesc = ""
s2e14.writers = [ 1 ]
s2e14.date = t.date(2012, 1, 21)
s2e14.url = "http://www.youtube.com/watch?v=iAByxdOe8Dk&hd=1"
s2e14.drinks = 16

s2e15 = Episode()
episodes.append(s2e15)
s2e15.name = "The Super Speedy Cider Squeezy 6000"
s2e15.season = 2
s2e15.number = 15
s2e15.feat = [ 0 ]
s2e15.tags = [ 0 ]
s2e15.desc = ""
s2e15.ldesc = ""
s2e15.writers = [ 6 ]
s2e15.date = t.date(2012, 1, 28)
s2e15.url = "http://www.youtube.com/watch?v=XoGOIXdeCg4&hd=1"
s2e15.drinks = 39

s2e16 = Episode()
episodes.append(s2e16)
s2e16.name = "Read It and Weep"
s2e16.season = 2
s2e16.number = 16
s2e16.feat = [ 0 ]
s2e16.tags = [ 0 ]
s2e16.desc = ""
s2e16.ldesc = ""
s2e16.writers = [ 2 ]
s2e16.date = t.date(2012, 2, 4)
s2e16.url = "http://www.youtube.com/watch?v=GeQ1lkMQErk&hd=1"
s2e16.drinks = 25

s2e17 = Episode()
episodes.append(s2e17)
s2e17.name = "Hearts and Hooves Day"
s2e17.season = 2
s2e17.number = 17
s2e17.feat = [ 0 ]
s2e17.tags = [ 0 ]
s2e17.desc = ""
s2e17.ldesc = ""
s2e17.writers = [ 4 ]
s2e17.date = t.date(2012, 2, 11)
s2e17.url = "http://www.youtube.com/watch?v=_NOd5jEsQ2c&hd=1"
s2e17.drinks = 33

s2e18 = Episode()
episodes.append(s2e18)
s2e18.name = "A Friend in Deed"
s2e18.season = 2
s2e18.number = 18
s2e18.feat = [ 0 ]
s2e18.tags = [ 0 ]
s2e18.desc = ""
s2e18.ldesc = ""
s2e18.writers = [ 1 ]
s2e18.date = t.date(2012, 2, 18)
s2e18.url = "http://www.youtube.com/watch?v=dyjSCcVv0uk&hd=1"
s2e18.drinks = 29

s2e19 = Episode()
episodes.append(s2e19)
s2e19.name = "Putting Your Hoof Down"
s2e19.season = 2
s2e19.number = 19
s2e19.feat = [ 0 ]
s2e19.tags = [ 0 ]
s2e19.desc = ""
s2e19.ldesc = ""
s2e19.writers = [ 5, 8 ]
s2e19.date = t.date(2012, 3, 3)
s2e19.url = "http://www.youtube.com/watch?v=FkVL3r7nqUY&hd=1"
s2e19.drinks = 27

s2e20 = Episode()
episodes.append(s2e20)
s2e20.name = "It's About Time"
s2e20.season = 2
s2e20.number = 20
s2e20.feat = [ 0 ]
s2e20.tags = [ 0 ]
s2e20.desc = ""
s2e20.ldesc = ""
s2e20.writers = [ 6 ]
s2e20.date = t.date(2012, 3, 10)
s2e20.url = "http://www.youtube.com/watch?v=1lnplqeh_vc&hd=1"
s2e20.drinks = 20

s2e21 = Episode()
episodes.append(s2e21)
s2e21.name = "Dragon Quest"
s2e21.season = 2
s2e21.number = 21
s2e21.feat = [ 0 ]
s2e21.tags = [ 0 ]
s2e21.desc = ""
s2e21.ldesc = ""
s2e21.writers = [ 8 ]
s2e21.date = t.date(2012, 3, 17)
s2e21.url = "http://www.youtube.com/watch?v=_nPKi9V9dLw&hd=1"
s2e21.drinks = 20

s2e22 = Episode()
episodes.append(s2e22)
s2e22.name = "Hurricane Fluttershy"
s2e22.season = 2
s2e22.number = 22
s2e22.feat = [ 0 ]
s2e22.tags = [ 0 ]
s2e22.desc = ""
s2e22.ldesc = ""
s2e22.writers = [ 2 ]
s2e22.date = t.date(2012, 3, 24)
s2e22.url = "http://www.youtube.com/watch?v=GUh2_jg3YL0&hd=1"
s2e22.drinks = 28

s2e23 = Episode()
episodes.append(s2e23)
s2e23.name = "Ponyville Confidential"
s2e23.season = 2
s2e23.number = 23
s2e23.feat = [ 0 ]
s2e23.tags = [ 0 ]
s2e23.desc = ""
s2e23.ldesc = ""
s2e23.writers = [ 6 ]
s2e23.date = t.date(2012, 3, 31)
s2e23.url = "https://www.youtube.com/watch?&v=_nAEz7CxLFI&hd=1"
s2e23.drinks = 29

s2e24 = Episode()
episodes.append(s2e24)
s2e24.name = "MMMystery on the Friendship Express"
s2e24.season = 2
s2e24.number = 24
s2e24.feat = [ 0 ]
s2e24.tags = [ 0 ]
s2e24.desc = ""
s2e24.ldesc = ""
s2e24.writers = [ 1 ]
s2e24.date = t.date(2012, 4, 7)
s2e24.url = "http://www.youtube.com/watch?&v=N1iNckux6vA&hd=1"
s2e24.drinks = 30

s2e25 = Episode()
episodes.append(s2e25)
s2e25.name = "A Canterlot Wedding, Part 1"
s2e25.season = 2
s2e25.number = 25
s2e25.feat = [ 0 ]
s2e25.tags = [ 0 ]
s2e25.desc = ""
s2e25.ldesc = ""
s2e25.writers = [ 4 ]
s2e25.date = t.date(2012, 4, 21)
s2e25.url = "http://www.youtube.com/watch?v=Fhz8X62FDns&hd=1"
s2e25.drinks = 25

s2e26 = Episode()
episodes.append(s2e26)
s2e26.name = "A Canterlot Wedding, Part 2"
s2e26.season = 2
s2e26.number = 26
s2e26.part = 2
s2e26.feat = [ 0 ]
s2e26.tags = [ 0 ]
s2e26.desc = ""
s2e26.ldesc = ""
s2e26.writers = [ 4 ]
s2e26.date = t.date(2012, 4, 21)
s2e26.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s2e26.drinks = 30

########## SEASON 3 #############

s3e1 = Episode()
episodes.append(s3e1)
s3e1.name = "The Crystal Empire, Part 1"
s3e1.season = 3
s3e1.number = 1
s3e1.feat = [ 0 ]
s3e1.tags = [ 0 ]
s3e1.desc = ""
s3e1.ldesc = ""
s3e1.writers = [ 4 ]
s3e1.date = t.date(2012, 11, 10)
s3e1.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e1.drinks = 25

s3e2 = Episode()
episodes.append(s3e2)
s3e2.name = "The Crystal Empire, Part 2"
s3e2.season = 3
s3e2.number = 2
s3e2.part = 2
s3e2.feat = [ 0 ]
s3e2.tags = [ 0 ]
s3e2.desc = ""
s3e2.ldesc = ""
s3e2.writers = [  ]
s3e2.date = t.date(2012, 11, 10)
s3e2.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e2.drinks = 30

s3e3 = Episode()
episodes.append(s3e3)
s3e3.name = "Too Many Pinkie Pies"
s3e3.season = 3
s3e3.number = 3
s3e3.feat = [ 0 ]
s3e3.tags = [ 0 ]
s3e3.desc = ""
s3e3.ldesc = ""
s3e3.writers = [ 4 ]
s3e3.date = t.date(2012, 11, 17)
s3e3.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e3.drinks = 30

s3e4 = Episode()
episodes.append(s3e4)
s3e4.name = "One Bad Apple"
s3e4.season = 3
s3e4.number = 4
s3e4.feat = [ 0 ]
s3e4.tags = [ 0 ]
s3e4.desc = ""
s3e4.ldesc = ""
s3e4.writers = [ 4 ]
s3e4.date = t.date(2012, 11, 10)
s3e4.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e4.drinks = 28 

s3e5 = Episode()
episodes.append(s3e5)
s3e5.name = "Magic Duel"
s3e5.season = 3
s3e5.number = 5
s3e5.feat = [ 0 ]
s3e5.tags = [ 0 ]
s3e5.desc = ""
s3e5.ldesc = ""
s3e5.writers = [ 4 ]
s3e5.date = t.date(2012, 11, 10)
s3e5.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e5.drinks = 50

s3e6 = Episode()
episodes.append(s3e6)
s3e6.name = "Sleepless in Ponyville"
s3e6.season = 3
s3e6.number = 6
s3e6.feat = [ 0 ]
s3e6.tags = [ 0 ]
s3e6.desc = ""
s3e6.ldesc = ""
s3e6.writers = [ 4 ]
s3e6.date = t.date(2012, 11, 10)
s3e6.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e6.drinks = 25

s3e7 = Episode()
episodes.append(s3e7)
s3e7.name = "Wonderbolt Academy"
s3e7.season = 3
s3e7.number = 7
s3e7.feat = [ 0 ]
s3e7.tags = [ 0 ]
s3e7.desc = ""
s3e7.ldesc = ""
s3e7.writers = [ 4 ]
s3e7.date = t.date(2012, 11, 10)
s3e7.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e7.drinks = 20

s3e8 = Episode()
episodes.append(s3e8)
s3e8.name = "Apple Family Reunion"
s3e8.season = 3
s3e8.number = 8
s3e8.feat = [ 0 ]
s3e8.tags = [ 0 ]
s3e8.desc = ""
s3e8.ldesc = ""
s3e8.writers = [ 4 ]
s3e8.date = t.date(2012, 11, 10)
s3e8.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e8.drinks = 25 

s3e9 = Episode()
episodes.append(s3e9)
s3e9.name = "Spike at Your Service"
s3e9.season = 3
s3e9.number = 9
s3e9.feat = [ 0 ]
s3e9.tags = [ 0 ]
s3e9.desc = ""
s3e9.ldesc = ""
s3e9.writers = [ 4 ]
s3e9.date = t.date(2012, 11, 10)
s3e9.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e9.drinks = 25

s3e10 = Episode()
episodes.append(s3e10)
s3e10.name = "Keep Calm and Flutter On"
s3e10.season = 3
s3e10.number = 10
s3e10.feat = [ 0 ]
s3e10.tags = [ 0 ]
s3e10.desc = ""
s3e10.ldesc = ""
s3e10.writers = [ 4 ]
s3e10.date = t.date(2012, 11, 10)
s3e10.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e10.drinks = 29

s3e11 = Episode()
episodes.append(s3e11)
s3e11.name = "Just For Sidekicks"
s3e11.season = 3
s3e11.number = 11
s3e11.feat = [ 0 ]
s3e11.tags = [ 0 ]
s3e11.desc = ""
s3e11.ldesc = ""
s3e11.writers = [ 4 ]
s3e11.date = t.date(2012, 11, 10)
s3e11.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e11.drinks = 26

s3e12 = Episode()
episodes.append(s3e12)
s3e12.name = "Games Ponies Play"
s3e12.season = 3
s3e12.number = 12
s3e12.feat = [ 0 ]
s3e12.tags = [ 0 ]
s3e12.desc = ""
s3e12.ldesc = ""
s3e12.writers = [ 4 ]
s3e12.date = t.date(2012, 11, 10)
s3e12.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e12.drinks = 20

s3e13 = Episode()
episodes.append(s3e13)
s3e13.name = "Magical Mystery Cure"
s3e13.season = 3
s3e13.number = 13
s3e13.feat = [ 0 ]
s3e13.tags = [ 0 ]
s3e13.desc = ""
s3e13.ldesc = ""
s3e13.writers = [ 4 ]
s3e13.date = t.date(2012, 11, 10)
s3e13.url = "http://www.youtube.com/watch?v=xRWb_lzrp5c&hd=1"
s3e13.drinks = 28

