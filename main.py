# ESW Egarden - An Effort for Hydroponics to be Automated with a Raspberry-Pi

import ConfigParser
import threading
from slack import slack
from systemTypes import nft
from systemTypes import ebbnflow

Config = ConfigParser.ConfigParser()
Config.read('config.ini')
systems = []

# slackIntegration = slack()

numSystems = len(Config.sections())
systemThreads = []

# Reading through the different systems that are in the Config.ini file
for i in range(numSystems):
    print "Looking at System %d" % (i + 1)
    sectionString = 'System' + str(i + 1)
    try:
        type = Config.get(sectionString,'Type')
        print "System Type is: %s" % (type)  # TO Fix
        status = Config.get(sectionString,'Status')
        print "System Status is: %r" % (status) #TO Fix
        pumpPin = int(Config.get(sectionString, 'PumpPin'))
        print "System Pump Pin is: %d" % (pumpPin)  # TO Fix
        waterLevelPin = int(Config.get(sectionString, 'WaterLevelPin'))
        print "System Water Level Detection Pin is: %d" % (waterLevelPin)  # TO Fix
    except:
        print 'Bad Naming of Sections in Config File, Continuing Haphazardly'

    # Starting the systems based of System Type
    if (type == 'NFT'):
        print 'Creating NFT System'
        x = nft.NFT(pumpPin,waterLevelPin)
        systemThreads.append(x)
    elif (type == 'Drip'):
        # Drip System has unique parameters for it, so parsing for the more information
        print 'Creating Drip System'
        try:
            onTime = Config.get(sectionString, 'onTime')
            print "System will be On This Much Time per Hour (minutes): %d" % (int(onTime))  # TO Fix
        except:
            print 'Bad Naming of Drip System Timer in Config File, Continuing Haphazardly'
        # x = Drip(pumpPin, waterLevelPin, onTime)
        # systemThreads.append(x)
    elif type == 'EbbNFlow':
        # EbbNFlow System has unique parameters for it, so parsing for the more information
        print 'Creating EbbNFlow System'
        try:
            onTime = Config.get(sectionString, 'onTime')
            print "System will be Off This Much Time per Hour (minutes): %d" % (int(onTime))  # TO Fix
            offTime = Config.get(sectionString, 'offTime')
            print "System will be Off This Much Time per Hour (minutes): %d" % (int(offTime))  # TO Fix
        except:
            print 'Bad Naming of Drip System Timer in Config File, Continuing Haphazardly'
        x = ebbnflow(pumpPin, waterLevelPin, onTime, offTime)
        systemThreads.append(x)
    else:
        print 'System type did not Match known types. Check Spelling of System Type'
        
if len(systemThreads) > 0:
    for t in systemThreads:
        t.systemRun()



