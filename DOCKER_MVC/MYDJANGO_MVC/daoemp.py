import pymysql
class DaoEmp:
    # 생성자
    def __init__(self):
        self.con = pymysql.connect(host='192.168.35.47'
                          , port = 3305
                          , user='root'
                          , password='python'
                          , db='python'
                          , charset='utf8')
    
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    
    # 전체 select
    def selectList(self) :
        sql = """
            select 
                e_id, e_name, gen, addr 
            from emp
        """
        
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list 

    # e_id와 일치하는 값 select 
    def selectOne(self, e_id) :
        sql = f"""
            select 
                e_id, e_name, gen, addr 
            from emp
            where e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        # fetchall() ==> 배열로 반환
        # vo = self.cur.fetchall()
        # 하나만 선택할때 fetchone()사용하는 것이 좋음 ==> 배열로 반환 안함
        vo = self.cur.fetchone()
        return vo
    
    def insert(self,e_id, e_name, gen, addr):
        sql = f"""
            INSERT INTO emp 
                (e_id, e_name, gen, addr)
            VALUES 
                ('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
        
        cnt = self.cur.execute(sql) 
        if cnt > 0 :
            self.con.commit()
        
        # cnt == self.cur.rowcount
        return(cnt)
    
    def update(self,e_id, e_name, gen, addr):
        sql = f"""
            UPDATE emp
            SET 
                e_name = {e_name}
                , gen = {gen}
                , addr = {addr}
            WHERE 
                e_id = {e_id}
        """
        
        cnt = self.cur.execute(sql)
        if cnt > 0 :
            self.con.commit()
        return(cnt)
    
    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp
            WHERE e_id = {e_id}
        """
        
        cnt = self.cur.execute(sql)
        if cnt > 0 :
            self.con.commit()
        return(cnt)
        
    # 소멸자
    def __del__(self):
        self.cur.close()
        self.con.close()
        

if __name__=='__main__' :
    de = DaoEmp()
    list = de.selectList()
    print('list',list)        
    vo = de.selectOne('1')
    print('vo',vo)
    
    