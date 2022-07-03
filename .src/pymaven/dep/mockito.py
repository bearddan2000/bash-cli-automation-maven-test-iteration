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

def addMockJunitDep(tree):
    groupId = 'org.mockito'
    addElem(tree, [groupId, 'mockito-core', '4.4.0'])
    addElem(tree, [groupId, 'mockito-junit-jupiter', '2.23.0'])

def addMockTestngDep(tree):
    addElem(tree, ['org.mockito', 'mockito-all', '1.9.5'])
    root = tree.findall(".//name")[0]
    root.text += "-Mockito"