#!/usr/bin/env python

import tornado.testing
import unittest
import roygbivs

TEST_MODULES = [
    'test.HomeTest',
]

class BaseTest(tornado.testing.AsyncHTTPTestCase, tornado.testing.LogTrapTestCase):
    def setUp(self):
        super(BaseTest, self).setUp()

    def tearDown(self):
        super(BaseTest, self).tearDown()        

class HomeTest(BaseTest):
    def get_app(self):
        return roygbivs.make_application(environment = roygbivs.RoygbivsApplication.TESTING)

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == "__main__":
    
    tornado.testing.main()
