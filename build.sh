#! /bin/bash

function replace_dockerfile_str() {
  #statements
  local file=$1/install.sh
  local old=$2
  local new=$3

  perl -pi.bak -e "s/${old}/${new}/" $file
  rm -f $1/install.sh.bak
}

d=$1

# replace_dockerfile_str $d "adoptopenjdk/maven-openjdk11", "maven:3-openjdk-17"

./.src/pymaven/pom.py $d/bin/pom.xml
