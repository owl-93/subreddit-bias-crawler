import requests
from post import Post
from input import Input
import sys
import praw
import pprint

filter = ["the",
          "of",
          "not",
          "as",
          "and",
          "a",
          "then",
          "an",
          "to",
          "he",
          "his",
          "all",
          "did",
          "what",
          "new",
          "can",
          "here",
          "weren't",
          "us",
          "or",
          "this",
          "we're",
          "want",
          "after",
          "onto",
          "for",
          "yes",
          "no",
          "got",
          "are",
          "why",
          "its",
          "it's"]
posts = []
f = open("credentials.txt")
platform = "praw"
app = "politics-scraper"
version = "0.1"
author = "(by /u/eine_bier_getrunken)"
agent = platform + ":"+app+":"+version+":"+author
appid = f.readline().rstrip()
secret = f.readline().rstrip()

reddit = praw.Reddit(client_id=appid, client_secret=secret, user_agent=agent)
subreddit = reddit.subreddit("politics")

#get parse program parameters from user input
input = Input()
persons, keywords = input.resolveInput(sys.argv)

print(persons)
print(keywords)
print "live reddit instance:" + str(reddit.read_only)
print "subreddit: " + str(subreddit.title)
count = 0
for post in reddit.subreddit('politics').submissions(1515888000,1515987464):
    count += 1
    p = Post()
    p.build(post)
    if count % 10 == 0:
        sys.stdout.write(".")
        if(count %100 == 0):
            sys.stdout.write("\n")
    posts.append(p)

print str(count) + " posts loaded.... beginning analytics..."
persondict = {}

def decomposeTitle(dict, post, filter=None, keywords=None):
    for word in post.title.split():
        #if we are using a stop word filter, apply it
        if filter and word in filter:
            continue
        #if we are using a keyword fiter, apply it
        if keywords and not word in keywords:
            continue
        #either add or not to dictionary
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1
    return dict

def searchPostsForPerson(person, filter=None, keywords=None):
    dict = {}
    for post in posts:
        if person in post.title:
            decomposeTitle(dict, post, filter, keywords)
    persondict[person]= dict


print("beginning analysis of " + str(count) + " posts using:")
print("------filter------")
pprint.pprint(filter)
if keywords:
    print("------keywords------")
    pprint.pprint(keywords)

for person in persons:
    sys.stdout.write("\nanalyzing " + str(count) + " posts for '" + person +"'")
    searchPostsForPerson(person, filter=filter)
    sys.stdout.write("...done\n")
    print("found " + str(persondict[person].keys().__len__()) + " unique words for " + person)

for person in persons:
    print("------" + person + "------")
    personwords = persondict[person]
    sortedWords = personwords.keys()
    for word in sortedWords:
        print(word + ": " + str(personwords[word]))
