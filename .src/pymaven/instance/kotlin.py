from util import *

'''
<properties>
  <kotlin.version>1.6.0</kotlin.version>
  <kotlin.compiler.incremental>true</kotlin.compiler.incremental>
</properties>
<dependencies>
  <dependency>
     <groupId>org.jetbrains.kotlin</groupId>
     <artifactId>kotlin-stdlib-jdk8</artifactId>
     <version>${kotlin.version}</version>
  </dependency>
</dependencies>
<build>
    <plugins>
     <plugin>
        <artifactId>kotlin-maven-plugin</artifactId>
        <groupId>org.jetbrains.kotlin</groupId>
        <version>${kotlin.version}</version>
        <executions>
           <execution>
              <id>compile</id>
              <goals>
                 <goal>compile</goal>
              </goals>
              <configuration>
                 <sourceDirs>
                    <sourceDir>${project.basedir}/src/main/kotlin</sourceDir>
                 </sourceDirs>
              </configuration>
           </execution>
           <execution>
              <id>test-compile</id>
              <goals>
                 <goal>test-compile</goal>
              </goals>
              <configuration>
                 <sourceDirs>
                    <sourceDir>${project.basedir}/src/test/kotlin</sourceDir>
                 </sourceDirs>
              </configuration>
           </execution>
        </executions>
     </plugin>
    </plugins>
</build>
'''

def kotlinPluginExecution(el, goal_name, path):
  children = [{'name': 'goal', 'value': goal_name, 'sib': False}]
  dict_array_tag = [
      {'name': 'execution', 'value': None, 'sib': False},
      {'name': 'id', 'value': goal_name, 'sib': True},
      {'name': 'goals', 'value': None, 'sib': True, 'children': children},
      {'name': 'configuration', 'value': None, 'sib': False},
      {'name': 'sourceDirs', 'value': None, 'sib': False},
      {'name': 'sourceDir', 'value': path, 'sib': False}
  ]
  buildEmbeddedElements(el, dict_array_tag)

def addKotlintDep(tree):
  # addPropertie(tree, {'name': "kotlin.version", 'value': "1.6.0"})
  # addPropertie(tree, {'name': "kotlin.compiler.incremental", 'value': "true"})
  deps = tree.findall(".//dependencies")[0]
  plugins = tree.findall(".//build/plugins")[0]
  dict_array_tag = [
      {'name': 'dependency', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'org.jetbrains.kotlin', 'sib': True},
      {'name': 'artifactId', 'value': 'kotlin-stdlib-jdk8', 'sib': True},
      {'name': 'version', 'value': '${kotlin.version}', 'sib': False}
  ]
  # buildEmbeddedElements(deps, dict_array_tag)
  dict_array_tag = [
      {'name': 'plugin', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'org.jetbrains.kotlin', 'sib': True},
      {'name': 'artifactId', 'value': 'kotlin-maven-plugin', 'sib': True},
      {'name': 'version', 'value': '${kotlin.version}', 'sib': True},
      {'name': 'executions', 'value': None, 'sib': False}
  ]
  execution = buildEmbeddedElements(plugins, dict_array_tag)
  kotlinPluginExecution(execution, 'compile', '${project.basedir}/src/main/kotlin')
  kotlinPluginExecution(execution, 'test-compile', '${project.basedir}/src/test/kotlin')