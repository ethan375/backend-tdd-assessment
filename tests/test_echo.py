#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

    class EchoTests(unittest.TestCase):
        def echo(self):
            self.assertEqual(echo.main('this is a test string'), 'this is a test string')

        def arg_parser(self):
            self.assertEqual(echo.create_parser('arg'), 'arg')

if __name__ == '__main__':
    unittest.main()
