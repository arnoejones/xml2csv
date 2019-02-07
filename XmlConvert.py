import xml.etree.ElementTree as et
import re

tree = et.parse('test1arno.xml')
root = tree.getroot()

# print('Item #2 attribute:')
# print(root[0][1].attrib)
#
# print('\nAll attributes:')
# for elem in root:
#     for subelem in elem:
#         print(subelem.attrib)

# print('\nItem #2 data:')
# print(root[0][1].text)

print('\nAll item data:')

all_elems_list = [elem.tag for elem in root.iter()]
pattern = re.compile(r'\n\s+')

list_of_elem_dicts = []

for elem in root:
    # if not pattern.findall(elem.text):
    print('-', elem.tag)
    print('-', elem.text)
    list_of_elem_dicts.append({elem.tag:elem.text})
    for subelem in elem:
        # if not pattern.findall(subelem.text):
        print('*', subelem.tag)
        print('*', subelem.text)
        list_of_elem_dicts.append({subelem.tag: subelem.text})
        for sub2elem in subelem:
            # if not pattern.findall(sub2elem.text):
            print('**', sub2elem.tag)
            print('**', sub2elem.text)
            list_of_elem_dicts.append({sub2elem.tag: sub2elem.text})
            for sub3elem in sub2elem:
                # if not pattern.findall(sub3elem.text):
                print('***', sub3elem.tag)
                print('***', sub3elem.text)
                list_of_elem_dicts.append({sub3elem.tag: sub3elem.text})
                for sub4elem in sub3elem:
                    # if not pattern.findall(sub4elem.text):
                    print('****', sub4elem.tag)
                    print('****', sub4elem.text)
                    list_of_elem_dicts.append({sub4elem.tag: sub4elem.text})
                    for sub5elem in sub4elem:
                        # if not pattern.findall(sub3elem.text):
                        print('*****', sub5elem.tag)
                        print('*****', sub5elem.text)
                        list_of_elem_dicts.append({sub5elem.tag: sub5elem.text})
print(all_elems_list)
# for elem in(all_elems_list):
#     print(elem)
#
# head = all_elems_list

# for configItem in root.findall('ConfigurationItems'):
#     row = []
#     name_name = configItem.find('Name').text
#     row.append(name_name)
#     type_name = configItem.find('Type').text
#     row.append(type_name)
#
# print('*****',row)
# print(et.tostring(root, encoding='utf8').decode('utf8'))
