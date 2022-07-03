#! /bin/bash

function replace_readme_str() {
  #statements
  local file=$1/README.md
  local old=$2
  local new=$3

  perl -pi.bak -e "s/${old}/${new}/" $file
  rm -f $1/README.md.bak
}

function replace_readme_first() {
  #statements
  local file=$1/README.md
  local old=$2
  local new=$3

  perl -pi.bak -0 -e "s/${old}/${new}/" $file
  rm -f $1/README.md.bak
}

d=$1

# replace_readme_str $d "testng" "junit5"

replace_readme_first $d "junit5" "junit"

replace_readme_str $d "car-data" "hello-world"

replace_readme_str $d "-cucumber" ""

replace_readme_str $d "\t- cucumber\n" ""

replace_readme_str $d ", and cucumber" ""

replace_readme_str $d "-spring" ""

replace_readme_str $d "\t- spring\n" ""
