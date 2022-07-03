'''
<properties>
    <spring.version>5.0.1.RELEASE</spring.version>
</properties>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>${spring.version}</version>
</dependency>
'''
from util import *
import xml.etree.ElementTree as ET

def addSpringDep(tree):
    groupId = 'org.springframework'
    version = '${spring.version}'
    addElem(tree, [groupId, 'spring-test', version])
    addElem(tree, [groupId, 'spring-context', version])
    root = tree.findall(".//properties")[0]
    abbr = ET.SubElement(root,'spring.version')
    abbr.text = '5.0.1.RELEASE'
    root = tree.findall(".//name")[0]
    root.text = "Spring-" + root.text
