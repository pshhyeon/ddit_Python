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
    
    # 연결 테스트
    def selectList(self) :
        sql = """
            select 
                m_id, m_name, tel, email 
            from mem
        """
        
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
        
    def selectOne(self, m_id) :
        sql = f"""
            select 
                m_id, m_name, tel, email 
            from 
                mem
            where 
                m_id = {m_id} 
        """
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
        
    def insert(self, m_id, m_name, tel, email) :
        sql = f"""
            insert into mem
                (m_id, m_name, tel, email) 
            values 
                ('{m_id}', '{m_name}', '{tel}', '{email}')
        """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
        
    def update(self, m_id, m_name, tel, email) :
        sql = f"""
            update mem
            set 
                m_name = '{m_name}', tel = '{tel}', email = '{email}'
            where 
                m_id = '{m_id}'
        """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
        
    def delete(self, m_id) :
        sql = f"""
            delete from mem
            where m_id = '{m_id}'
        """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
        
    # 소멸자
    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    pass
    
    
    
    
    