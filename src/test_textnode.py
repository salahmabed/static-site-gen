import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a","text inside a paragraph", None, {"href": "https://www.google.com"})
        node2 = HTMLNode()
        node3 = HTMLNode("p","more text inside a paragraph")
        print(node1)
        print(node2)
        print(node3)

if __name__ == "__main__":
    unittest.main()