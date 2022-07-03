# bash-cli-automation-maven-test-iteration

## Description
An automated solution for iterating
maven test projects.

The idea is to model projects with a
single code base located here: `.src`.
Although the current code is java; groovy,
kotlin, or scala can be used.

A python lib is used to alter the maven
xml.

## Tech stack
- bash
- python
  - etree

## Known issue
Etree doesn't delete xml nodes well. I wrote
a small function `delElement` in `.src/pymaven/util.py`
that deletes upto one depth.

## To run
`sudo ./install.sh -u`

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
