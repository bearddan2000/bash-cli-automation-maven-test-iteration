#!/usr/bin/python3.8

import re
import xml.dom.minidom as MD
import xml.etree.ElementTree as ET


def clean(xmlStr, header):
    xmlStr = re.sub('[\n|\t]', '', xmlStr)
    xmlStr = re.sub(' +', ' ', xmlStr)
    xmlStr = re.sub('> <', '><', xmlStr)
    xmlStr = re.sub(header, '<root>', xmlStr)
    xmlStr = re.sub('<\?xml*>', '', xmlStr)
    return re.sub('</project>', '</root>', xmlStr)


def redoDir(lst, idx, repl):
    del lst[idx]
    lst.insert(idx, repl)


def addElem(tree, arr):
    root = tree.findall(".//dependencies")[0]
    dependency = ET.SubElement(root, 'dependency')
    groupId = ET.SubElement(dependency, 'groupId')
    artifactId = ET.SubElement(dependency, 'artifactId')

    if len(arr) == 3:
        version = ET.SubElement(dependency, 'version')
        version.text = arr[-1]

    groupId.text = arr[0]
    artifactId.text = arr[1]


def delElem(tree, artifactLst, xpath=".//dependencies"):
    child_index = 0
    root = tree.findall(xpath)[0]
    for tmp in root:
        for child in tmp.findall(".//artifactId"):
            if child.text == artifactLst[0]:
                del root[child_index]
        child_index += 1

def delElementRecurcive(tree, node):
    for el in node:
        delElementRecurcive(tree, el)
        tree.remove(el)

    tree.remove(node)

def delElemExpirement(tree, artifactLst, xpath=".//dependencies"):
    path = xpath + "/[artifactId='" + artifactLst[0] + "']"
    for tmp in tree.findall(path):
        delElementRecurcive(tree, tmp)
    root = tree.findall(path)
    print(f'array len: {len(root)}')

def delProperty(tree, propLst):
    child_index = 0
    root = tree.findall(".//properties")[0]
    for tmp in root:
        if tmp.tag in propLst:
            del root[child_index]
        child_index += 1


# function to get unique values
def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def addPropertie(tree, dict_tag):
    '''
    Adds maven variables
    :param tree: the document root
    :param dict_tag: dictionary of tag attributes
    :return: None
    '''
    props = tree.findall(".//properties")[0]
    prop = ET.SubElement(props, dict_tag['name'])
    prop.text = dict_tag['value']


def buildEmbeddedElements(parent, dict_array_tag):
    el = ET.SubElement(parent, dict_array_tag[0]['name'])
    if dict_array_tag[0]['value']:
        el.text = dict_array_tag[0]['value']

    if 'children' in dict_array_tag[0]:
        buildEmbeddedElements(el, dict_array_tag[0]['children'])

    if dict_array_tag[0]['sib']:
        dict_array_tag.pop(0)
        if dict_array_tag:
            return buildEmbeddedElements(parent, dict_array_tag)
    else:
        dict_array_tag.pop(0)
        if dict_array_tag:
            return buildEmbeddedElements(el, dict_array_tag)

    return el
