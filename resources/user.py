# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:31:38 2020

@author: User
"""
#import sqlite3
#from flask import request
from flask_restful import Resource,reqparse
from models.user import UserModel
#to create a user class


class UserRegister(Resource):
    parser= reqparse.RequestParser()#a new object to parse the request
    parser.add_argument('username',type= str, required = True , help= "This field cannot be left blank!")
    parser.add_argument('password',type= str, required = True , help= "This field cannot be left blank!")
   
    def post(self):
            
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message":"username already exist, please try another one."},400
        try:
            user = UserModel(**data)#unpack data to data["username"] and "password") we can do this cause we are using parser
           #and we know we will always only have those 2.
        except:
            return {"message": "An error occured registering the user"}, 500 
        
        user.save_to_db()
        
        return {"message": "User created suscessfully."}, 201