#!/usr/bin/env python3



# code for log-analysis-project
# Athour By : Alaa Adil Alaboud
# created At: Nov 15, 2018


import psycopg2

       # we connect to the db ("put the name of db")
db = psycopg2.connect("dbname=news")
       # for run queres and show the result
cursor = db.cursor()

# query for QUESTION1
def report_q1():
       # execute query
    cursor.execute("select articles.title, count(log.path) as views from articles join log on log.path = concat('/article/', articles.slug) group by articles.title order by views desc limit 3")
    results1 = cursor.fetchall()
    return results1


# query for QUESTION 2
def report_q2():
    cursor.execute("select authors.name, count(log.path) as views from authors join articles on articles.author = authors.id join log on log.path = concat('/article/', articles.slug) group by authors.name order by views desc")
    results2 = cursor.fetchall()
    return results2


 # query for QUESTION 3
def report_q3():
    cursor.execute("select total_time.day, round(errors.get_requests * 100.0 / total_time.get_requests, 3) as percent_num from(select date(log.time) as day, count(log.path) as get_requests from log group by day) as total_time join (select date(log.time) as day, count(log.path) as get_requests from log where log.status like '404%' group by day) as errors on total_time.day = errors.day where round(errors.get_requests * 100.0 / total_time.get_requests, 3) > 1.00 order by percent_num desc")
    results3 = cursor.fetchall()
    return results3


# print results
results1 = report_q1()
print('\nThe most popular three articles of all time: ')
count = 1
for i in results1:
    views = str(i[1]) + " views"
    print('"' + i[0] + '"' + " - " + views)
    count += 1

results2 = report_q2()
print("\nThe most popular article authors of all time: ")
count = 1
for i in results2:
    print(i[0] + ' - ' + str(i[1]) + " views")
    count += 1

results3 = report_q3()
print("\nThe days did more than 1% of requests lead to errors: ")
for i in results3:
    date = i[0].strftime('%B %d, %Y')
    errors = str(round(i[1]*100, 1)) + "%" + " errors"
    print(date + " - " + errors)
# close database
db.close()
