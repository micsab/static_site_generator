class HTMLNODE():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes must have a value")
        
        props_str = self.props_to_html()
        if props_str:
            props_str = " " + props_str

        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNODE):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None or not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        props_str = self.props_to_html()
        if props_str:
            props_str = " " + props_str

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

    

def main():
    proppy = {
        "href": "https://www.google.com", 
        "target": "_blank",
    }

    html_node = HTMLNODE('p','yadda yadda',None, proppy)
    print(html_node)

if __name__ == "__main__":
    main()


