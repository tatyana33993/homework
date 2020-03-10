#!/usr/bin/env python3

import pep as t
import unittest


class Testpep(unittest.TestCase):
    def test_check_good_comment(self):
        result = t.check_comments('Good comment', 1)
        self.assertEqual(result, None)

    def test_check_bad_comment(self):
        result = t.check_comments('Плохой комментарий', 2)
        self.assertEqual(result, 'line: 2 comments should be written in English')

    def test_check_bad_variable_I(self):
        result = t.check_variables('    I = 5', 3)
        self.assertEqual(result, 'line: 3, column: 3 name I is bad name')

    def test_check_bad_variable_O(self):
        result = t.check_variables('    O = 6', 4)
        self.assertEqual(result, 'line: 4, column: 3 name O is bad name')

    def test_check_bad_variable_l(self):
        result = t.check_variables('    l = 7', 5)
        self.assertEqual(result, 'line: 5, column: 3 name l is bad name')

    def test_check_good_variable(self):
        result = t.check_variables('    a = 7', 6)
        self.assertEqual(result, None)

    def test_check_bad_class_name(self):
        result = t.check_class_name('class bad_class:', 7)
        self.assertEqual(result, 'line: 7, column: 6 for the class name use CamelCase')

    def test_check_good_class_name(self):
        result = t.check_class_name('class GoodClass:', 8)
        self.assertEqual(result, None)

    def test_check_bad_def_name(self):
        result = t.check_def_name('def BadDef', 9)
        self.assertEqual(result, 'line: 9, column: 4 for the def name use lower_case_with_underscores')

    def test_check_good_def_name(self):
        result = t.check_def_name('def good_def', 10)
        self.assertEqual(result, None)

    def test_check_whitespace_before_commas(self):
        result = t.check_commas('arr = [1 , 2]', 11)
        self.assertEqual(result, 'line: 11, column: 9 whitespace before ","')

    def test_check_whitespace_after_commas(self):
        result = t.check_commas('arr = [1,2]', 12)
        self.assertEqual(result, 'line: 12, column: 8 missing whitespace after ","')

    def test_check_good_whitespaces_commas(self):
        result = t.check_commas('arr = [1, 2]', 13)
        self.assertEqual(result, None)

    def test_check_whitespace_after_square_bracket(self):
        result = t.check_brackets('arr = [ 1, 2]', 14)
        self.assertEqual(result, 'line: 14, column: 6 whitespace after "["')

    def test_check_whitespace_before_square_bracket(self):
        result = t.check_brackets('arr = [1, 2 ]', 15)
        self.assertEqual(result, 'line: 15, column: 12 whitespace before "]"')

    def test_check_whitespace_after_round_bracket(self):
        result = t.check_brackets('set = ( 1, 2)', 16)
        self.assertEqual(result, 'line: 16, column: 6 whitespace after "("')

    def test_check_whitespace_before_round_bracket(self):
        result = t.check_brackets('set = (1, 2 )', 17)
        self.assertEqual(result, 'line: 17, column: 12 whitespace before ")"')

    def test_check_good_whitespaces_square_brackets(self):
        result = t.check_brackets('arr = [1, 2]', 18)
        self.assertEqual(result, None)

    def test_check_good_whitespaces_round_brackets(self):
        result = t.check_brackets('set = (1, 2)', 19)
        self.assertEqual(result, None)

    def test_check_good_operators(self):
        result = t.check_operators('sum = 5 + 4', 20)
        self.assertEqual(result, None)

    def test_check_bad_operators(self):
        result = t.check_operators('if count== 4', 21)
        self.assertEqual(result, 'line: 21, column: 8 missing whitespace around operator')

    def test_check_good_equality_in_function_arguments(self):
        result = t.check_equality_in_function_argument('def check(arg, sum=5):', 22)
        self.assertEqual(result, None)

    def test_check_bad_equality_in_function_arguments(self):
        result = t.check_equality_in_function_argument('def check(a, b = 3):', 23)
        self.assertEqual(result, 'line: 23, column: 15 unexpected spaces around keyword / parameter equals')

    def test_check_good_whitespaces_around_key_words(self):
        result = t.check_key_words('if a = 3 and b = 4:', 24)
        self.assertEqual(result, None)

    def test_check_bad_whitespaces_around_key_words(self):
        result = t.check_key_words('if (flag)and(sum == max):', 25)
        self.assertEqual(result, 'line: 25, column: 9 missing whitespace around keyword')

    def test_check_very_bad_whitespaces_around_key_words(self):
        result = t.check_key_words('if sum == max  or  flag:', 26)
        self.assertEqual(result, 'line: 26, column: 15 multiple spaces around keyword')

    def test_check_good_extra_spaces(self):
        result = t.check_extra_spaces('flag = True', 27)
        self.assertEqual(result, None)

    def test_check_bad_extra_spaces(self):
        result = t.check_extra_spaces('flag = False  ', 28)
        self.assertEqual(result, 'line: 28, column: 14 trailing whitespace')

    def test_check_good_imports(self):
        result = t.check_imports('import sys', 29)
        self.assertEqual(result, None)

    def test_check_bad_imports(self):
        result = t.check_imports('import sys, re', 30)
        self.assertEqual(result, 'line: 30, column: 10 multiple imports on one line')

    def test_good_check_for_tabulation(self):
        result = t.check_for_tabulation('    count = 5', 31)
        self.assertEqual(result, None)

    def test_bad_check_for_tabulation(self):
        result = t.check_for_tabulation('\tcount = 7', 32)
        self.assertEqual(result, 'line: 32, column: 0 unexpected indentation')

    def test_good_check_for_semicolon(self):
        result = t.check_for_semicolon('x, y = 1, 1', 33)
        self.assertEqual(result, None)

    def test_bad_check_for_semicolon(self):
        result = t.check_for_semicolon('return True;', 34)
        self.assertEqual(result, 'line: 34, column: 11 statement ends with a semicolon')

    def test_good_check_lenght_string(self):
        result = t.check_lenght_string('small string', 35)
        self.assertEqual(result, None)

    def test_bad_check_lenght_string(self):
        result = t.check_lenght_string('This is very very very very very very very very very very very very very very very very very very long string', 36)
        self.assertEqual(result, 'line: 36, column: 80 line too long (109 > 79 characters)')

if __name__ == '__main__':
    unittest.main()
