# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.25, CS]:   start with an enemy array; 
                    start with packs, talents, tricks;
[2016.03.29, CS]:   insert a list with the possible directions;
[2016.03.30, CS]:   changed the name to parameter_RPG.py;
                    changed the directions-list: now it can be used as ring to
                    find the direction of the last room;

"""
# sorted to be used for the ring
directions = ['north','east','up','south','west','down']

enemystatus = {
    'katze':{
        "name"      : 'Schleicher',
        "clever"    : 3,
        "social"    : 3,
        "strong"    : 3,
        "fast"      : 5,
        "life"      : 9,
        "tricks"    : [],
        "talents"   : ['climb,spring',1,'vanish,hide',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'hund':{
        "name"      : 'Stinker',
        "clever"    : 2,
        "social"    : 2,
        "strong"    : 5,
        "fast"      : 4,
        "life"      : 15,
        "tricks"    : [],
        "talents"   : ['hear,see,sniff',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'krähe':{
        "name"      : 'Schwarzflügel',
        "clever"    : 3,
        "social"    : 2,
        "strong"    : 2,
        "fast"      : [1,3],
        "life"      : 6,
        "tricks"    : ['fly'],
        "talents"   : ['vanish,hide',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'kakerlake':{
        "name"      : 'Krabbler',
        "clever"    : 4,
        "social"    : 3,
        "strong"    : 4,
        "fast"      : 4,
        "life"      : 12,
        "tricks"    : ['Dickes Fell'],
        "talents"   : [],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'fuchs':{
        "name"      : 'Rotschweif',
        "clever"    : 4,
        "social"    : 3,
        "strong"    : 4,
        "fast"      : 4,
        "life"      : 12,
        "tricks"    : [],
        "talents"   : ['hear,see,sniff',1,'vanish,hide',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'marder':{
        "name"      : 'Flinkfuß',
        "clever"    : 2,
        "social"    : 2,
        "strong"    : 2,
        "fast"      : 4,
        "life"      : 6,
        "tricks"    : [],
        "talents"   : ['scratch,bite',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'kröte':{
        "name"      : 'Glotzer',
        "clever"    : 1,
        "social"    : 1,
        "strong"    : 2,
        "fast"      : [1,3],
        "life"      : 6,
        "tricks"    : ['clench'],
        "talents"   : ['swim,dive',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'schlange':{
        "name"      : 'Zischer',
        "clever"    : 1,
        "social"    : 1,
        "strong"    : 2,
        "fast"      : 4,
        "life"      : 6,
        "tricks"    : ['poison'],
        "talents"   : ['vanish,hide',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        },
        
    'fledermaus':{
        "name"      : 'Schwingenschreck',
        "clever"    : 1,
        "social"    : 1,
        "strong"    : 1,
        "fast"      : 4,
        "life"      : 3,
        "tricks"    : ['fly'],
        "talents"   : ['vanish,hide',1],
        "pack"      : [],
        "pros"      : [],
        "cons"      : []
        }
    }
    
packs = ['Brandratten','Müllschlinger','Sammler','Rotaugen','Scharfzähne','Laborratten','Taucher']
# nur eine Stufe
tricks = ['Außergewöhnlicher Verbündeter', 'Eisenkiefer', 'Eisenmagen', 'Dickes Fell', 'Fiese Ratte', 'Flinke Ratte', 'Geruchlos', 'Gespür für Artefakte', 'Guter Beobachter', 'Kampfratte', 'Loses Maulwerk', 'Pakt mit dem Rattentod', 'Rattensinn', 'Rattig', 'Schlangenratte', 'Tote Ratte', 'Treuer Diener der Erbauer', 'Untrüglicher Instinkt', 'Vererbte Resistenz', 'Wir sind doch Kollegen']
# Stufe 1 oder 2 (Bonus +1/+2)
talents = ['Aus dem Weg gehen', 'Fallenkunde', 'Gänge und Abteilungen', 'hear,see,sniff', 'scratch,bite', 'climb,spring', 'legends,rumors', 'Quasseln und beeindrucken', 'swim,dive', 'vanish,hide', 'Von den Erbauern', 'Von der Natur', 'Wunden lecken']