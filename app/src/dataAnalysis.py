import json
import datetime
import operator
import re
import copy

class memberObj(object):
    pageUrl = ""
    name = ""
    facebookId = ""
    amount = 0
    isTeamCaptain = False
    supportor = {}

    def __init__(self, pageUrl, name, facebookId,amount, isTeamCaptain):
        self.pageUrl = pageUrl
        self.name = name
        self.facebookId = facebookId
        self.amount = amount
        self.isTeamCaptain = isTeamCaptain

#today = datetime.date.today()
today = datetime.date(2017,9,5)
completeData = {}

def importData(filePath):
    with open(filePath) as json_file:
        jsonData = json.load(json_file)
        
    for date in jsonData:
        dayData = []
        d = date.split(sep=',')
        d = [int(x) for x in d]
        datestamp = datetime.date(d[0],d[1],d[2])
        for member in jsonData[date]:
            amount = float(re.sub('[$]','',member["amount"]))
            tempVar = memberObj(member["pageUrl"], member["name"], member["facebookId"], amount, member["isTeamCaptain"])
            dayData.append(tempVar)
        completeData[datestamp] = dayData

importData("data.json")

def highestDonor(Dict):
    topDonor = Dict[0]
    for donor in Dict:
        if donor.amount > topDonor.amount:
            topDonor = donor
    return topDonor

highestDonorToDate = (highestDonor(completeData[today]))

def collectedToDate():
    return completeData[today]

collectedSoFar = (collectedToDate())

def donationsWithinWeek():
    
    deltaData = []
    lastWeek = (datetime.date.today() - datetime.timedelta(days = 7))
    for donor in completeData[today]:
        clone = copy.copy(donor)
        if lastWeek in completeData.keys():
            if donor in completeData[lastWeek].keys():
                clone.amount = completeData[today][donor].amount - completeData[lastWeek][donor].amount
                deltaData.append(clone)
            else:
                deltaData.append(clone)
        else:
            deltaData.append(clone)
    return deltaData

donorsWithinWeek = (donationsWithinWeek())

highestDonorInWeek = (highestDonor(donationsWithinWeek()))
