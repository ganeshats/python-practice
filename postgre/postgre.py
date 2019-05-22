import psycopg2.extras


def mod_for_num(iter):
    div, mod = divmod(iter,26)
    values = [div, mod]
    if 0 in values: values.remove(0)
    if div <= 26:
        return values
    else:
        tmp = mod_for_num(div)
        values.remove(div)
        tmp.extend(values)
        return tmp


def str_maker(iter):
    return reduce(lambda x, y: str(x) + chr(96+y),mod_for_num(iter) ,"")

# print str_maker(2) # abn - 742

try:
    conn = psycopg2.connect("host='localhost' dbname='ganesha'")
    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # curs = conn.cursor()
    curs.execute(""" SELECT * from test """)
    rows = curs.fetchall()
    addRows = input("We have {0} rows. Enter 1 to add and 2 to delete: ".format(len(rows)))
    while addRows not in [1,2]:
        addRows = input("We have {0} rows. Enter 1 to add and 2 to delete. Nothing else please: ".format(len(rows)))

    maxi = max(rows, key=lambda i: i["id"])["id"]

    if addRows == 1:
        rowsToAdd = input("We have {0} rows. Enter the no.of rows to add: ".format(len(rows)))
        maxi += 1
        for i in range(rowsToAdd):
            curs.execute('INSERT INTO test ("id","name","done") VALUES ( %s,%s,%s) ',
                         (str(maxi + i), str_maker(maxi + i), (maxi + i) % 2 == 0))
    else:
        rowsToDel = input("We have {0} rows. Enter the no.of rows to Del: ".format(len(rows)))
        for i in range(rowsToDel):
            curs.execute('DELETE FROM test where ID= %s', (maxi - i,))

    conn.commit()
    curs.close()
    conn.close()
except Exception as e: print "Connection failure {0}".format(e)
