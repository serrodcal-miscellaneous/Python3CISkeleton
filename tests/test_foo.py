from unittest import TestCase
from Python3CISkeleton.foo import Foo

class TestGenome(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.foo = Foo()

    def test_get_mutations(self):
        self.foo.print_foo()
        self.assertEqual(self.foo.foo, "foo")

if __name__ == '__main__':
    unittest.main()
