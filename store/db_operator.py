import pymysql
import traceback
from store.config import config

print(config)

class db_operator:
    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor()
        print("init ok.....")

    def select(self, db, sql):
        try:
            self.conn.select_db(db)
            count = self.cursor.execute(sql)
            print("数据条目: %d", count)
            results = self.cursor.fetchall()
            for result in results:
                print(result)
        except Exception as e:
            traceback.print_exc()
            self.conn.rollback()
        finally:
            # 关闭游标连接
            self.cursor.close()
            # 关闭数据库连接
            self.conn.close()

    def insert(self, db, sql):
        try:
            self.conn.select_db(db)
            count = self.cursor.execute(sql)
            self.cursor.execute(sql)
            print("数据条目: %d", count)
        except Exception as e:
            traceback.print_exc()
            self.conn.rollback()
        finally:
            # 关闭游标连接
            self.cursor.close()
            # 关闭数据库连接
            self.conn.close()


if __name__ == "__main__":
    do = db_operator()



