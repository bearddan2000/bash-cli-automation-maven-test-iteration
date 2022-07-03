from util import *
import xml.dom.minidom as MD
import xml.etree.ElementTree as ET

def fixProjectTitle(tree):
    root = tree.findall(".//name")[0]
    title = unique(root.text.split('-'))

    for x in title:
        if 'JBehave' in x:
            x = 'Cucumber'

    root.text = '-'.join(title)

    root = tree.findall(".//artifactId")[0]
    root.text.replace('jbehave', 'cucumber')

    lst = tree.findall(".//properties/spring.version")
    if 1 < len(lst):
        del lst[-1]

def fixMavenCompile(tree):
    root = tree.findall(".//build/plugins/plugin")[0]
    config = root.findall(".//configuration")[0]
    source = config.findall(".//source")[0]
    target = config.findall(".//target")[0]
    version = '1.8'
    source.text = version
    target.text = version