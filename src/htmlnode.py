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
    

def main():
    proppy = {
        "href": "https://www.google.com", 
        "target": "_blank",
    }

    html_node = HTMLNODE('p','yadda yadda',None, proppy)
    print(html_node)

if __name__ == "__main__":
    main()


