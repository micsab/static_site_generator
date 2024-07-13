import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "http://www.espn.com")
        node2 = TextNode("This is a text node", "bold", "http://www.espn.com")
        node3 = TextNode("Yadda Yadda", "Italics", "aol.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_missing_params(self):
        with self.assertRaises(TypeError):
            TextNode("This is some text", "Bold")
        with self.assertRaises(TypeError):
            TextNode("This is some text")
        with self.assertRaises(TypeError):
            TextNode()

    def test_blank_params(self):
        blank = TextNode('','', '')
        self.assertEqual(blank.text, '', "Parameter text should be blank")
        self.assertEqual(blank.text_type, '', "Parameter text_type should be blank")
        self.assertEqual(blank.url, '', "Parameter url should be blank")

    def test_none_params(self):
        none1 = TextNode('test', 'bold', None)
        none2 = TextNode('test', None, 'www.espn.com')
        none3 = TextNode(None, 'bold', 'www.espn.com')
        self.assertIsNone(none1.url, "Parameter url should be None")
        self.assertIsNone(none2.text_type, "Parameter text_type should be None")
        self.assertIsNone(none3.text, "Parameter text should be None")

if __name__ == "__main__":
    unittest.main()
