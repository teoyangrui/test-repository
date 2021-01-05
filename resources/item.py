# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:18:52 2020

@author: User
"""
#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser= reqparse.RequestParser()#a new object to parse the request
    parser.add_argument('price',type= float, required = True , help= "This field cannot be left blank!"
                            )# must pass float. No request can pass through without price
    parser.add_argument('store_id',type= int, required = True , help= "Every item needs a store id."
                        )
    #dont put self, because it there's self, it means it belongs individually to the unique object created
    #from the classs
    #without sel fmeans it applies to all class items
    @jwt_required()
    def get(self, name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json() #the json method we did before
        return {'message': "Item not found"}, 404
# =============================================================================
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         
#         query = "SELECT * FROM items WHERE name=?"
#         result = cursor.execute(query, (name,))
#         row =result.fetchone()
#         connection.close()   
#         if row:
#             return {'item': {'name': row[0], 'price': row[1]}}
# =============================================================================
    
#was find by name in item.py in resources   @classmethod
    # need to return like that cause we need
        #json format!!!! cause we return forthe server!
# # =============================================================================
# #         for item in items:
# #             if item['name']== name:
# #                return item, 200# 200 is the data exist and you retrieved it
# # =============================================================================
#         item=next(filter(lambda x:x["name"]==name,items),None)    #this is for now a filter item need to list it    
#         #next give us the first item in the filter function, if theres a second one, we can call next again
#         #will give error if there is no item left, so added the second parameter None for it toreturn None instead
#         #of Error
#         return {'item': item}, 200 if item else 404
# =============================================================================
        
#        return {'message':'Item not found'}, 404#return status 404 not found. #VERY important to use the right status codes
    
    #if we put JWT above, it will mean before using the function we need authenttication
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 #400 is the user's fault
# =============================================================================
#         if next(filter(lambda x:x["name"]==name,items),None):
#             return {'message': "An item with name '{}' already exists.".format(name)},400
# =============================================================================
        #it is a bad request if it is already in the server.
        #request_data=request.get_json(force=True)#if content header isnt set correctly. not best as even if it is not correct
        data=Item.parser.parse_args()
        print(data)
        item=ItemModel(name, data['price'], data['store_id']) #{'name': name, "price":data['price']}
        #ItemModel.insert(item) #hhave to check if databse inserted the item not
        try:
            #ItemModel.insert(item) #call insert in the item class
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500 #internal server error
        
        return item.json(), 201#application know that this have happened. 201 is created
    
# was insert from item.py in resource    @classmethod

        #items.append(item)

 
    #To do by myself to update to data base the queries!
    def delete(self, name):
        #this items like this is an items that exist only in this function but we want to use global items
        #cant use cause no more itmes list
# =============================================================================
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         
#         query = "DELETE FROM items WHERE name=?" #without this, we will delete the whole table nooooo!
#         cursor.execute( query, (name,))
#         #items = list(filter(lambda x: x['name'] != name, items)) #looking for all the elements except one
#         connection.commit()
#         connection.close()
# =============================================================================
        item= ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}
        # so that one is getting deleted, 
        
    def put(self,name):
        
        #data = request.get_json()
        data = Item.parser.parse_args() #any other names in the json payload will get erased so we only see price
        #cannot change name of the item now!
        #data only have the argument we add into parser!
        item=ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data["price"]) #update_item is now the class object so can call the functions withi
        
        if item is None:
            try:
                #updated_item.insert(updated_item) #update databse
                item = ItemModel(name, data['price'], data['store_id'])
            except:
                return {"message": "An error occured inserting the item"}, 500
        else:
            try:
                #updated_item.update(updated_item) #the item we found in items will update. 
                item.price=data['price']
            except:
                return {"message": "An error occured updating the item"}, 500
           
        item.save_to_db()
        return item.json()
    
# was update method in item.py resource    @classmethod



class ItemList(Resource):
    def get(self):
# =============================================================================
#         connection=sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         
#         query="SELECT * FROM items"
#         result = cursor.execute(query)
#         items=[]
#         
#         for row in result:
#             items.append({'name': row[0], "price": row[1]})
#         
#         connection.close()
# =============================================================================
        # wrong answer: 
        
        return {"items":[item.json() for item in ItemModel.query.all()]}, 200
    #or for people more use to programming in other ways
        r#eturn {'items': list(map(lambda x:x.json(), ItemModel.query.all()))}
        