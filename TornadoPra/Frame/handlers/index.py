# coding=utf-8
import tornado.web
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("index.html",user=one_user)

    def post(self):
        # 从前端传到后端的那个json对象的键的名字，是哪个键就获取该键的值。
        username = self.get_argument("username")
        password = self.get_argument("password")
        # 从后端向前端返回数据
        user_infos = mrd.select_table(
            table="users", colunm="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no user.")
