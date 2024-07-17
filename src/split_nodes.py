import re

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(old_node)
            continue

        for anchor, url in links:
            parts = text.split(f"[{anchor}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(anchor, text_type_link, url))
            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, text_type_text))
            
    return new_nodes
        #print(new_nodes)


def extract_markdown_links(text):
    link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    return link_pattern.findall(text) 

def extract_markdown_image(text):
    image_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    return image_pattern.findall(text) 



def main():
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
    

if __name__ == "__main__":
    main()