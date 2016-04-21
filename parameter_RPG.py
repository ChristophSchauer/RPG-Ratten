# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version :           1.0

Programmed with:    WinPython 3.4.4.1
Changed to:         WinPython 2.7.10.3

History:
[2016.03.25, CS]:   start with an enemy array; 
                    start with packs, talents, tricks;
[2016.03.29, CS]:   insert a list with the possible directions;
[2016.03.30, CS]:   changed the name to parameter_RPG.py;
                    changed the directions-list: now it can be used as ring to
                    find the direction of the last room;
[2016.04.11, CS]:   ISSUE#16: changed all the naming of the interaction in
                    english;
[2016.04.13, CS]:   ISSUE#17: start with the dictionary for 'generate_char', 'showStatus',
                    fct_rooms, fct_move, fct_get, fct_drop, fct_fight;
[2016.04.19, CS]:   change to version 1.0;  
"""
# sorted to be used for the ring
directions = ['north','east','up','south','west','down']

enemystatus = {
    'cat':{
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
        
    'dog':{
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
        
    'crow':{
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
        
    'cockroach':{
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
        
    'fox':{
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
        
    'marten':{
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
        
    'toad':{
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
        
    'snake':{
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
        
    'bat':{
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
packs_eng = ['brand rats','garbage eater','collectors','red eyes','sharp teeth','lab rats','diver']
# nur eine Stufe
tricks = ['Außergewöhnlicher Verbündeter', 'Eisenkiefer', 'Eisenmagen', 'Dickes Fell', 'Fiese Ratte', 'Flinke Ratte', 'Geruchlos', 'Gespür für Artefakte', 'Guter Beobachter', 'Kampfratte', 'Loses Maulwerk', 'Pakt mit dem Rattentod', 'Rattensinn', 'Rattig', 'Schlangenratte', 'Tote Ratte', 'Treuer Diener der Erbauer', 'Untrüglicher Instinkt', 'Vererbte Resistenz', 'Wir sind doch Kollegen']
# Stufe 1 oder 2 (Bonus +1/+2)
talents = ['Aus dem Weg gehen', 'Fallenkunde', 'Gänge und Abteilungen', 'hear,see,sniff', 'scratch,bite', 'climb,spring', 'legends,rumors', 'Quasseln und beeindrucken', 'swim,dive', 'vanish,hide', 'Von den Erbauern', 'Von der Natur', 'Wunden lecken']

talents_eng = ['Aus dem Weg gehen', 'Fallenkunde', 'Gänge und Abteilungen', 'hear,see,sniff', 'scratch,bite', 'climb,spring', 'legends,rumors', 'Quasseln und beeindrucken', 'swim,dive', 'vanish,hide', 'Von den Erbauern', 'Von der Natur', 'Wunden lecken']

# german / english dictionary
language = {"selection"                         : "Auswahl",
            # generate_char
            "name your hero please:"            : "Bitte benenne deinen Helden:",
            "you distributed the values false"  : "du hast die Werte falsch verteilt",
            "your char was created, now the game can begin" : "Character erstellt, beginne das Abenteuer",
            # showStatus
            "you are in the "                   : "du bist in der/dem ",
            "inventory: "                       : "Inventar: ",
            "you see: "                         : "du siehst: ",
            "you won the game!"                 : "du hast das Spiel gewonnen!",
            "you played "                       : "Spielzeit ",
            " turn(s)"                          : " Zug/Züge",
            "There's a door leading: "          : "Eine Tür führt nach: ",
            "There are no doors you can see!"   : "Du siehst keine Türen!",
            "There are doors leading: "         : "Es führen Türen nach: ",
            # fct_rooms
            "using default":"",
            # fct_move
            "door locked":"",
            "want to use the key? [Y/N]":"",
            "opens the door with the key":"",
            "you can't go that way!":"",
            # fct_get
            " got!":"",
            "can't get ":"",
            # fct_fight
            "enemy died":"",
            "you died":"",
            "the game closes in 10 seconds":"",
            "this person can't be attacked":"",
            "you are fighting against your own shadow":"",
            #ftc_drop
            "you can't drop anything":"",
            "you dropped ":""
            # fct_exit
            
            }