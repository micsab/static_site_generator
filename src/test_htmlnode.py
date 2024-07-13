import unittest

from htmlnode import HTMLNODE

class TestHTMLNode(unittest.TestCase):
    def test_init_default_values(self):
        node = HTMLNODE()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    
    def test_init_with_values(self):
        node = HTMLNODE("div", "Hello", [HTMLNODE("p", "world")], {"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertIsInstance(node.children[0], HTMLNODE)
        self.assertEqual(node.props, {"class": "greeting"})

    def test_props_to_html(self):
        node = HTMLNODE(props={"class": "test", "id": "my_id"})
        self.assertIn('class="test"', node.props_to_html())
        self.assertIn('id="my_id"', node.props_to_html())

    def test_repr(self):
        node = HTMLNODE("div", "hello", None, {"class": "greeting"})
        expected = "HTMLNode(div, hello, None, {'class': 'greeting'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
