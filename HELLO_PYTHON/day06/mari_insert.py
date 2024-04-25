import pymysql

con = pymysql.connect(host='localhost'
                      , port = 3305
                      , user='root'
                      , password='python'
                      , db='python'
                      , charset='utf8')

cur = con.cursor()
# cur = con.cursor(pymysql.cursors.DictCursor)



sql = """
    INSERT INTO emp 
        (e_id, e_name, gen, addr)
    VALUES 
        (%s, %s, %s, %s)
"""

# 튜플형식으로 값 넣기
res = cur.execute(sql, ("4", "4", "4", "4")) 
con.commit()
print(res)
# res = cur.fetchall()
# print(res)

cur.close()
con.close()
