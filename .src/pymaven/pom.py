#!/usr/bin/python3.8

from util import *
# from instance.kotlin import addKotlintDep
# from project import *
# from instance.scala import *
import sys
import xml.dom.minidom as MD
import xml.etree.ElementTree as ET

def main():

    tree = None
    header="""<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">"""

    with open(sys.argv[1], encoding='utf-8') as f:
        xmlStr = f.readlines()
        redoDir(xmlStr, 0, """<?xml version="1.0" ?>""")
        redoDir(xmlStr, 1, header)
        xmlStr = clean("".join(xmlStr), header)
        tree = ET.fromstring(xmlStr)
        delElem(tree, ['spring-test'])
        delElem(tree, ['spring-context'])
        delElem(tree, ['serenity-cucumber'])

    xmlstr = MD.parseString(ET.tostring(tree)).toprettyxml(indent="   ")
    with open(sys.argv[1], "w") as f:
        xmlstr = xmlstr.replace('<root>', header).replace('</root>', '</project>')
        f.write(xmlstr)

if __name__ == '__main__':
    main()
