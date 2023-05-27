import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #     main: function void() {
    #         x: integer = 10;
    #         printInteger(x);
    #     }
    #     """
    #     expect = """10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    # def test_2(self):
    #     input = """
    #     main: function void() {
    #         x: float = 10e1;
    #         printFloat(x);
    #     }
    #     """
    #     expect = """100.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_3(self):
    #     input = """
    #     main: function void() {
    #         x: boolean = true;
    #         printBoolean(x);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    # def test_4(self):
    #     input = """
    #     main: function void() {
    #         x: string = "abc\\n";
    #         printString(x);
    #     }
    #     """
    #     expect = """abc\n\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    # def test_5(self):
    #     input = """
    #     main: function void() {
    #         x: string = "abc\\n";
    #         printString(x :: "123");
    #     }
    #     """
    #     expect = """abc\n123\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
    
    # def test_6(self):
    #     input = """
    #     main: function void() {
    #         printInteger(1);
    #         printFloat(1.9);
    #         printBoolean(true);
    #         printString("abc");
    #     }
    #     """
    #     expect = """1\n1.9\ntrue\nabc\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))
    
    # def test_7(self):
    #     input = """
    #     x: integer = 10;
    #     main: function void() {
    #         printInteger(x);
    #     }
    #     """
    #     expect = """10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    # def test_8(self):
    #     input = """
    #     x: float = 10e1;
    #     main: function void() {
    #         printFloat(x);
    #     }
    #     """
    #     expect = """100.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    # def test_9(self):
    #     input = """
    #     x: boolean = true;
    #     main: function void() {
    #         printBoolean(x);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    # def test_10(self):
    #     input = """
    #     x: string = "abc\\n";
    #     main: function void() {
    #         printString(x);
    #     }
    #     """
    #     expect = """abc\n\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    # def test_11(self):
    #     input = """
    #     x: string = "abc\\n";
    #     main: function void() {
    #         printString(x :: "heyyyyy");
    #     }
    #     """
    #     expect = """abc\nheyyyyy\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    # def test_12(self):
    #     input = """
    #     main: function void() {
    #         x: integer = 10 + 9 - 1 / 2 * 100 % 20;
    #         printInteger(x);
    #     }
    #     """
    #     expect = """19\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    # def test_13(self):
    #     input = """
    #     main: function void() {
    #         x: float = 10e1 * 10 - (9.4 + 1.e3) * 10 / 5.4;
    #         printFloat(x);
    #     }
    #     """
    #     expect = """-869.2593\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    # def test_14(self):
    #     input = """
    #     main: function void() {
    #         y: boolean = false && true || true;
    #         x: boolean = true || false && true && !y;
    #         printBoolean(x);
    #     }
    #     """
    #     expect = """false\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    # def test_15(self):
    #     input = """
    #     main: function void() {
    #         x: string = "abc\\n" :: "hel no\\t Word";
    #         printString(x);
    #     }
    #     """
    #     expect = """abc\nhel no	 Word\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    # def test_16(self):
    #     input = """
    #     x: function integer() {
    #         return 10;
    #     }
    #     main: function void() {
    #         printInteger(x());
    #     }
    #     """
    #     expect = """10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    # def test_17(self):
    #     input = """
    #     x: function float() {
    #         return 10e1;
    #     }
    #     main: function void() {
    #         printFloat(x());
    #     }
    #     """
    #     expect = """100.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    # def test_18(self):
    #     input = """
    #     x: function float() {
    #         return 10;
    #     }
    #     main: function void() {
    #         printFloat(x());
    #     }
    #     """
    #     expect = """10.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    # def test_19(self):
    #     input = """
    #     x: function boolean() {
    #         return true;
    #     }
    #     main: function void() {
    #         printBoolean(x());
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    # def test_20(self):
    #     input = """
    #     x: function string() {
    #         x: string = "abc\\n";
    #         return x;
    #     }
    #     main: function void() {
    #         printString(x());
    #     }
    #     """
    #     expect = """abc\n\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    # def test_21(self):
    #     input = """
    #     x: function integer() {
    #         return 10 * 67 - 0 + 19;
    #     }
    #     main: function void() {
    #         printInteger(x());
    #     }
    #     """
    #     expect = """689\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    # def test_22(self):
    #     input = """
    #     x: function float() {
    #         return 10e1 / 89.0 * 333;
    #     }
    #     main: function void() {
    #         printFloat(x());
    #     }
    #     """
    #     expect = """374.1573\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    # def test_23(self):
    #     input = """
    #     x: function float() {
    #         return 10;
    #     }
    #     main: function void() {
    #         y: float = 123;
    #         printFloat(x());
    #         printFloat(y + 1 - 2);
    #     }
    #     """
    #     expect = """10.0\n122.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    # def test_24(self):
    #     input = """
    #     x: function boolean() {
    #         return true || false && !false;
    #     }
    #     main: function void() {
    #         printBoolean(x());
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    # def test_25(self):
    #     input = """
    #     x: function string() {
    #         x: string = "abc";
    #         return x :: "plz dont give up!!";
    #     }
    #     main: function void() {
    #         printString(x());
    #     }
    #     """
    #     expect = """abcplz dont give up!!\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))
        
    # def test_26(self):
    #     input = """
    #     x: function float() {
    #         return 10;
    #     }
    #     main: function void() {
    #         y: float;
    #         y = 80;
    #         printFloat(x());
    #         printFloat(y - 10);
    #     }
    #     """
    #     expect = """10.0\n70.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    # def test_27(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of integer = {1, 2, 3};
    #         printInteger(x[0] + x[2]);
    #     }
    #     """
    #     expect = """4\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_28(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of float = {1.4, 2.e-1, 3E2};
    #         printFloat(x[0] + x[2] - 2 * x[1]);
    #     }
    #     """
    #     expect = """301.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    # def test_29(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of boolean = {true, false, !false && true};
    #         printBoolean(x[1] || x[2]);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    # def test_30(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of string = {"principle of ", "programming ", "language"};
    #         printString((x[0] :: x[1]) :: x[2]);
    #     }
    #     """
    #     expect = """principle of programming language\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    # def test_31(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of float = {1.4, 2.e-1, 3E2};
    #         x[1] = 100 - 1;
    #         printFloat(2 + 1 + x[2]);
    #     }
    #     """
    #     expect = """303.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    # def test_32(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of integer = {1 + 2 - 1, 2 % 20, 3 / 2 + 0 - 120};
    #         printInteger(x[0] + x[2]);
    #     }
    #     """
    #     expect = """-117\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_33(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of float = {1.4 / 3, 2.e-1 + 9 - 2, 3E2 * 21};
    #         printFloat(-1 + x[0] + x[2] - 2 * x[1]);
    #     }
    #     """
    #     expect = """6285.067\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    # def test_34(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of boolean = {!!!(true), 123 > 9, !(2 <= 4)};
    #         printBoolean(x[1] && !x[2]);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    # def test_35(self):
    #     input = """
    #     main: function void() {
    #         x: array[3] of string = {"principle " :: "of ", "programming" :: " ", "language" :: " (PPL)"};
    #         printString((x[0] :: x[1]) :: x[2]);
    #     }
    #     """
    #     expect = """principle of programming language (PPL)\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    # def test_36(self):
    #     input = """
    #     x: array[3] of integer = {1, 2, 3};
    #     main: function void() {
    #         printInteger(x[0] + x[2]);
    #     }
    #     """
    #     expect = """4\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_37(self):
    #     input = """
    #     x: array[3] of float = {1.4, 2.e-1, 3E2};
    #     main: function void() {
    #         printFloat(x[0] + x[2] - 2 * x[1]);
    #     }
    #     """
    #     expect = """301.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    # def test_38(self):
    #     input = """
    #     x: array[3] of boolean = {true, false, !false && true};
    #     main: function void() {
    #         printBoolean(x[1] || x[2]);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    # def test_39(self):
    #     input = """
    #     x: array[3] of string = {"principle of ", "programming ", "language"};
    #     main: function void() {
    #         printString((x[0] :: x[1]) :: x[2]);
    #     }
    #     """
    #     expect = """principle of programming language\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    # def test_40(self):
    #     input = """
    #     x: array[3] of float = {1.4, 2.e-1, 3E2};
    #     main: function void() {
    #         x[1] = 100 - 1;
    #         printFloat(2 + 1 + x[2]);
    #     }
    #     """
    #     expect = """303.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))
    
    # def test_41(self):
    #     input = """
    #     x: array[3] of integer = {1 + 2 - 1, 2 % 20, 3 / 2 + 0 - 120};
    #     main: function void() {
    #         printInteger(x[0] + x[2]);
    #     }
    #     """
    #     expect = """-117\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # def test_42(self):
    #     input = """
    #     x: array[3] of float = {1.4 / 3, 2.e-1 + 9 - 2, 3E2 * 21};
    #     main: function void() {
    #         printFloat(-1 + x[0] + x[2] - 2 * x[1]);
    #     }
    #     """
    #     expect = """6285.067\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    # def test_43(self):
    #     input = """
    #     x: array[3] of boolean = {!!!(true), 123 > 9, !(2 <= 4)};
    #     main: function void() {
    #         printBoolean(x[1] && !x[2]);
    #     }
    #     """
    #     expect = """true\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    # def test_44(self):
    #     input = """
    #     x: array[3] of string = {"principle " :: "of ", "programming" :: " ", "language" :: " (PPL)"};
    #     main: function void() {
    #         printString((x[0] :: x[1]) :: x[2]);
    #     }
    #     """
    #     expect = """principle of programming language (PPL)\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    # def test_45(self):
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
    #     expect = """false\n-80\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    # def test_46(self):
    #     input = """
    #     main: function void() {
    #         arr: array[10] of integer;
    #         arr[0] = 10;
    #         x: integer = 10 % 3;
    #         printInteger(x);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))
    
    # def test_47(self):
    #     input = """
    #     main: function void() {
    #         if (true) {
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
    #     expect = """1\n3\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    # def test_48(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 12;
    #         while (i >= 0) {
    #             printInteger(i);
    #             i = i - 1;
    #         }
    #     }
    #     """
    #     expect = """12\n11\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))

    # def test_49(self):
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
    #         expect = """0\n1\n2\n3\n4\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    # def test_50(self):
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
    #         self.assertTrue(TestCodeGen.test(input, expect, 550))
        
    # def test_51(self):
    #     input = """
    #     foo: function string() {
    #         return "abc";
    #     }
        
    #     main: function void() {
    #         printString(foo() :: "buhbuh");
    #     }
    #     """
    #     expect = """abcbuhbuh\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))
    
    # def test_52(self):
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
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))
    
    # def test_53(self):
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
    #     expect = """5\n4\n3\n2\n1\n0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    # def test_54(self):
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
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))
    # def test_55(self):
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
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))
    # def test_56(self):
    #     input = """
    #     //foo: function string() {
    #     //    return "abc";
    #     //}
        
    #     x: array[3] of integer = {1,2,3};
    #     main: function void() {
    #         x[0] = 10;
    #         s: string = "ldc";
    #         ff: float = 2.1e4;
    #         printInteger(x[0]);
    #         printFloat(ff);
    #     }
    #     """
    #     expect = """10\n21000.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    # def test_57(self):
    #     input = """
    #     //foo: function string() {
    #     //    return "abc";
    #     //}
        
    #     x: array[3] of string = {"a","b","c"};
    #     main: function void() {
    #         //x[0] = "hello world!!!";
    #         x[1] = x[1] :: " sb";
    #         printString(x[1]);
    #     }
    #     """
    #     expect = """b sb\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))
        
    # def test_58(self):
    #     input = """
    #     x: array[3] of integer = {1,2,3};
        
    #     foo: function integer() {
    #         x[0] = 3 + 3;
    #         return x[0];
    #     }
        
    #     main: function void() {
    #         b: integer = foo();
    #         printInteger(b);
    #     }
    #     """
    #     expect = """6\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    # def test_59(self):
    #     input = """
    #     foo: function integer(i: integer) {
    #         x: array[3] of integer = {1,2,3};
    #         return x[i];
    #     }
        
    #     main: function void() {
    #         x: array[3] of integer = {foo(0), foo(1), foo(2)};
    #         printInteger(x[2] % x[1]);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))
    
    # def test_60(self):
    #     input = """
    #     foo: function float(i: integer) {
    #         x: array[3] of float = {1.5,2.2,3.22343};
    #         return x[i];
    #     }
        
    #     main: function void() {
    #         x: array[3] of float = {foo(0), foo(1), foo(2)};
    #         printFloat(x[2] - x[1]);
    #     }
    #     """
    #     expect = """1.0234299\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    # def test_61(self):
    #     input = """
    #     main: function void() {
    #         if (true || false && true) {
    #             printInteger(537);
    #         }
            
    #         x: boolean = true;
    #         if (!!!!!!!!!!!!!!!!x) {
    #             printInteger(2345);
    #         }
    #         else {
    #             printInteger(346);
    #         }
    #     }
    #     """
    #     expect = """537\n2345\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    # def test_62(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 5;
    #         while (i >= 0) {
    #             printInteger(i * 10);
    #             i = i - 2;
    #         }
    #     }
    #     """
    #     expect = """50\n30\n10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))

    # def test_63(self):
    #         input = """
    #         foo: function integer(i: integer) {
    #             return i * 20 % 3 - (-9);
    #         }
            
    #         main: function void() {
    #             for (i = 0, i < 5, i + 1) {
    #                 printInteger(i);
    #             }
    #         }
    #         """
    #         expect = """0\n1\n2\n3\n4\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    # def test_64(self):
    #         input = """
    #         foo: function float(i: integer) {
    #             return i * 2;
    #         }
            
    #         main: function void() {
    #             i: integer = 5;
                
    #             do {
    #                 printFloat(foo(i));
    #                 i = i - 1;
    #             } while (i >= 6);
    #         }
    #         """
    #         expect = """10.0\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    # def test_65(self):
    #     input = """
    #     main: function void() {
    #         x: boolean = true;
    #         if (!!!x) {
    #             printInteger(2345);
    #             if (true || false && true) {
    #                 printInteger(537);
    #             }
    #         }
    #         else if (true) {
    #             printString("Visit elif");
    #         }
    #         else if (true) {
    #             printString("Visit elif 2");
    #         }
    #         else {
    #             printInteger(346);
    #         }
    #     }
    #     """
    #     expect = """Visit elif\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    # def test_66(self):
    #     input = """
    #     foo: function integer (x: integer, y: integer) {
    #         return x * y + 1;
    #     }
    #     main: function void() {
    #         i: integer = 8;
    #         while (i >= 0) {
    #             printInteger(foo(10, i));
    #             i = i - 2;
    #         }
    #     }
    #     """
    #     expect = """81\n61\n41\n21\n1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    # def test_67(self):
    #     input = """
    #     foo: function integer (x: integer, y: integer) {
    #         return x * y / 10;
    #     }
    #     main: function void() {
    #         i: integer = 8;
    #         while (i >= 0) {
    #             if (i >= 6) {
    #                 i = i - 1;
    #                 continue;
    #             }
    #             printInteger(foo(100, i));
    #             i = i - 2;
    #         }
    #     }
    #     """
    #     expect = """50\n30\n10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    # def test_68(self):
    #     input = """
    #     foo: function integer (x: integer, y: integer) {
    #         return (x * y + 3) % 5;
    #     }
    #     main: function void() {
    #         i: integer = 8;
    #         while (i >= 0) {
    #             if (i <= 3) {
    #                 break;
    #             }
    #             printInteger(foo(100, i));
    #             i = i - 2;
    #         }
    #     }
    #     """
    #     expect = """3\n3\n3\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))

    # def test_69(self):
    #         input = """
            
    #         main: function void() {
    #             ff: integer = 10;
    #             for (i = 0, i < 10, i + 1) {
    #                 if (i >= 7) continue;
    #                 printInteger(i);
    #             }
    #         }
    #         """
    #         expect = """0\n1\n2\n3\n4\n5\n6\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    # def test_70(self):
    #         input = """
    #         foo: function integer(i: integer) {
    #             return i * 20 % 3 - (-9);
    #         }
            
    #         main: function void() {
    #             ff: integer = 10;
    #             for (i = 0, i < 10, i + 1) {
    #                 if (i <= 3) break;
    #                 printInteger(foo(i));
    #             }
    #         }
    #         """
    #         expect = """"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    # def test_71(self):
    #         input = """
    #         foo: function float(i: integer) {
    #             return i * 2;
    #         }
            
    #         main: function void() {
    #             i: integer = 9;
                
    #             do {
    #                 if (i <= 3) break;
    #                 printFloat(foo(i));
    #                 i = i - 1;
    #             } while (i >= 0);
    #         }
    #         """
    #         expect = """18.0\n16.0\n14.0\n12.0\n10.0\n8.0\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    # def test_72(self):
    #         input = """
    #         foo: function float(i: integer) {
    #             return i * 2;
    #         }
            
    #         main: function void() {
    #             i: integer = 15;
                
    #             do {
    #                 if (i <= 3) {
    #                     i = i - 2;
    #                     continue;
    #                 }
    #                 printFloat(foo(i));
    #                 i = i - 1;
    #             } while (i >= 0);
    #         }
    #         """
    #         expect = """30.0\n28.0\n26.0\n24.0\n22.0\n20.0\n18.0\n16.0\n14.0\n12.0\n10.0\n8.0\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    # def test_73(self):
    #         input = """
    #         foo: function void(i: integer) {
    #             if (i == 0) {
    #                 return;
    #             }
    #             printInteger(i);
    #             foo(i - 1);
    #         }
            
    #         main: function void() {
    #             foo(5);
    #         }
    #         """
    #         expect = """5\n4\n3\n2\n1\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    # def test_74(self):
    #         input = """
    #         foo: function void(i: float, count: integer) {
    #             if (count <= -1) {
    #                 return;
    #             }
    #             printFloat(i);
    #             foo(i - 0.8, count - 1);
    #         }
            
    #         main: function void() {
    #             foo(5.1, 3);
    #         }
    #         """
    #         expect = """5.1\n4.2999997\n3.4999998\n2.6999998\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    # def test_75(self):
    #         input = """
    #         foo: function void(i: string, count: integer) {
    #             if (count <= -1) {
    #                 return;
    #             }
    #             printString(i :: "a");
    #             foo(i :: "a", count - 1);
    #         }
            
    #         main: function void() {
    #             foo("hello", 4);
    #         }
    #         """
    #         expect = """helloa\nhelloaa\nhelloaaa\nhelloaaaa\nhelloaaaaa\n"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    # def test_76(self):
    #     input = """
    #     foo: function void(i: boolean, count: integer) {
    #         if (count <= -1) {
    #             return;
    #         }
    #         printBoolean(!i);
    #         foo(!i, count - 1);
    #     }
        
    #     main: function void() {
    #         foo(true, 4);
    #     }
    #     """
    #     expect = """false\ntrue\nfalse\ntrue\nfalse\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    def test_77(self):
        input = """
        foo: function void() {
            
        }
        
        main: function void() {
            x: integer = - (10 + 8 - 2) % 17;
            printInteger(x);
        }
        """
        expect = """-16\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))
    
    def test_78(self):
        input = """
        main: function void() {
            x: float = 10e1 / 4E-1 + 1.3;
            printFloat(x);
        }
        """
        expect = """251.3\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test_79(self):
        input = """
        z: boolean = true || !false;
        main: function void() {
            x: boolean = true || true || true || true;
            x = x && false;
            y: boolean = true;
            printBoolean(x && y || !z);
        }
        """
        expect = """false\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    def test_80(self):
        input = """
        main: function void() {
            x: string = "abc\\n" :: "123";
            y: string = "dsf";
            z: string = "sfdsg";
            x = x :: y;
            y = y :: z;
            x = x :: z;
            x = x :: y;
            printString(x);
        }
        """
        expect = """abc\n123dsfsfdsgdsfsfdsg\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    
    
    def test_81(self):
        input = """
        main: function void() {
            printInteger(1 + 90 - 20);
            printFloat(1.9 + 0.1);
            printBoolean(true || false);
            printString("abc" :: "abc");
        }
        """
        expect = """71\n2.0\ntrue\nabcabc\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test_82(self):
        input = """
        x: function integer(i: integer) {
            return i + 10 / 2 + 100;
        }
        main: function void() {
            arr: array[2] of integer = {1, 2};
            printInteger(x(arr[0]));
        }
        """
        expect = """106\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test_83(self):
        input = """
        x: function float(f: float) {
            return 10e1 + f;
        }
        main: function void() {
            arr: array[2] of float = {1.2, 2.4};
            printFloat(x(arr[1]));
        }
        """
        expect = """102.4\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test_84(self):
        input = """
        x: function boolean(z: boolean) {
            return true && z;
        }
        main: function void() {
            z: boolean = true;
            arr: array[5] of boolean = {true, false, false || true, false, z};
            printBoolean(x(arr[4]));
        }
        """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    
    def test_85(self):
        input = """
        x: function string(s: string) {
            x: string = "abc\\n";
            return x :: s;
        }
        main: function void() {
            s: string = "uoi";
            a: array[4] of string = {"asg", s, "asdg", "dfg"};
            printString(x(a[1]));
        }
        """
        expect = """abc\nuoi\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test_86(self):
        input = """
        x: array[3] of integer = {1,2,3};
        
        foo: function integer() {
            x[0] = 3 + x[1];
            return x[0];
        }
        
        foo1: function integer() {
            return 8;
        }
        
        main: function void() {
            b: integer = foo();
            b = foo1() / b;
            printInteger(b);
        }
        """
        expect = """1\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test_87(self):
        input = """
        x: array[3] of float = {1.4,2e-1,3E2};
        
        foo: function float() {
            x[0] = 3.234 + x[1];
            return x[0];
        }
        
        foo1: function float() {
            return 8;
        }
        
        main: function void() {
            b: float = foo();
            b = foo1() / b;
            printFloat(b);
        }
        """
        expect = """2.3296447\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))
    
    def test_88(self):
        input = """
        x: array[3] of boolean = {true, false, true};
        
        foo: function boolean() {
            x[0] = x[0] || true && x[1];
            return x[0];
        }
        
        foo1: function boolean() {
            return true;
        }
        
        main: function void() {
            b: boolean = foo();
            b = foo1() || !b;
            printBoolean(b);
        }
        """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    def test_89(self):
        input = """
        x: array[3] of string = {"adsf", "hrtjr", "adsgrteyh"};
        
        foo: function string() {
            x[0] = "hnalsdkhf" :: x[1];
            return x[0];
        }
        
        foo1: function string() {
            return "y7435683476589734658973456";
        }
        
        main: function void() {
            b: string = foo();
            b = foo1() :: b;
            printString(b);
        }
        """
        expect = """y7435683476589734658973456hnalsdkhfhrtjr\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_90(self):
        input = """
        x: integer = foo1();
        
        foo1: function integer() {
            return 8;
        }
        
        main: function void() {
            b: integer = 324;
            b = b / x;
            printInteger(b);
        }
        """
        expect = """40\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test_91(self):
        input = """
        x: float = foo1();
        
        foo1: function float() {
            return 8;
        }
        
        main: function void() {
            b: float = 3.24e-1;
            b = b * x - 10;
            printFloat(b);
        }
        """
        expect = """-7.408\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 591))
    
    def test_92(self):
        input = """
        x: boolean = foo1();
        
        foo1: function boolean() {
            return true || false;
        }
        
        main: function void() {
            b: boolean = foo1();
            z: boolean = false;
            b = b || false && z;
            printBoolean(b);
        }
        """
        expect = """false\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test_93(self):
        input = """
        x: string = foo1();
        
        foo1: function string() {
            return "hello " :: "gogogo";
        }
        
        main: function void() {
            b: string = foo1();
            z: string = "yyxzz";
            b = (b :: z) :: "ppl";
            printString(b);
        }
        """
        expect = """hello gogogoyyxzzppl\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    def test_94(self):
        input = """
        foo1: function integer(i: integer) {
            return 8 * i;
        }
        
        arr: array[4] of integer = {21,foo1(1),6,8};
        
        main: function void() {
            b: integer = 324;
            b = b / arr[1];
            printInteger(b);
        }
        """
        expect = """40\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test_95(self):
        input = """
        foo1: function float(i: integer) {
            return 8 * i;
        }
        
        arr: array[4] of float = {21.4,foo1(1),6e-2,8.4e1};
        
        main: function void() {
            b: float = 324;
            b = b * arr[1] / arr[0] + arr[2];
            printFloat(b);
        }
        """
        expect = """121.181496\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    def test_96(self):
        input = """
        foo1: function string(i: integer) {
            if (i == 0) {
                return "rot ppl ";
            }
            else if (i == 1)
                return "tach ppl ";
            else if (i == 2)
                return "fanclub ppl ";
            return "hoc lai ppl ";
        }
        
        arr: array[4] of string = {foo1(0), foo1(1), foo1(2), foo1(3)};
        
        main: function void() {
            a: string = arr[0] :: arr[1];
            b: string = arr[2] :: arr[3];
            printString(b :: a);
        }
        """
        expect = """fanclub ppl hoc lai ppl rot ppl tach ppl \n"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    def test_97(self):
        input = """
        foo1: function boolean(i: integer) {
            if (i == 0) {
                return true;
            }
            return false;
        }
        
        arr: array[4] of boolean = {foo1(0), foo1(1), foo1(2), foo1(3)};
        
        main: function void() {
            a: boolean = arr[0] || arr[1];
            b: boolean = arr[2] && arr[3];
            printBoolean(!!!!!!!!!!!!b || !!!!!!!!!!!!!!a);
        }
        """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test_98(self):
        input = """
        foo1: function integer(i: integer) {
            return 8 * i;
        }
        
        arr: array[4] of integer = {21,foo1(1),6,8};
        
        main: function void() {
            b: integer = 324;
            b = b / arr[1];
            b = b / 10;
            
            while (b >= 3) {
                printInteger(b);
                b = b - 1;
                i: integer = 3;
                while (i >= 0) {
                    printString("googogogoogog");
                    i = i - 1;
                }
            }
        }
        """
        expect = """4\ngoogogogoogog\ngoogogogoogog\ngoogogogoogog\ngoogogogoogog\n3\ngoogogogoogog\ngoogogogoogog\ngoogogogoogog\ngoogogogoogog\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    def test_99(self):
        input = """
        foo1: function string(i: integer) {
            if (i == 0) {
                return "rot ppl ";
            }
            else if (i == 1)
                return "tach ppl ";
            else if (i == 2)
                return "fanclub ppl ";
            return "hoc lai ppl ";
        }
        
        arr: array[4] of string = {foo1(0), foo1(1), foo1(2), foo1(3)};
        
        main: function void() {
            a: string = arr[0] :: arr[1];
            b: string = arr[2] :: arr[3];
            printString(b :: a);
            
            for (j = 1, j < 20, j * 2) {
                printString(arr[j % 4] :: "\\talooo");
                if (j > 15) continue;
            }
        }
        """
        expect = """fanclub ppl hoc lai ppl rot ppl tach ppl 
tach ppl 	alooo
fanclub ppl 	alooo
rot ppl 	alooo
rot ppl 	alooo
rot ppl 	alooo
"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
    
    def test_100(self):
        input = """
        foo1: function string(i: integer) {
            if (i == 0) {
                return "rot ppl ";
            }
            else if (i == 1)
                return "tach ppl ";
            else if (i == 2)
                return "fanclub ppl ";
            return "hoc lai ppl ";
        }
        
        foo2: function integer(i: integer) {
            return i % 3; 
        }
        
        foo3: function boolean() {
            return true || false;   
        }
        
        foo4: function integer() {
            if (foo3()) {
                return 100;
            }
            return 263;
        }
        
        main: function void() {
            printString(foo1(foo2(foo4())));
        }
        """
        expect = """tach ppl \n"""
        self.assertTrue(TestCodeGen.test(input, expect, 600))