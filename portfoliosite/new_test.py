#!/usr/bin/env python

Site = 'New Test'

Timezone = 'Pacific/Honolulu'

Colors = '''
    base03:    #002b36;
    base02:    #073642;
    base01:    #586e75;
    base00:    #657b83;
     base0:    #839496;
     base1:    #93a1a1;
     base2:    #eee8d5;
     base3:    #fdf6e3;
    yellow:    #b58900;
    orange:    #cb4b16;
       red:    #dc322f;
   magenta:    #d33682;
    violet:    #6c71c4;
      blue:    #268bd2;
      cyan:    #2aa198;
     green:    #859900;
''' # - http://ethanschoonover.com/solarized

Analytics = '''<script>


</script>'''


# - HTML Page Code

main_page_html = '''<style>

</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Hi</span></header>

</div><!-- - /page_html - -->'''

form_page_html = '''<style>
.form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
tr { height: 32px; }
td.label { font-size: 14px; text-align: right; padding-right: 10px; }
input[type="text"] { width: 200px; height: 16px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Fill Out The Form</span></header>
  <article class="form_wrap">
    <form action="../../add_form" enctype="multipart/form-data" method="post">
      <table>
        <tr>
          <td class="label">Email Addess</td>
          <td class="input"><input type="text" name="email_address" /></td>
        </tr>
        <tr>
          <td class="label">User Name</td>
          <td class="input"><input type="text" name="user_name" /></td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right"><input type="submit" value="Sign Up" /></td>
        </tr>
      </table>
    </form>
  </article><!-- - /form_wrap - -->
</div><!-- - /page_html - -->'''


entries_page_html = '''<style>
.text_wrap { margin-left: 65px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Form Entries</span></header>
  <article class="text_wrap">
    <p>Sign in as an &nbsp; <b><span class="color_a">Admin User</span></b> &nbsp; to view form data</p>
  </article><!-- - /form_wrap - -->
</div><!-- - /page_html - -->'''


entries_page_html_admin = '''<style>
.list_wrap { margin-left: 25px; margin-top: 45px; }
.item_wrap { width: 400px; border-bottom: 1px solid #eee; padding: 15px; padding-bottom: 10px; margin-top: 45px; }
.item_wrap:hover { border-bottom: 1px solid #657b83; }
.right_wrap { float: right; text-align: right; font-size: 12px; }
.right_wrap a { color: #cb4b16; }
.right_wrap a:hover { text-decoration: underline; }
.id_wrap { padding-top 40px; color: #839496; }
.email_address { font-size: 14px; line-height: 20px; }
.user_name { font-size: 22px; color: #073642; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Form Entries</span></header>
  <article class="list_wrap">
    <div class="item_wrap" ng-repeat="item in items">
      <div class="item_data">

        <div class="right_wrap">
          <p><a href ng-click="delete(item.data_id)">Delete</a></p>
          <div class="id_wrap">[!item.data_id!]</div>
        </div><!-- - /right_wrap - -->

        <p><span class="email_address">[!item.email_address!]</span>
        <br />
        <span class="user_name">[!item.user_name!]</span></p>
        
      </div><!-- - /item_data - -->
    </div><!-- - /item_data - -->
  </article><!-- - /list_wrap - -->
</div><!-- - /page_html - -->'''


code_page_html = '''<style>
.link_wrap { margin-left: 85px; margin-top: 45px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Code Link</span></header>
  <div class="link_wrap">
    <p>View on &nbsp; <a href="https://github.com/Kyle2501/App-Engine-Parts" target="_blank">GitHub</a></p>
  </div><!-- - /link_wrap - -->
</div><!-- - /page_html - -->'''


# - System
import os
import urllib
import wsgiref.handlers
import webapp2
import json
# - 
from google.appengine.api import users
from google.appengine.api import mail
# -
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
# -
import time
import datetime
from pytz.gae import pytz


class Form_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    data_id = db.StringProperty()
  #
    user_name = db.StringProperty()
    email_address = db.StringProperty()

class addForm_db(webapp2.RequestHandler):
    def post(self):
        date_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = Form_db(key_name=data_id)
        item.data_id = data_id
      # - -
        item.user_name = self.request.get('user_name')
        item.email_address = self.request.get('email_address')
      #
        item.put()
        time.sleep(1)
        self.redirect('/entries')

class deleteData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_id = base.split('?')[1]
        if users.is_current_user_admin():
            item = db.Query(Form_db).filter('data_id =', data_id).get()
        item.delete()
        time.sleep(1)
        self.redirect('../../list/entries')


class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'main'
        analytics = Analytics
        page_html = main_page_html
        admin = ''
        if users.is_current_user_admin():
            admin = 'true' 

        if path_layer == 'form':
            page_id = 'form'
            page_name = 'Form'
            page_html = form_page_html

        if path_layer == 'entries':
            page_id = 'entries'
            page_name = 'Entries'
            if admin == 'true':         
                page_html = entries_page_html_admin #!
            else:
                page_html = entries_page_html

        if path_layer == 'code':
            page_id = 'code'
            page_name = 'Code'
            page_html = code_page_html
               
      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'page_html': page_html,
            
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/publicSite.html')
        self.response.out.write(template.render(path, objects))


class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        if users.is_current_user_admin():
            if base == 'entries':
                q = db.Query(Form_db, projection=('data_id', 'email_address', 'user_name'))
                db_data = q.order('-addTime').fetch(50)
        data = []
        for f in db_data:
            data.append(db.to_dict(f))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))


app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/form/?', publicSite),
      ('/add_form/?', addForm_db),
      ('/delete/data/?', deleteData),
    ('/entries/?', publicSite),
      ('/list/entries/?', listData),
    ('/code/?', publicSite),


], debug=True)

