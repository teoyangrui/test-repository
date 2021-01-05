# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:15:21 2020

@author: User
"""
#import sqlite3
from db import db
#internal representation of what an item does and look like
class ItemModel(db.Model):#telling them item model is map to the database
    
    __tablename__="items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))#foreign key because it has id value idential
    #to another table. stores.id tell us from the table name stores we get the id! so sql alchemy can communicate
    store = db.relationship('StoreModel') #don't have to do a join of stores id!
    #what this does, is that it sees we have a store id, terefore we can find a store in the database that matches
    #this store id.
    
    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id=store_id
     
    def json(self):
        return{'name': self.name,'price':self.price}
         
    @classmethod    
    def find_by_name(cls,name):# should still be a class method beacuse
    # =============================================================================
    #         connection= sqlite3.connect('data.db')
    #         cursor = connection.cursor()
    #         
    #         query ="SELECT * FROM items WHERE name=?"
    #         result = cursor.execute(query, (name,))
    #         row = result.fetchone()
    #         connection.close()
    #         if row: #return an object of type item model instead of the dictionary
    #             
    #             #return {'item': {'name': row[0], 'price': row[1]}}
    #             return cls(*row) # same as cls(row[0],row[1])
    #     
    # =============================================================================
        return cls.query.filter_by(name=name).first() #query is smething that comes from sqlalchmcemy
         #can filter by multiple vairable names
         #first returns the first row only, the first match of the name.
     
    def save_to_db(self): #update or insert does both! 
        db.session.add(self)
        db.session.commit()
        
    # =============================================================================
    #          connection = sqlite3.connect('data.db')
    #          cursor = connection.cursor()
    #          query ="INSERT INTO items VALUES (?,?)"
    #          cursor.execute(query, (self.name, self.price))#the name and price to insert)
    #          connection.commit()
    #          connection.close()
    # =============================================================================

    # =============================================================================
    #      def update(self):
    #          connection=sqlite3.connect('data.db')
    #          cursor = connection.cursor()
    #         
    #          query="UPDATE items SET price=? WHERE name=?"
    #          cursor.execute(query, (self.price,self.name))
    #         
    #          connection.commit()
    #          connection.close()
    # =============================================================================
    def delete_from_db(self):
        db.session.delete(self)
            
        db.session.commit()            
