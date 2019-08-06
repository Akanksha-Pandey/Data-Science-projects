## 1. Introduction ##

# Stream column for top 5 songs only
top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]
def average(values):
    total = 0.
    for s in values:
        total += s
    return total/len(values)
    
total_average = average(top5_streams)

## 2. Introduction to Modules ##

top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]
import statistics

average = statistics.mean(top5_streams)

## 3. Loading our data using the CSV module ##

import csv
f = open("top100.csv","r")
csvreader = csv.reader(f)
music = list(csvreader)

print(music)

## 4. Understanding the namespace ##

import statistics
print(dir())
print(dir(statistics))

## 5. Cleaning Our Data ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))
music = music[1:]
stream_num =[]
track_name =[]
for rows in music:
    stream_num.append(int(rows[3]))
    track_name.append(rows[0])

    

## 6. Writing Modular Code ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))

stream_num = []
track_name = []

for song in music[1:]:
    stream_num.append(int(song[3]))
    track_name.append(song[0])
def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))


def get_data(data):
    list1 = []
    list2 = []
    for x in data[1:]:
        list1.append(int(x[3]))
        list2.append(x[0])
    return list1, list2
 

print(dir())

## 7. Local and Global Variables ##

filename = "top100.csv"
def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))

f=read_data(filename)

## 8. Using Programming Paradigms ##

def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))


def get_data(data):
    list1 = []
    list2 = []
    for x in data[1:]:
        list1.append(int(x[3]))
        list2.append(x[0])
    return list1, list2

def ceil(data):
    ceiling = 0
    for x in data:
        if x > ceiling:
            ceiling = x
        else:
            ceiling
    return ceiling

def average(data):
    total = 0
    for x in data:
        total += x
    return total/len(data)

music = read_data("top100.csv")
(stream_num, track_name) = get_data(music)
average = average(stream_num)

## 9. Importing using an Alias ##

import statistics as s

variation = s.stdev(stream_num)

## 10. Importing Specific Objects ##

from statistics import mean, stdev, median

average = statistics.mean(stream_num)
variation = statistics.stdev(stream_num)
med = statistics.median(stream_num)