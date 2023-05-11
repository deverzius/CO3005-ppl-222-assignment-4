import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #     y: integer = 10;
    #     main: function void() {
    #         printInteger(1);
    #         printFloat(1.9);
    #         printBoolean(true);
    #         printString("abc");
    #     }
    #     """
    #     expect = """11.9true"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test_2(self):
        input = """
        //y: integer = 10;
        main: function void() {
            jx: boolean = true;
            printBoolean(jx);
        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))
