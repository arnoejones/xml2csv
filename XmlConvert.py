import xml.etree.ElementTree as et
import re
import pandas as pd
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
config_item_count = 0

list_of_elem_dicts = [[]]
for i in range(228):
    list_of_elem_dicts.append([])

for elem in root:
    # if not pattern.findall(elem.text):
# want a new list everytime I come here
    config_item_count += 1
    print('-', elem.tag)
    print('-', elem.text)
    list_of_elem_dicts[config_item_count].append({elem.tag:elem.text})
    for subelem in elem:
        # if not pattern.findall(subelem.text):
        print('*', subelem.tag)
        print('*', subelem.text)
        list_of_elem_dicts[config_item_count].append({subelem.tag: subelem.text})
        for sub2elem in subelem:
            # if not pattern.findall(sub2elem.text):
            print('**', sub2elem.tag)
            print('**', sub2elem.text)
            list_of_elem_dicts[config_item_count].append({sub2elem.tag: sub2elem.text})
            for sub3elem in sub2elem:
                # if not pattern.findall(sub3elem.text):
                print('***', sub3elem.tag)
                print('***', sub3elem.text)
                list_of_elem_dicts[config_item_count].append({sub3elem.tag: sub3elem.text})
                for sub4elem in sub3elem:
                    # if not pattern.findall(sub4elem.text):
                    print('****', sub4elem.tag)
                    print('****', sub4elem.text)
                    list_of_elem_dicts[config_item_count].append({sub4elem.tag: sub4elem.text})
                    # for sub5elem in sub4elem:
                    #     # if not pattern.findall(sub3elem.text):
                    #     print('*****', sub5elem.tag)
                    #     print('*****', sub5elem.text)
                    #     list_of_elem_dicts[config_item_count].append({sub5elem.tag: sub5elem.text})

df = pd.DataFrame(list_of_elem_dicts)
df.to_csv('exportedconfig.csv')
# print(all_elems_list)
print("Dataframe exported.")
# written to .csv, done
# now, try to convert back to xml
df1 = pd.read_csv('exportedconfig.csv')





print("I'm here")

def to_xml(df, filename=None, mode='w'):
    def row_to_xml(row):
        xml = ['<item>']
        for i, col_name in enumerate(row.index):
            xml.append('  <field name="{0}">{1}</field>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)
    res = '\n'.join(df.apply(row_to_xml, axis=1))

    if filename is None:
        return res
    with open(filename, mode) as f:
        f.write(res)

pd.DataFrame.to_xml = to_xml
print("what's next?")
