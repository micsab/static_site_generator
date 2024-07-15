import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "http://www.espn.com")
        node2 = TextNode("This is a text node", "bold", "http://www.espn.com")
        node3 = TextNode("Yadda Yadda", "Italics", "aol.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_missing_params(self):
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

class TestTextNodeToHTMLNODE(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
