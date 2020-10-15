import unittest
import primes as pr

# Prime numbers list http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

class TestPrimesMethods(unittest.TestCase):

    def test_primes1(self):
        self.assertEqual(pr.is_prime1(131), True)

    def test_primes2(self):
        self.assertEqual(pr.is_prime2(131), True)

    def test_primes3(self):
        self.assertEqual(pr.is_prime3(131), True)

    def test_primes4(self):
        self.assertEqual(pr.is_prime4(131), True)

    def test_primes5(self):
        self.assertEqual(pr.is_prime5(131), True)

    def test_primes6(self):
        self.assertEqual(pr.is_prime6(131), True)

    def test_primes7(self):
        self.assertEqual(pr.is_prime7(131), True)

    def test_primes8(self):
        self.assertEqual(pr.is_prime8(131), True)

    def test_primes9(self):
        self.assertEqual(pr.is_prime9(131), True)

    def test_primes10(self):
        self.assertEqual(pr.is_prime10(131), True)

    def test_primes11(self):
        self.assertEqual(pr.is_prime11(131), True)

    def test_primes12(self):
        self.assertEqual(pr.is_prime12(131), True)


if __name__ == '__main__':
    unittest.main()