# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
    def insert(atMe, newFrob):
        """
        atMe: a Frob that is part of a doubly linked list
        newFrob:  a Frob with no links 
        This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
        """

        if newFrob.myName() < atMe.myName():
            after = atMe
            #while loop that continues as long as newFrob is lexicographically before atMe
            while after.getBefore() != None and newFrob.myName() < after.getBefore().myName():
                after = after.getBefore()
            #for the element after - sets it after newFrob
            newFrob.setAfter(after)
            #for the element before after - sets it before newFrob
            newFrob.setBefore(after.getBefore())
            if after.getBefore() != None:
                #for the element before after - sets newFrob after that element
                after.getBefore().setAfter(newFrob)
            after.setBefore(newFrob)
        else:
            before = atMe
            #while loop that goes thru linked list as long as atMe is lexicographically before newFrob
            while before.getAfter() != None and newFrob.myName() > before.getAfter().myName():
                before = before.getAfter()
            #for element after before - set it after newFrob
            newFrob.setAfter(before.getAfter())
            #for element before - set it before newFrob
            newFrob.setBefore(before)
            if before.getAfter() != None:
                #for the element after before - sets newFrob before it
                before.getAfter().setBefore(newFrob)
            #set newFrob after before
            before.setAfter(newFrob)
        
    def findFront(start):
        """
        start: a Frob that is part of a doubly linked list
        returns: the Frob at the beginning of the linked list 
        """
        before = start.getBefore()
        if before == None:
            return start
        else:
            return findFront(start.getBefore())
