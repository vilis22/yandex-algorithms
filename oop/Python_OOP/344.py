from xml.etree import ElementTree


class Decor:
    def __init__(self, param=None):
        self.param = param

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if self.param is None:
                return result

            return [elem for elem in result if elem.tag == self.param]

        return wrapper


class XmlParser:
    def parse(self, path="data.xml"):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        return list(root.iter())


xml_parse = XmlParser()
print(*(i.tag for i in xml_parse.parse()))
