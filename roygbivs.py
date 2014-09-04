import os

import tornado.web
from handlers import home, markup, images


class RoygbivsApplication(tornado.web.Application):

    DEVELOPMENT = 1
    PRODUCTION = 2
    TESTING = 3

    @classmethod
    def get_environment(cls, env_string="development"):
        environments = dict(development=cls.DEVELOPMENT,
                            production=cls.PRODUCTION, testing=cls.TESTING)
        try:
            return environments[env_string]
        except:
            return cls.DEVELOPMENT

    @staticmethod
    def environment_as_string(env):
        environments = ["development", "production", "testing"]
        try:
            return environments[env - 1]
        except:
            return "unknown"

    @classmethod
    def app_settings(cls, environment):
        dirname = os.path.dirname(os.path.abspath(__file__))
        debug = False
        if environment == cls.DEVELOPMENT:
            debug = True
        return {
            "login_url": "/sign-in",  # unecessary
            "static_path": os.path.join(dirname, "static"),
            "template_path":  os.path.join(dirname, "templates"),
            "debug": debug,
            "environment": environment,
        }

    def __init__(self, *args, **settings):
        super(RoygbivsApplication, self).__init__(*args, **settings)


def make_application(environment=RoygbivsApplication.DEVELOPMENT):
    app_settings = RoygbivsApplication.app_settings(environment)

    app = RoygbivsApplication([
        (r"/", home.IndexHandler),
        (r"/og/?(.*)", markup.OGHandler),
        (r"/twitter/?(.*)", markup.TwitterHandler),
        (r"/i/(\w+)\.(png|jpg|gif)", images.ImageHandler),
    ], **app_settings)

    return app
