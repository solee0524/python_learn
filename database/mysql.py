#!/usr/bin/python

__author__ = 'oracle'

import MySQLdb


def find_result(input_result):
    line = []
    for i in input_result:
        line.append(str(i))
    print line

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='******', port=3306, charset='utf8')
    #select database
    conn.select_db('sakila')
    cur = conn.cursor()

    count = cur.execute('select * from actor')
    print 'Total %s records in actor table (%s)' % (count, count)

    #fetch one record from result set
    print 'fetch one record'
    result = cur.fetchone()
    print 'Type of result:', type(result)
    find_result(result)

    #fetch ten records from result set
    print '\nfetch ten records'
    results = cur.fetchmany(10)
    print 'Type of results:', type(results)
    for result in results:
        find_result(result)

    # .fetchall() is finding all records

    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

