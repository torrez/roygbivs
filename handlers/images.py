from tornado.web import HTTPError

from base import BaseHandler

class ImageHandler(BaseHandler):
    def get(self, image_name, image_type):
        if image_type not in ("gif", "png", "jpg"):
            raise HTTPError(404)
        
        if image_type == "png":
            with open("static/blue.png", 'rb') as f:
                blue_file = f.read()
            self.set_header('Content-Type', 'image/png')
            self.write(blue_file)
        else:
            raise HTTPError(404)
