from util import *
'''
<properties>
    <scala.version>2.12.7</scala.version>
    <scala.compat.version>2.12</scala.compat.version>
</properties>
<dependencies>
    <dependency>
       <groupId>org.scala-lang</groupId>
       <artifactId>scala-library</artifactId>
       <version>${scala.version}</version>
    </dependency>
    <dependency>
       <groupId>org.scala-lang.modules</groupId>
       <artifactId>scala-xml_${scala.compat.version}</artifactId>
       <version>1.1.1</version>
    </dependency>
    <dependency>
       <groupId>org.scala-lang.modules</groupId>
       <artifactId>scala-parser-combinators_${scala.compat.version}</artifactId>
       <version>1.1.1</version>
    </dependency>
</dependencies>
<build>
    <plugins>
         <plugin>
            <groupId>net.alchim31.maven</groupId>
            <artifactId>scala-maven-plugin</artifactId>
            <version>3.4.4</version>
            <executions>
               <execution>
                  <goals>
                     <goal>compile</goal>
                  </goals>
               </execution>
            </executions>
            <configuration>
               <launchers>
                  <launcher>
                     <id>foo</id>
                     <mainClass>example.Main</mainClass>
                  </launcher>
               </launchers>
            </configuration>
         </plugin>
    </plugins>
</build>
'''

def cleanScala(tree):
    delProperty(tree, ["kotlin.version"])
    delProperty(tree, ["kotlin.compiler.incremental"])
    delElem(tree, ["kotlin-stdlib-jdk8"])

def addScalaDep(tree, main_class = 'example.Main'):
    '''
    <scala.version>2.12.7</scala.version>
    <scala.compat.version>2.12</scala.compat.version>
    '''
    addPropertie(tree, {'name': "scala.version", 'value': "2.12.7"})
    addPropertie(tree, {'name': "scala.compat.version", 'value': "2.12"})
    '''
    <dependency>
       <groupId>org.scala-lang</groupId>
       <artifactId>scala-library</artifactId>
       <version>${scala.version}</version>
    </dependency>
    <dependency>
       <groupId>org.scala-lang.modules</groupId>
       <artifactId>scala-xml_${scala.compat.version}</artifactId>
       <version>1.1.1</version>
    </dependency>
    <dependency>
       <groupId>org.scala-lang.modules</groupId>
       <artifactId>scala-parser-combinators_${scala.compat.version}</artifactId>
       <version>1.1.1</version>
    </dependency>
    '''
    deps = tree.findall(".//dependencies")[0]
    dict_array_tag = [
      {'name': 'dependency', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'org.scala-lang', 'sib': True},
      {'name': 'artifactId', 'value': 'scala-library', 'sib': True},
      {'name': 'version', 'value': '${scala.version}', 'sib': False}
    ]
    buildEmbeddedElements(deps, dict_array_tag)
    dict_array_tag = [
      {'name': 'dependency', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'org.scala-lang.modules', 'sib': True},
      {'name': 'artifactId', 'value': 'scala-xml_${scala.compat.version}', 'sib': True},
      {'name': 'version', 'value': '1.1.1', 'sib': False}
    ]
    buildEmbeddedElements(deps, dict_array_tag)
    dict_array_tag = [
      {'name': 'dependency', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'org.scala-lang.modules', 'sib': True},
      {'name': 'artifactId', 'value': 'scala-parser-combinators_${scala.compat.version}', 'sib': True},
      {'name': 'version', 'value': '1.1.1', 'sib': False}
    ]
    buildEmbeddedElements(deps, dict_array_tag)
    plugins = tree.findall(".//build/plugins")[0]
    execution_children = [
      {'name': 'execution', 'value': None, 'sib': False},
      {'name': 'goals', 'value': None, 'sib': False},
      {'name': 'goal', 'value': 'compile', 'sib': False}
    ]
    configuration_children = [
      {'name': 'launchers', 'value': None, 'sib': False},
      {'name': 'launcher', 'value': None, 'sib': False},
      {'name': 'id', 'value': 'foo', 'sib': True},
      {'name': 'mainClass', 'value': main_class, 'sib': False}
    ]
    dict_array_tag = [
      {'name': 'plugin', 'value': None, 'sib': False},
      {'name': 'groupId', 'value': 'net.alchim31.maven', 'sib': True},
      {'name': 'artifactId', 'value': 'scala-maven-plugin', 'sib': True},
      {'name': 'version', 'value': '3.4.4', 'sib': True},
      {'name': 'executions', 'value': None, 'sib': True, 'children': execution_children},
      {'name': 'configuration', 'value': None, 'sib': False, 'children': configuration_children}
    ]
    buildEmbeddedElements(plugins, dict_array_tag)