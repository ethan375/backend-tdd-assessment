#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import echo
import subprocess
import os


class EchoTests(unittest.TestCase):
    def test_echo(self):
        """Testing the program with no flags, should return the same string that was supplied"""
        output = subprocess.check_output(["python", "echo.py", "this is a string"])
        
        # the subprocess is putting a new line char at the end of the string so I am removing it
        output = output.strip("\n")

        self.assertEqual(output, "this is a string")


    def test_l_flag(self):
        """Running the program with the l flag should return the input string in all lowercase letters"""
        output = subprocess.check_output(["python", "echo.py", "-l", "THIS IS A STRING!!"])

        output = output.strip('\n')

        self.assertEqual(output, "this is a string!!")

    def test_lower_flag(self):
        """Running the program with the lower flag should return the input string in all lowercase letters"""
        output = subprocess.check_output(["python", "echo.py", "--lower", "THIS IS A STRING!!"])

        output = output.strip('\n')

        self.assertEqual(output, "this is a string!!")

    def test_u_flag(self):
        """Running the program with the u flag should print the string with every lettter capitalized"""
        output = subprocess.check_output(["python", "echo.py", "-u", "just anotha strang"])

        output = output.strip('\n')

        self.assertEqual(output, "JUST ANOTHA STRANG")

    def test_upper_flag(self):
        """Running the program with the upper flag should print the string with every lettter capitalized"""
        output = subprocess.check_output(["python", "echo.py", "--upper", "just anotha strang"])

        output = output.strip('\n')

        self.assertEqual(output, "JUST ANOTHA STRANG")

    def test_t_flag(self):
        """running the program with the t flag should return the string with the first letter of evey word capitalized"""
        output = subprocess.check_output(["python", "echo.py", "-t", "this is yet anotha string"])

        output = output.strip('\n')

        self.assertEqual(output, "This Is Yet Anotha String")

    def test_title_flag(self):
        """running the program with the title flag should return the string with the first letter of evey word capitalized"""
        output = subprocess.check_output(["python", "echo.py", "--title", "this is yet anotha string"])

        output = output.strip('\n')

        self.assertEqual(output, "This Is Yet Anotha String")

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

tests = EchoTests("test_echo")
tests.test_l_flag()

if __name__ == '__main__':
    unittest.main()
