# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:09:39 2020

@author: User
"""
#import sqlite3
from db import db
#model only helps our program to do what it has to do
# give us more flexiblity so the client are interacting with
#the resources.
class UserModel(db.Model):# this class will have the ability to interact with sqlite #cannot be the same resource to sign up
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True) #primary key means it is unique, tell them  id is an integer key and a primary key
    username = db.Column(db.String(80)) #80 limits the size of the username to 80
    password = db.Column(db.String(80)) #we tell sequel alchemy this are the three columns it must have. so 
    #username provided in  __init__ must match username and password to be stored in the database
    #prevents nonsense from being stored!
    #SQLalchemy automatically pump in these username and passwords to create these objects.(users here and items on the other side).
    #need these for sql alchemy to help us connec
    
    def __init__(self,  username, password):
        #self.id = _id #dont need to create as sqlchemy will create for us, this creates another primary id making 
        #it difficult as i have to update it too
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_by_username(cls, username):

        return cls.query.filter_by(username=username).first() #either return userobject or none
        # returns select * from user, an object which allows us to build query filter by username=username tablename=argument
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()