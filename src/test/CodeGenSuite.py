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

    # def test_5(self):
    #         input = """
    #         foo: function integer() {
    #             return 1;
    #         }
            
    #         main: function void() {
    #             for (i = 0, i < 5, i + 1) {
    #                 printInteger(i);
    #             }
    #         }
    #         """
    #         expect = """1\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_6(self):
    #         input = """
    #         foo: function integer() {
    #             return 1;
    #         }
            
    #         main: function void() {
    #             i: integer = 5;
                
    #             do {
    #                 printInteger(i);
    #                 i = i - 1;
    #             } while (i >= 6);
    #         }
    #         """
    #         expect = """5\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 502))
        
    # def test_7(self):
    #     input = """
    #     foo: function string() {
    #         return "abc";
    #     }
        
    #     main: function void() {
    #         printString(foo() :: "buhbuh");
    #     }
    #     """
    #     expect = """abcbuhbuh\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_7(self):
    #     input = """
    #     foo: function string() {
    #         return "abc";
    #     }
        
    #     arr: array[3] of integer = {1,2,3};
    #     main: function void() {
    #         printInteger(arr[0]);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_8(self):
    #     input = """
    #     foo: function string() {
    #         return "abc";
    #     }
        
    #     main: function void() {
    #         i: integer = 10;
            
    #         do {
    #             i = i - 1;
    #             if (i > 5) {
    #                 continue;
    #             }
    #             printInteger(i);
    #         } while (i > 0);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_9(self):
    #     input = """
    #     //foo: function string() {
    #     //    return "abc";
    #     //}
        
    #     main: function void() {
    #         x: array[3] of integer = {1,2,3};
    #         x[0] = 12;
    #         printInteger(x[0]);
    #     }
    #     """
    #     expect = """12\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    # def test_10(self):
    #     input = """
    #     //foo: function string() {
    #     //    return "abc";
    #     //}
        
    #     main: function void() {
    #         x: array[3] of string = {"a","b","c"};
    #         x[0] = "hiii";
    #         printString(x[0]);
    #     }
    #     """
    #     expect = """hiii\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    def test_10(self):
        input = """
        //foo: function string() {
        //    return "abc";
        //}
        
        x: array[3] of integer = {1,2,3};
        main: function void() {
            x[0] = 10;
            s: string = "ldc";
            ff: float = 2.1e4;
            printInteger(x[0]);
            printFloat(ff);
        }
        """
        expect = """10\n21000.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))