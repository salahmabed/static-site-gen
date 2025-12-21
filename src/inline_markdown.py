from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    link_list = re.findall(r'!\[.*?\]\(.*?\)', text)
    tuple_list = []
    for link in link_list:
        last_alt_index = link.rindex("]")
        alt_text = link[2:last_alt_index]
        first_url_index = link.rindex("(")+1
        url = link[first_url_index:-1]
        tuple_list.append((alt_text,url))
    return tuple_list


def extract_markdown_links(text):
    link_list = re.findall(r'(?<!!)\[.*?\]\(.*?\)', text)
    tuple_list = []
    for link in link_list:
        last_alt_index = link.rindex("]")
        alt_text = link[1:last_alt_index]
        first_url_index = link.rindex("(")+1
        url = link[first_url_index:-1]
        tuple_list.append((alt_text,url))
    return tuple_list