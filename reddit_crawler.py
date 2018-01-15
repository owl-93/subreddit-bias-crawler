import requests
import json
from input import Input
import sys

#get parse program parameters from user input
input = Input()
persons, keywords = input.resolveInput(sys.argv)

print(persons)
print(keywords)

