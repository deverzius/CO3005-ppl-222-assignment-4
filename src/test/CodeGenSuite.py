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
    
    # def test_2(self):
    #     input = """
    #     y: integer = 10;
    #     main: function void() {
    #         jx: boolean = true;
    #         jx = false || !true;
    #         s: string = "abc" :: "a";
    #         jx = !jx && false || !true;
    #         y = -100 + 20;
    #         printBoolean(jx);
    #         printInteger(y);
    #         //printString(s);
    #     }
    #     """
    #     expect = """false-80"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_2(self):
    #     input = """
    #     main: function void() {
    #         //arr: array[10] of integer;
    #         //arr[0] = 10;
    #         x: integer = 10 % 3;
    #         printInteger(x);
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_4(self):
    #     input = """
    #     main: function void() {
    #         if (false) {
    #             printInteger(1);
    #         }
            
    #         if (false) {
    #             printInteger(2);
    #         }
    #         else {
    #             printInteger(3);
    #         }
    #     }
    #     """
    #     expect = """1\n2\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
#     def test_4(self):
#         input = """
#         main: function void() {
#             i: integer = 12;
#             while (i >= 0) {
#                 printInteger(i);
#                 i = i - 1;
#             }
#         }
#         """
#         expect = """12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_5(self):
            input = """
            foo: function integer() {
                return 100 % 5;
            }
            
            main: function void() {
                i: integer = foo();
            }
            """
            expect = """12\n"""
            self.assertTrue(TestCodeGen.test(input, expect, 502))
