import os
import random
import string

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(BaseHandler, self).initialize()
        
    @property
    def random_string(self):
        size = 10
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))        
