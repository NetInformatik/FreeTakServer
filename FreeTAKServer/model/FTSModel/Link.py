from FreeTAKServer.model.FTSModel.fts_protocol_object import FTSProtocolObject
#######################################################
# 
# Link.py
# Python implementation of the Class Link
# Generated by Enterprise Architect
# Created on(FTSProtocolObject):      11-Feb-2020 11(FTSProtocolObject):08(FTSProtocolObject):08 AM
# Original author: Corvo
# 
#######################################################
import datetime as dt
from FreeTAKServer.model.FTSModelVariables.LinkVariables import LinkVariables as vars

class Link(FTSProtocolObject):
    def __init__(self):
        self.uid = None
        self.relation = None
        self.production_time = None
        self.type = None
        self.parent_callsign = None

    @staticmethod
    def drop_point(UID = vars.drop_point().UID, RELATION = vars.drop_point().RELATION,
                   PRODUCTIONTIME = vars.drop_point().PRODUCTIONTIME,
                   TYPE = vars.drop_point().TYPE, PARENTCALLSIGN = vars.drop_point().PARENTCALLSIGN):
        link = Link()
        link.setuid(UID)
        link.setrelation(RELATION)
        link.setproduction_time(PRODUCTIONTIME)
        link.settype(TYPE)
        link.setparent_callsign(PARENTCALLSIGN)
        return link

    @staticmethod
    def geochat(UID=vars.geochat().UID, RELATION=vars.geochat().RELATION,
                   PRODUCTIONTIME=vars.geochat().PRODUCTIONTIME, TYPE=vars.geochat().TYPE,
                   PARENTCALLSIGN=vars.geochat().PARENTCALLSIGN):
        link = Link()
        link.setuid(UID)
        link.setrelation(RELATION)
        link.settype(TYPE)
        link.setparent_callsign(PARENTCALLSIGN)
        return link

    @staticmethod
    def emergency_on(UID=vars.emergency_on().UID, RELATION=vars.emergency_on().RELATION,
                PRODUCTIONTIME=vars.emergency_on().PRODUCTIONTIME, TYPE=vars.emergency_on().TYPE,
                PARENTCALLSIGN=vars.emergency_on().PARENTCALLSIGN):
        link = Link()
        link.setuid(UID)
        link.setrelation(RELATION)
        link.setproduction_time(PRODUCTIONTIME)
        link.settype(TYPE)
        link.setparent_callsign(PARENTCALLSIGN)
        return link

    @staticmethod
    def disconnect(UID=vars.disconnect().uid, TYPE=vars.disconnect().type, RELATION=vars.disconnect().relation):
        link = Link()
        link.setuid(UID)
        link.settype(TYPE)
        link.setrelation(RELATION)
        return link

    # uid getter 
    def getuid(self): 
        return self.uid 

    # uid setter 
    def setuid(self, uid=0):  
        self.uid=uid 

    # production_time getter 
    def getproduction_time(self): 
        return self.production_time 

    # production_time setter 
    def setproduction_time(self, production_time=0):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ"
        if production_time == None:
            timer = dt.datetime
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            add = dt.timedelta(minutes=1)
            production_time_part = dt.datetime.strptime(zulu, DATETIME_FMT) + add
            self.production_time = production_time_part.strftime(DATETIME_FMT)
        else:
            self.production_time = production_time

    # relation getter 
    def getrelation(self): 
        return self.relation 

    # relation setter 
    def setrelation(self, relation=0):  
        self.relation=relation 

    # type getter 
    def gettype(self): 
        return self.type 

    # type setter 
    def settype(self, type=0):  
        self.type=type 

    # parent_callsign getter 
    def getparent_callsign(self): 
        return self.parent_callsign 

    # parent_callsign setter 
    def setparent_callsign(self, parent_callsign=0):  
        self.parent_callsign=parent_callsign 