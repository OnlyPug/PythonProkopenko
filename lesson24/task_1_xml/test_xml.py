def test_xml_to_srt(xmlfile):
    result = xmlfile.xml_to_string()
    print(result)


def test_add_to_xml(xmlfile):
    xmlfile.add_custom_tag('breakfast_menu', 'food', {}, None)
    xmlfile.add_custom_tag('food', 'name', {}, 'Xml Pancakes')
    xmlfile.add_custom_tag('food', 'price', {}, 'Just work')
    result = xmlfile.xml_to_string()
    print(result)


def test_add_new_teg_food_with_atrributes(xmlfile):
    food_item_data = {
        'name': 'Vegan Pancakes',
        'price': '$5.50',
        'description': 'Delicious vegan pancakes with blueberries',
        'calories': '500'
    }
    xmlfile.add_food_item(food_item_data)
    result = xmlfile.xml_to_string()
    print(result)


def test_replace_to_srt_with_tag(xmlfile):
    xmlfile.replace_price_tag(old_tag='<price>$4.50</price>', new_tag='<price>$1.99</price>')


def test_delete_tag(xmlfile):
    xmlfile.remove_custom_tag('description')
    result = xmlfile.xml_to_string()
    print(result)


def test_get_element_by_name(xmlfile):
    find_teg = xmlfile.get_elements_by_tag('calories')
    print(find_teg)
