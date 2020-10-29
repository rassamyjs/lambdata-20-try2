""" 
Basic unit test for lambdata package
"""

import unittest
from example_module import COLORS, increment
from oop_example import SocialMediaUser

class SocialMediaUserTests(unittest.TestCase):
    """
    Tests for the usage of Social Media Users in our Social Media Class
    """
    def setUp(self): 
        self.user1 = SocialMediaUser(name="Jimmy", location="France")
        self.user2 = SocialMediaUser(name="Craig", location="Kenya")

    def test_name(self):
        """
        Testing the name attribute
        """
        self.assertEqual(self.user1.name, "Jimmy")
        self.assertEqual(self.user2.name, "Craig")

    def test_location(self):
        """
        Testing the location attribute
        """
        self.assertEqual(self.user1.location, "France")
        self.assertEqual(self.user2.location, "Kenya")






class ExampleTests(unittest.TestCase):
    """
    Making sure examples work as expected
    """
    def test_increment(self):
        """
        Testing that increment adds one to a number
        """
        
        x0 = 0
        y0 = increment(x0) # this should return the value plus 1
        self.assertEqual(y0, 1)
        
        
        x1 = 100
        y1 = increment(x1)
        self.assertEqual(y1, 101)

        x2 = -1
        y2 = increment(x2)
        self.assertEqual(y2, 0)

        x3 = -1.5
        y3 = increment(x3)
        self.assertEqual(y3, -0.5)



#  COLORS = ['cyan', 'teal', 'mauve', 'blue', 'crimson']
    
    def test_colors(self):
        """
        Testing the presence/absense of members in the color list
        """
        self.assertIn("crimson", COLORS)
        self.assertNotIn('brown', COLORS)


    def test_number_colors(self):
        """
        Testing that we have the expected number of colors
        """
        self.assertEqual(len(COLORS), 5)


if __name__ == "__main__":
    unittest.main()



