from xml.etree import ElementTree

"""Опишіть клас, який оброблятиме xml/ зробіть йому п'ять методів, один хай переганяє xml в строку, один декодує
строку назад в xml, один додає кастомний тег, один видаляє кастомний тег, один дістає елементи з параметрами за
прикладом як ми зробили на занятті. В якості хмл файлу скористайтесь або прикріпленим файлом, або будь-яким з
просторів інтернету, не менший за прикріплений"""


class XMLwork:
    def __init__(self, name_file):
        self.tree = ElementTree.parse(name_file)
        self.root = self.tree.getroot()

    def xml_to_string(self):
        return ElementTree.tostring(self.root).decode()

    def string_to_xml(self, xml_string):
        return ElementTree.fromstring(xml_string)

    def add_custom_tag(self, parent_tag, tag_name, attributes, text=None):
        parent_elements = self.root.findall(parent_tag)
        if parent_elements:
            parent = parent_elements[-1]
            new_element = ElementTree.SubElement(parent, tag_name)
            for key, value in attributes.items():
                new_element.set(key, value)
            if text:
                new_element.text = text

    def add_food_item(self, food_data):
        food = ElementTree.SubElement(self.root, 'food')
        for tag, text in food_data.items():
            child = ElementTree.SubElement(food, tag)
            child.text = text

    def replace_price_tag(self, old_tag=None, new_tag=None):
        change = self.xml_to_string().replace(old_tag, new_tag)
        encoder_result = self.string_to_xml(change)
        food = encoder_result[3]
        for parametrs in food:
            if parametrs.tag == 'price':
                return print(f'New text inside teg: {parametrs.text}')

    def remove_custom_tag(self, tag_name):
        for parent in self.root.findall(".//"):
            for child in parent.findall(tag_name):
                parent.remove(child)

    def get_elements_by_tag(self, tag_name):
        found_elements = self.root.findall(f'.//{tag_name}')
        return [ElementTree.tostring(element) for element in found_elements]
