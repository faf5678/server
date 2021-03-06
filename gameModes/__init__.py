#-------------------------------------------------------------------------------
# Copyright (c) 2014 Gael Honorez.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#-------------------------------------------------------------------------------

import logging
logger= logging.getLogger(__name__)


#hyper container
from hyperGamesContainer import hyperGamesContainerClass

# Game container
from gamesContainer import gamesContainerClass
# derived
from customGamesContainer import customGamesContainerClass # custom games
from ladderGamesContainer import ladder1v1GamesContainerClass # ladder games
from customNomadsGamesContainer import customNomadsGamesContainerClass # custom nomads games
from customLabwarsGamesContainer import customLabwarsGamesContainerClass # custom labwars games

from customMurderPartyGamesContainer import customMurderPartyGamesContainerClass # custom murder party games
from customKothGamesContainer import customKothGamesContainerClass # custom king of the hill games
from customPhantomXGamesContainer import customPhantomXGamesContainerClass # custom phantomX games
#from customPhantomNGamesContainer import customPhantomNGamesContainerClass # custom phantomN games
from customEWGamesContainer import customEWGamesContainerClass # custom Exp Wars games
#from customNFTWGamesContainer import customNFTWGamesContainerClass # custom NFTW games
#from customWyvernGamesContainer import customWyvernGamesContainerClass # custom Wyvern games
from customBlackopsGamesContainer import customBlackopsGamesContainerClass # custom Blackops games

from customXtremewarsGamesContainer import customXtremewarsGamesContainerClass # custom Blackops games

# game entity
from game import gameClass
#derived
from ladderGame import ladder1v1GameClass #ladder 1v1
from customGame import customGameClass #custom
from nomadsGame import nomadsGameClass #nomads
from labwarsGame import labwarsGameClass #labwars

from murderPartyGame import murderPartyGameClass # murder party
#from phantomNGame import phantomNGameClass #phantom N
from phantomXGame import phantomXGameClass # phantom X
from kothGame import kothGameClass # king of the hill
#from EWGame import EWGameClass # exp war

#from NFTWGame import NFTWClass # exp war
#from wyvernGame import wyvernClass # exp war
from blackopsGame import blackopsGameClass # exp war
from xtremewarsGame import xtremewarsGameClass # exp war
                           

def reloadModules():
    '''reloading gameModes modules'''
    #print "reloading gameModes modules"

    logger.debug("reloading gameModes modules")
    
    #reload(ladderGame)
#    reload(customGame)
#    reload(nomadsGame)
#    reload(labwarsGame)
#    reload(murderPartyGame)
#    reload(phantomNGame)
#    reload(phantomXGame)
#    reload(kothGame)
#    reload(EWGame)
#    reload(NFTWGame)
#    reload(wyvernGame)
#    reload(blackopsGame)
#    reload(xtremewarsGame)
#
    #reload(game)
#    
#    reload(customGamesContainer)
    #reload(ladderGamesContainer)
#    reload(customNomadsGamesContainer)
#    reload(customLabwarsGamesContainer)
#    reload(customMurderPartyGamesContainer)
#    reload(customEWGamesContainer)
#    reload(customPhantomXGamesContainer)
#    reload(customPhantomNGamesContainer)
#    reload(customKothGamesContainer)
#    
#    reload(customWyvernGamesContainer)
#    reload(customNFTWGamesContainer)
#    reload(customBlackopsGamesContainer)
#    reload(customXtremewarsGamesContainer)
##    
#    reload(gamesContainer)
##    
#    reload(hyperGamesContainer)
    
    
    
    
