import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_init_defaul_values(self):
        leaf = LeafNode(value="hello")
        self.assertIsNone(leaf.tag)
        self.assertIsNone(leaf.props)
        self.assertIsNone(leaf.children)
        self.assertEqual(leaf.value, "hello")

    def test_missing_param(self):
        with self.assertRaises(ValueError):
            LeafNode()

    def test_with_tag(self):
        leaf = LeafNode(tag="span", value="hello", props={"class": "test"})
        expected_html = '<span class="test">hello</span>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_no_tag(self):
        leaf = LeafNode(value="hello")
        expected_html = 'hello'
        self.assertEqual(leaf.to_html(), expected_html)

class TestParentNode(unittest.TestCase):
    def test_valid_params(self):
        parent = ParentNode(
            tag='div',
            children=[LeafNode(tag='span', value='child')]
        )
        self.assertEqual(parent.tag, 'div')
        self.assertEqual(len(parent.children), 1)
        self.assertIsNone(parent.value)
    
    def test_creation_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(
                children=[LeafNode(tag="span",value="Child")]
            )

    def test_creation_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag='div', children=[])

    def test_html_render_with_children(self):
        parent = ParentNode(
            tag='p',
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(value="Normal text"),
            ]
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_html_render_with_props(self):
        parent = ParentNode(
            tag='div',
            children=[LeafNode(tag='span',value='child')],
            props={"class": "container"}
        )
        expected_html = '<div class="container"><span>child</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
