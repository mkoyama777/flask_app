from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

# appという変数名で Flask オブジェクトをインスタンス化
app = Flask(__name__)

#WTForms を使い、index.htmlで表示させるフォームを構築
class InputForm(Form):
    InputFormTest = StringField('文字を入力してください',
                    [validators.InputRequired()])

    # HTML 側で表示する submit ボタンの表示
    submit = SubmitField('送信')

#URLにアクセスがあった場合の挙動の設定
@app.route('/',methods=["GET",'POST'])
def input():
    #WTFormsで構築したフォームをインスタンス化
    form = InputForm(request.form)
    #POST メソッドの条件の定義
    if request.method == 'POST':
        
        if form.validate() == False:
            #条件に当てはまらない場合（StringFieldに値がない場合)
            return render_template('index.html')
        else:
            #条件に当てはまる場合（StringFieldに値がある場合)
            outputname_ = request.form['InputFormTest']
            return render_template('result.html',outputname=outputname_)
    #GET メソッドの条件の定義
    elif request.method == 'GET':
        return render_template('index.html',forms=form)
#アプリケーションの実行の定義
if __name__ == '__main__':
    app.run(debug=True)