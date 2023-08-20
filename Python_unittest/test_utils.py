import utils
import unittest


class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))
        self.assertEqual(utils.is_prime(-3), "Negative numbers are not allowed")

    def test_cubic(self):
        self.assertEqual(utils.cubic(2), 8)
        self.assertEqual(utils.cubic(-2), -8)
        self.assertNotEqual(utils.cubic(2), 4)
        self.assertNotEqual(utils.cubic(-3), 27)

    def test_say_hello(self):
        self.assertEqual(utils.say_hello("Oscar"), "Hello Oscar")
        self.assertEqual(utils.say_hello("Danya"), "Hello Danya")
        self.assertNotEqual(utils.say_hello("Gael"), "Hi Gael")
        self.assertNotEqual(utils.say_hello("Abril"), "Hi Abril")
        self.assertEqual(utils.say_hello("Arantxa Mayte"), "Hello Arantxa Mayte")


if __name__ == '__name__':
    unittest.main()
