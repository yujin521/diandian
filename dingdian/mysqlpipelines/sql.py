import mysql.connector
from  dingdian import settings

MYSQL_HOSTS=settings.MYSQL_HOSTS
MYSQL_USER=settings.MYSQL_USER
MYSQL_PASSWORD=settings.MYSQL_PASSWORD
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB

cnx=mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
print(cnx)
cur=cnx.cursor(buffered=True)
print(cur)

class Sql:

    @classmethod
    def intsert_dd_name(cls,xs_name,xs_author,category,name_id):
        sql='INSERT INTO dd_name(xs_name,xs_author,category,name_id) VALUES(%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)'
        value={
            'xs_name':xs_name,
            'xs_author':xs_author,
            'category':category,
            'name_id':name_id
        }
        cur.execute(sql,value)
        cnx.commit()

    @classmethod
    def selcet_name(cls,name_id):
        sql='SELECT EXISTS(SELECT 1 From dd_name WHERE name_id=%(name_id)s)'
        value={
            'name_id':name_id
        }
        cur.execute(sql,value)
        return  cur.fetchall()[0]
    @classmethod
    def instert_dd_chaptername(cls,xs_chaptername,xs_content,id_name,num_id,url):
        sql='INSERT INTO dd_chaptername(xs_chaptername,xs_content,id_name,num_id,url)  \
            VALUES(%(xs_chaptername)s,%(xs_content)s,%(id_name)s,%(num_id)s,%(url)s)'
        value={
            'xs_chaptername':xs_chaptername,
            'xs_content':xs_content,
            'id_name':id_name,
            'num_id':num_id,
            'url':url
        }
        cur.execute(sql,value)
        cnx.commit()

    @classmethod
    def sclect_chapter(cls,url):
        sql='SELECT EXISTS(SELECT 1 From dd_chaptername WHERE url=%(url)s)'
        value={
            'url':url
        }
        cur.execute(sql,value)
        return  cur.fetchall()[0]