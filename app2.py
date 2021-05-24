from flask import Flask, render_template
app = Flask(__name__)
#取消靜態網頁快取時間設定為0
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

#類別
class User:
    def __init__(self,name,age,is_vip):
        self.name=name
        self.age=age
        self.is_vip=is_vip
#串列
user_list = [
    User("Andy",30,True),
    User("john",31,True),
    User("eason",32,False),
    User("mark",35,True)
]

@app.route('/')
def home_page():
    #變數宣告
    main_title="mySite"
    subtitle="welcome"
    author={
        "name":"yucheng",
        "email":"yucheng@mail.com",
        "phone":"0960123456"
    }
    #是否顯示subtitle變數
    show_subtitle=False
    #將變數傳送到模板
    return render_template("home.html",
    a=main_title,
    b=subtitle,
    c=author,
    d=show_subtitle,
    e=user_list)

#動態路由<uid>
@app.route('/user/<int:uid>')
#加入參數uid
def user_page(uid):
    #轉換成整數
    #uid=int(uid)
    #從user_list取得索引為uid的資料
    try:
        user=user_list[uid]
        return render_template("user.html",
        user=user)
    except IndexError:
        #return "你所查詢的{uid}頁面不存在"
        return render_template("user_not_found.html",uid=uid)

if __name__ == '__main__':
    app.run(debug=True)
