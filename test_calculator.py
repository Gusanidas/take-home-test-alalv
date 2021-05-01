import calculator
import unittest


class TestCalculator(unittest.TestCase):
    """
    Test the calculator module
    """

    def test_correct_prefix_expr(self):
        """
        Test that well formated prefix expressions return the correct output
        """
        expressions = {
            "+ 11 2": 13,
            "* * 2 2 2": 8,
            "/ 15 * 3 1": 5,
            "- + - 3 1 / 9 3 * 2 1": 3}
        for expr, value in expressions.items():
            result = calculator.eval_prefix_expr(expr)
            self.assertEqual(result, value)

    def test_incorrect_prefix_expr(self):
        """
        Test that badly formated prefix expressions raise ValueError
        """
        expressions = [
            "+ 1  2",
            "+ 1 2 3",
            "* * 2 2 -",
            "/ 6 * 3  -1",
            "( ( 2 * 2 ) * 2 )"]
        
        for expr in expressions:
            self.assertRaises(ValueError, calculator.eval_prefix_expr, expr)

    def test_correct_infix(self):
        """
        Test that well formated infix expressions return the correct output
        """
        expressions = {
            "( 11 + 2 )": 13,
            "( ( 2 * 2 ) * 2 )": 8,
            "( 36 / ( 3 * 1 ) )": 12,
            "( ( ( 3 - 1 ) + ( 9 / 3 ) ) - ( 2 * 1 ) )": 3}
        
        for expr, value in expressions.items():
            result = calculator.eval_infix_expr(expr)
            self.assertEqual(result, value)

    def test_incorrect_infix_expr(self):
        """
        Test that badly formated infix expressions raise ValueError
        """
        expressions = [
            "( 1 + 2)",
            "( ( 2 * 2 ) * 2 - 1 )",
            "( 6 / ( 3 * 1)",
            "( ( ( 3 - 1 ) + ( 9 / 3 ) ) - ( -2 * 1 ) )"]
        
        for expr in expressions:
            self.assertRaises(ValueError, calculator.eval_infix_expr, expr)


if __name__ == '__main__':
    unittest.main()