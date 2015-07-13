#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cybak-lzma
----------------------------------

Tests for `cybak-lzma` module.
"""

import unittest
import tempfile

from cybak-lzma import cybak-lzma

class ConfigFixture(unittest.TestCase):

    def setUp(self):
        # make a config file object with testable properties
        fil = tempfile.TemporaryFile()
        fil.write('[SECTION1]\ndir1=../\ndir2=~\ndirlist=./zsh_src/,/python')
        
class TestCybak-lzma(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

class ConfigTests(ConfigFixture):

    def test_configbhv(self):
       pass  

if __name__ == '__main__':
    unittest.main()
