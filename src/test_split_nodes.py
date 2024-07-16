import unittest
from split_nodes import split_nodes_delimiter, extract_markdown_image, extract_markdown_links

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

class TestMarkDownImage(unittest.TestCase):
    def test_extract_markdown_images(self):
        self.assertEqual(extract_markdown_image("No images here"), [])
        self.assertEqual(extract_markdown_image("![alt text](https://example.com/image.jpg)"), [("alt text", "https://example.com/image.jpg")])
        self.assertEqual(extract_markdown_image("This is ![image1](https://example.com/1.jpg) and ![image2](https://example.com/2.jpg)"), [
            ("image1", "https://example.com/1.jpg"),
            ("image2", "https://example.com/2.jpg")
        ])
        self.assertEqual(extract_markdown_image("![special characters](https://example.com/image-1_2.jpg)"), [("special characters", "https://example.com/image-1_2.jpg")])

    def test_extract_markdown_links(self):
        self.assertEqual(extract_markdown_links("No links here"), [])
        self.assertEqual(extract_markdown_links("[special characters](https://example.com/link-1_2)"), [("special characters", "https://example.com/link-1_2")])
        self.assertEqual(extract_markdown_links("[anchor text](https://example.com)"), [("anchor text", "https://example.com")])

if __name__ == "__main__":
    unittest.main()