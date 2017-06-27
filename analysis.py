#!/usr/bin/env python
import psycopg2
import datetime as vidit9


# a function to run the queries
def running(a, b=1):
    datab, cur = conn()
    c = None
    cur.execute(a)
    if b:
        c = cur.fetchall()
    datab.commit()
    datab.close()
    return c


# a function for errors when it gets above 1%
def auth():
    c = running("""select name, count from popular_author, total_count
    where popular_author.id=total_count.author""")
    for j in range(len(c)):
        print(" %s - %d " % (c[j][0], c[j][1]))
    return c


# a function to connect to database
def conn():
    datab = psycopg2.connect("dbname = news")
    cur = datab.cursor()
    return datab, cur


# a function for getting articles
def arti():
    c = running("""select title , view from article_view
    order by view desc LIMIT 3 """)
    for j in range(len(c)):
	    print(" %s - %d " % (c[j][0], c[j][1]))
    return c


# a function for getting authors
def mistake():
    c = running("""select date, 100.0* fail/total as probb
    from mistake where 100.0 * fail/total > 1 order by probb DESC""")
    date_time = vidit9.datetime.strptime(str(c[0][0]),
                                         '%Y-%m-%d').strftime("%B %d %Y")
    print(" %s - %s " % (date_time, round(c[0][1], 2)))
    return c


if __name__ == '__main__':
    arti()
    auth()
    mistake()
