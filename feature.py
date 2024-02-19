from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField
FAI = Flask(__name__)

@FAI.route('/htmlforms',methods = ['GET','POST'])
def htmlforms():
    if request.method == 'POST':
        fd = request.form
        un = fd['un']
        return un
    return render_template('htmlforms.html')

class Webform(Form):
    name = StringField()
    submit = SubmitField()

@FAI.route('/webforms',methods = ['GET','POST'])
def webforms():
    nfo = Webform()
    if request.method == 'POST':
        nfd = Webform(request.form)
        if nfd.validate():
            return nfd.name.data
    return render_template('webforms.html',nfo = nfo)



if __name__ == '__main__':
    FAI.run(debug=True,host='192.168.137.1',port=2002)