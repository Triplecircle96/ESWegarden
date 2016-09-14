# ESW Egarden - An Effort for Hydroponics to be Automated with a Raspberry-Pi

import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

numSystems = len(Config.sections())

for i in range(numSystems):
	print "Looking at System %d" % (i + 1)
	sectionString = 'System' + str(i + 1);
	try:
		pinNumber = Config.get(sectionString,'PumpPin')
		print "Pin Number Assigned is: %d" % (int(pinNumber)) #TO Fix
	except:
		print 'Bad Naming of Sections in Config File, Continuing Haphazardly'


