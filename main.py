#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import datetime
import jinja2
import os
import model
import dish

from google.appengine.api import users
from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        current_time = datetime.datetime.now()
        #dish.initialize()
        key = db.Key.from_path('Restaurant', 6543193696894976) #ID of Ten Ren
        restaurant = db.get(key)
        template = template_env.get_template('test.html')
        context = {
            'restaurant' : restaurant,
        }
        self.response.out.write(template.render(context))

class DishHandler(webapp2.RequestHandler):
    def get(self):
        did = self.request.get('did')
        #key = db.Key.from_path('Dish', did)
        dish = db.get(did)
        restaurant = dish.restaurant
        template = template_env.get_template('dish.html')
        context = {
                   'dish' : dish,
                   'restaurant' : restaurant,
        }
        self.response.out.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/dish', DishHandler),
], debug=True)



		##user = users.get_current_user()
		##login_url = users.create_login_url(self.request.path)
		##logout_url = users.create_logout_url(self.request.path)
		##userprefs = model.get_userprefs()
		
		#if userprefs:
		#	current_time += datetime.timedelta( 0, 0, 0, 0, 0, userprefs.tz_offset)
		
		#template = template_env.get_template('home.html')
		#context = { 
		#	'current_time' : current_time,
		#	'user': user,
		#	'login_url': login_url,
		#	'logout_url': logout_url,
		#	'userprefs': userprefs,
		#}
		#message = '<p>The time is: %s</p>' % datetime.now()