'''
    <properties>
      <cucumber.bom.version>7.0.0</cucumber.bom.version>
    </properties>

  <dependency>
     <groupId>io.cucumber</groupId>
     <artifactId>cucumber-java</artifactId>
     <scope>test</scope>
  </dependency>

   <dependencyManagement>
      <dependencies>
         <dependency>
            <groupId>io.cucumber</groupId>
            <artifactId>cucumber-bom</artifactId>
            <version>${cucumber.bom.version}</version>
            <type>pom</type>
            <scope>import</scope>
         </dependency>
      </dependencies>
   </dependencyManagement>

    <build>
        <plugins>
         <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version>
            <configuration>
               <properties>
                  <configurationParameters> cucumber.plugin=pretty,html:target/site/cucumber-pretty.html cucumber.publish.quiet=true cucumber.publish.enabled=false </configurationParameters>
               </properties>
            </configuration>
         </plugin>
        </plugins>
    </build>
'''
from util import *

def addCucumberJunitDep(tree):
    '''
   <dependencies>
      <dependency>
         <groupId>io.cucumber</groupId>
         <artifactId>cucumber-junit-platform-engine</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>
    '''
    groupId = 'io.cucumber'
    addPropertie(tree, {'name': "cucumber.bom.version", 'value': "7.0.0"})
    deps = tree.findall(".//dependencies")[0]
    plugin = tree.findall(".//build/plugins")[0]
    mgmn = tree.findall(".//dependencyManagement/dependencies")[0]
    dict_array_tag = [
        {'name': 'dependency', 'value': None, 'sib': False},
        {'name': 'groupId', 'value': groupId, 'sib': True},
        {'name': 'artifactId', 'value': 'cucumber-bom', 'sib': True},
        {'name': 'version', 'value': '${cucumber.bom.version}', 'sib': True},
        {'name': 'type', 'value': 'pom', 'sib': True},
        {'name': 'scope', 'value': 'import', 'sib': False}
    ]
    buildEmbeddedElements(mgmn, dict_array_tag)
    dict_array_tag = [
        {'name': 'dependency', 'value': None, 'sib': False},
        {'name': 'groupId', 'value': groupId, 'sib': True},
        {'name': 'artifactId', 'value': 'cucumber-java', 'sib': False}
    ]
    buildEmbeddedElements(deps, dict_array_tag)
    dict_array_tag = [
        {'name': 'dependency', 'value': None, 'sib': False},
        {'name': 'groupId', 'value': groupId, 'sib': True},
        {'name': 'artifactId', 'value': 'cucumber-junit-platform-engine', 'sib': False}
    ]
    buildEmbeddedElements(deps, dict_array_tag)
    delElem(tree, ["maven-surefire-plugin"], ".//build/plugins")
    dict_array_tag = [
        {'name': 'plugin', 'value': None, 'sib': False},
        {'name': 'groupId', 'value': 'org.apache.maven.plugins', 'sib': True},
        {'name': 'artifactId', 'value': 'maven-surefire-plugin', 'sib': True},
        {'name': 'version', 'value': '3.0.0-M5', 'sib': True},
        {'name': 'configuration', 'value': None, 'sib': False},
        {'name': 'properties', 'value': None, 'sib': False},
        {'name': 'configurationParameters', 'value': 'cucumber.plugin=pretty,html:target/site/cucumber-pretty.html cucumber.publish.quiet=true cucumber.publish.enabled=false', 'sib': False}
    ]
    buildEmbeddedElements(plugin, dict_array_tag)