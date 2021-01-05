# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:36:18 2020

@author: User
"""
#hi
from db import db #import this here because of circular import
from flask import Flask
#to do RESTFUL API
from flask_restful import Api
from flask_jwt import JWT #for authentication
#TO DO JWT, json web token, an offication of data, encode it to do authentication later

from security import authenticate, identity
from resources.user import UserRegister #look in the resource package.
from resources.item import Item, ItemList #must import for sql alchemy for sqlachmey to see and know and create the database table!
from resources.store import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' # tell sqlalchemy where to find the data.db file
#dont need to put sqlite, need 3 slash
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turn off the modification tracker for flask;s sqlalchemy modification
#tracker but not sqlalchemy's modification tracker.
app.secret_key = "jose"#the authentication key.
api = Api(app) #every resource has to be a class. These are the default existing resources

#tell sql to create the database for us with the name columns inside it. if not it will automatically only create a database
@app.before_first_request #decorator from flast that will run the method below it before the first request
def create_tables():
    db.create_all() #before the first request comes, it will create the data.db and all the table that exist in the file

jwt = JWT(app, authenticate, identity) #JWT create a new endpoint /auth. we send it a username and password
#if authenticate correct, jwt returns a jwt token
#tthen it calls the identity user with the authentity token and use that to get the correct user id
# app=>authenticate=>identity
# =============================================================================
# 
# class Student(Resource):
#     def get(self, name):
#         return {'student': name} #just return a dictionary with student names, where the name is the request itself.
# 
# api.add_resource(Student, '/student/<string:name>') #don't need provide dictionary
# #the second parameter is same @app.route but we no longer need to do the app routing
# app.run(port=5000)
# 
# #Test first API to help us see what request we actually need
# =============================================================================

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')

api.add_resource(UserRegister, '/register')

#we want to only run the file when we want to run it not when we import.
#cause import will run the file
if __name__=='__main__':#the name given to the file we run  
    db.init_app(app)
    app.run(port=5000, debug=True)# debug=true gives a nice page that tells us whats wrong

#Test first API to help us see what request we actually need
## ALWAYS TEST INCREMENTALLY AND MAKE SURE THEY WORK EVERYTIME

