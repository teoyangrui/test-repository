# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:25:57 2020

@author: User
"""

#import sqlite3
from db import db
#internal representation of what an item does and look like
class StoreModel(db.Model):#telling them item model is map to the database
    
    __tablename__="stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    #we can also do a back reference to see if stored_id=its own id
    items = db.relationship('ItemModel' , lazy='dynamic')
    #self.item no longers give a listt of item, now it is a query builder that has the ability to look into the item table
    #then we use .all to look into the items table. So until we call json item, we are not looking at the table.
    #If not it will create an item object for each item, which is an expensive operation
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
     
    def json(self):
        return{'name': self.name,'items':[item.json() for item in self.items.all()]}
        #for this, we have to go into the table everytime we call json, we can prevent that by removing lazy=dynamic
        #so that all the items are created once and for all, which means slower stall creation rate
        #so call item.json() for item in self.items
        #but when doing this, every time we call json, it will have to look up the table, which means slower
        #returning of the json
         
    @classmethod    
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #query is smething that comes from sqlalchmcemy
         #can filter by multiple vairable names
         #first returns the first row only, the first match of the name.
     
    def save_to_db(self): #update or insert does both! 
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
            
        db.session.commit()          