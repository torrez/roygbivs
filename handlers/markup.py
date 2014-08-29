
import os

from base import BaseHandler

class OGHandler(BaseHandler):
    def get(self, randomness):
        if randomness == "":
            self.redirect("/og/{0}".format(self.random_string))

        page_title = "This should be random."
        page_type = "website"
        page_url = "http://roygbivs.herokuapp.com/og/{0}".format(randomness)
        page_image = "http://roygbivs.herokuapp.com/i/{0}.png".format(self.random_string)

        self.render("og.html", page_title=page_title,
                    page_type=page_type, page_url=page_url,
                    page_image=page_image)
