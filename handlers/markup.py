
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
        page_description = """Here is a bunch of text that is going to be 
                                randomized shortly. Meanwhile it is multi-line
                                and there are some < characters in it. <script>"""
        self.render("og.html", page_title=page_title,
                    page_type=page_type, page_url=page_url,
                    page_image=page_image, page_description=page_description)

class TwitterHandler(BaseHandler):
    def get(self, randomness):
        if randomness == "":
            self.redirect("/twitter/{0}".format(self.random_string))

        page_title = "This should be random."
        page_type = "summary"
        page_url = "http://roygbivs.herokupapp.com/twitter/{0}".format(randomness)
        page_image = "http://roygbivs.herokuapp.com/i/{0}.png".format(self.random_string)
        page_description = """Here is a bunch of text that is going to be """
        self.render("twitter.html", page_title=page_title,
                    page_type=page_type, page_url=page_url,
                    page_image=page_image, page_description=page_description)

