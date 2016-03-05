from collections import Counter as co
import re
import bs4
import chitchat as cc
import requests


def compare(prefix, channel, message):

    try:
        _, id1, id2, *_ = message.split(maxsplit=3)
        
    except ValueError:
        return cc.privmsg(target, 'Onii-chan you baka! Use it like this: ".compare <id 1> <id 2>"')
    
    id1, id2 = int(id1), int(id2)    
    return (cc.privmsg(channel, line) for line in statcomp(id1, id2))


def htmlget(ID):
    
    req = requests.get('http://puzzledragonx.com/en/monster.asp?n='+str(ID))
    req.encoding = 'utf-8'
    req.raise_for_status()

    return bs4.BeautifulSoup(req.text, "html.parser")



def info(ID):

    awaken = found = list()
    mon = htmlget(ID)
    name = mon.find('h1').string
    hp = mon.find('td', class_='stathp').next.next.next.next.string
    atk = mon.find('td', class_='statatk').next.next.next.next.string
    rcv = mon.find('td', class_='statrcv').next.next.next.next.string

    try:
        provisory = str(mon.find('td', class_='awoken1').find_all('a'))
        for m in re.finditer('awoken/(.+?).png', provisory):
            awaken.append(str(m))
        for i in range(len(awaken)):
            awaken[i]=re.search('awoken/(.+?).png', awaken[i])
            if awaken[i]:
                found[i]=(awaken[i].group(1))

    except AttributeError:
        awaken='none'

    return [name,hp,atk,rcv,found] 



def statcomp(ID1, ID2):

    info1 = info(ID1)
    info2 = info(ID2)
    diff_hp = int(info1[1])-int(info2[1])
    diff_atk = int(info1[2])-int(info2[2])
    diff_rcv = int(info1[3])-int(info2[3])

    yield str(info1[0])+': '+str(info1[1])+'/'+str(info1[2])+'/'+str(info1[3])
    yield str(info2[0])+': '+str(info2[1])+'/'+str(info2[2])+'/'+str(info2[3])
    yield 'Difference: '+str(diff_hp)+'/'+str(diff_atk)+'/'+str(diff_rcv)


    
def awakencomp(ID1, ID2):

    info1 = info(ID1)
    info2 = info(ID2)
    m1_awks=info(ID1)[4]
    m2_awks=info(ID2)[4]
    common_awks = awaken_translator(list((co(m1_awks) & co(m2_awks)).elements()))
    m1_unique_awks = list((co(awaken_translator(m1_awks)) - co(common_awks)).elements())
    m2_unique_awks = list((co(awaken_translator(m2_awks)) - co(common_awks)).elements())

    yield 'Common awakens: '+str(common_awks)
    yield str(info(ID1)[0])+' unique awakens: '+str(m1_unique_awks)
    yield str(info(ID2)[0])+' unique awakens: '+str(m2_unique_awks)



def awaken_dict(awk_n):

    awk_list=['none', 'Enhanced HP', 'Enhanced HP', 'Enhanced HP', 'Enhanced Atk', 'Enhanced RCV', 'Reduce Red DMG', 'Reduce Blue DMG', 'Reduce Green DMG', 'Reduce Light DMG', 'Reduce Dark DMG', 'AutoRCV', 'Bind Resist', 'Blind Resist', 'Jammer Resist', 'Poison Resist', 'Enhanced Red', 'Enhanced Blue', 'Enhanced Green', 'Enhanced Light', 'Enhanced Dark', 'Time Extend', 'Bind Clear', 'Skill Boost', 'Red Row', 'Blue Row', 'Green Row', 'Light Row', 'Dark Row', 'TPA', 'Skill Bind Resist', 'Enhanced Hearts', 'Coop Boost', 'Dragon Killer', 'God Killer', 'Devil Killer', 'Machine Killer']

    return(awk_list[awk_n])



def awaken_translator(awk_list):
    result=list()

    for i in range(len(awk_list)):
        result.append(awaken_dict(int(awk_list[i])))

    return result
