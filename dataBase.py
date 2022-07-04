import sqlite3
class SQLighter:

    def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subs` WHERE `status` = ?", (status,)).fetchall()

    def subs_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subs` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subs(self, user_id,username, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'subs' ('user_id', 'status', 'username') VALUES(?,?,?)", (user_id, status, username))

    #def take_name(self, username):
     #   with self.connection:
      #      return self.cursor.execute("INSERT INTO 'subs' ('username') VALUES(?)", (username,))


    def update_subs(self,user_id,status):
        with self.connection:
            return self.cursor.execute("UPDATE `subs` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        self.connection.close()