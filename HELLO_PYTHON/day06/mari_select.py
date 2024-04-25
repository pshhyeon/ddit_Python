import pymysql

con = pymysql.connect(host='localhost'
                      , port = 3305
                      , user='root'
                      , password='python'
                      , db='python'
                      , charset='utf8')

# cur = con.cursor()
# (('1', '1', '1', '1'), ('2', '2', '2', '2')) 
# ==> tuple(튜플)로 반환
cur = con.cursor(pymysql.cursors.DictCursor)
# [{'e_id': '1', 'e_name': '1', 'gen': '1', 'addr': '1'}, {'e_id': '2', 'e_name': '2', 'gen': '2', 'addr': '2'}]
# ==> dictionary로 반환(json과 비슷)


sql = """
    select 
        e_id, e_name, gen, addr 
    from emp
"""
        

cur.execute(sql)
res = cur.fetchall()
print(res)

cur.close()
con.close()
