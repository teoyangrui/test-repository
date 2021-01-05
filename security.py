# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:24:09 2020

@author: User
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel

#Have an inmemory table with our registered users
# =============================================================================
# 
# users = [
#        User(1, 'bob', 'asdf')
#         ]
# =============================================================================

#help us to easily find the user we are looking for. Don't need to iterate over users
# =============================================================================
# username_mapping = { u.username: u for u in users } #a set comprehension
# userid_mapping = {u.id: u for u in users}
# =============================================================================



# =============================================================================
# userid_mapping= {1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'}
# }
# =============================================================================

def authenticate(username, password):
    user= UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password): #works on all python version, system and version than ==
         #check if the password provided is the same as the password stored
         return user#used to return an authentication key00
# =============================================================================
#     user = username_mapping.get(username, None)#. get i a way to access a dictionary. it gives us the value of the key
#     #if there isnt a username with that username, we return None, instead of error with dict[key]
#     if user and safe_str_cmp(user.password,password): #works on all python version, system and version than ==
#         #check if the password provided is the same as the password stored
#         return user#used to return an authentication key00
# =============================================================================
    
def identity(payload): #use the authentication token to call the identity function, then get the user id. Once get user id means authenticated
    user_id = payload['identity']
    #return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)