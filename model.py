import datetime

from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import db

class Restaurant(db.Model):
    name = db.StringProperty()
    


class Dish(db.Model):
    name = db.StringProperty()
    categories = db.ListProperty(db.Key)
    restaurant = db.ReferenceProperty(Restaurant)

class Category(db.Model):
    name = db.StringProperty()
    menus = db.ListProperty(db.Key)
    
    @property
    def dishes(self):
        return Dish.all().filter('categories', self.key())

class Menu(db.Model):
    name = db.StringProperty()
    restaurant = db.ReferenceProperty(Restaurant, collection_name='menus')

    @property
    def categories(self):
        return Category.all().filter('menus', self.key())




"""
Many to Many Relationship - Many Dishes to Many Categories

List of Keys Implementation:
Problems:
The limitation to keep in mind in using ListProperties is that there's a limit to the number of indexes per entity, 
and a limit to the total entity size. This means that there's a limit to the number of entities in the list (depending on 
whether you hit the index count or entity size first).

To circumvent this limitation, the ListProperty resides within the dish class to keep the list small. Many dishes belong to a few
categories; each dish has a short list of categores, while each category may havwe a long list of players.

class Dish(db.Model):
    name = db.StringPropety()
    categories = db.ListProperty(db.Key)

class Category(db.Model):
    name = db.StringProperty()
    
    @property
    def dishes(self):
        return Dish.all().filter('categories', self.key())


Sample Use:

c = db.get(category_key)
for dish in g.dishes
    print dish.name
"""

"""
One to Many Relationship - Many Menus to One Restaurant

class Menu(db.Model):
    name = db.StringPropety()
    restaurant = db.ReferenceProperty(Restaurant, collection_name='menus')

class Restaurant(db.Model):
    name = db.StringPropety()


Sample Use:

res = Restaurant(name = 'Jollibee')
res.put()


p

-------------------------------------------------+----------------------------

To print all dishes within a menu:

for dish in res.dishes:
    print dish.name
"""

"""
Lunch Menu:
Appetizers:
Egg Rolls
Chicken Wings
Dinner Menu
Small Bites:
Egg Rolls
Large Bites:
Chicken Wings
"""
    



#class Book(db.Model):
#    title = db.StringProperty(default = "")
#    author = db.StringProperty(default = "")
#    copyright_year = db.IntegerProperty(default = 0)
#    author_birthdate = db.DateTimeProperty(default = datetime.datetime.now())



#class UserPrefs(db.Model):
#    tz_offset = db.IntegerProperty(default = 0)
#    user = db.UserProperty(auto_current_user_add=True)
#    book = db.ReferenceProperty(Book)

#    def cache_set(self):
#		memcache.set('UserPrefs:' + self.key().name(), self)
	
#    def put(self):
#		super(UserPrefs, self).put()
#		self.cache_set()

#def get_userprefs(user_id=None):
#	if not user_id:
#		user = users.get_current_user()
#	if not user:
#		return None
#	user_id = user.user_id()

#	userprefs = memcache.get('UserPrefs:' + user_id)
	
#	if not userprefs:
#		key = db.Key.from_path('UserPrefs', user_id)
#		userprefs = db.get(key)
#		if userprefs:
#			userprefs.cache_set()
#		else:
#			userprefs = UserPrefs(key_name=user_id)
#	return userprefs


#def get_book(input):
#    title = input
#    book = memcache.get('Book:' + title)

#    if not book:
#        key = db.Key.from_path('Books', title)
#        book = db.get(key)
#        if book:
#            pass
#        else:
#            book = Book(key_name = input, title = input)
#    return book