import pymysql

con = pymysql.connect(host='localhost'
                      , port = 3305
                      , user='root'
                      , password='python'
                      , db='python'
                      , charset='utf8')

cur = con.cursor(pymysql.cursors.DictCursor)

e_id = "6"
e_name = "6"
gen = "6"
addr = "6"

sql = f"""
    INSERT INTO emp 
        (e_id, e_name, gen, addr)
    VALUES 
        ('{e_id}', '{e_name}', '{gen}', '{addr}')
"""

cur.execute(sql) 
con.commit()
print("cnt", cur.rowcount)

cur.close()
con.close()
