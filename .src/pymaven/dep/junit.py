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

def addJunitDep(tree):
    root = tree.findall(".//properties")[0]
    abbr = ET.SubElement(root,'junit.bom.version')
    abbr.text = '5.8.1'

    root = tree.findall('./')[7]
    mgmnt = ET.SubElement(root, 'dependencyManagement')
    deps = ET.SubElement(mgmnt, 'dependencies')
    dep = ET.SubElement(deps, 'dependency')
    ET.SubElement(dep, 'groupId').text = 'org.junit'
    ET.SubElement(dep, 'artifactId').text = 'junit-bom'
    ET.SubElement(dep, 'version').text = '${junit.bom.version}'
    ET.SubElement(dep, 'type').text = 'pom'
    ET.SubElement(dep, 'scope').text = 'import'

    addElem(tree, ['org.junit.platform', 'junit-platform-suite'])
    addElem(tree, ['org.junit.jupiter', 'junit-jupiter'])