# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:19:17 2021

@author: danny
"""

import pygal.maps.world
northamerica={'am':282162848,'ca':30770661,'mx':99959895}
europe={'fr':60762406,'se':1011781,'ch':71847981}
africa={'eg':67649043,'cg':49626496,'za':44000833}
worldmap=pygal.maps.world.World()
worldmap.title='Europe、Africa、North America人口'
worldmap.add('Europe',europe)
worldmap.add('africa',africa)
worldmap.add('north_america',northamerica)
worldmap.render_to_file('2.svg')