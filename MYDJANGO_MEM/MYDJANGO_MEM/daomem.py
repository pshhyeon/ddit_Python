import pymysql
class DaoMem:
    # 생성자
    def __init__(self):
        self.con = pymysql.connect(host='localhost'
                          , port = 3305
                          , user='root'
                          , password='python'
                          , db='python'
                          , charset='utf8')
    
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self) :
        sql = """
            select 
                m_id, m_name, tel, email 
            from mem
        """
        
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return(list)
        
    # 소멸자
    def __del__(self):
        pass

if __name__ == '__main__':
    dm = DaoMem();
    list = dm.selectList();
    print('list',list)