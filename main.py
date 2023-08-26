from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/todo'
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    content = db.Column(db.String(150), nullable=False)
    

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    data=Todo.query.all()

    return render_template('home.html', data=data)

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        title=request.form.get('title')
        content=request.form.get('content')
        data=Todo(title=title, content=content)
        db.session.add(data)
        db.session.commit()
        return redirect('home')
    
    return render_template('form.html')

@app.route('/delete', methods=['GET','POST'])
def delete_data():
    id=request.form.get("id")
    data_id=Todo.query.filter_by(sno=id).delete()
    db.session.commit()
    return redirect('home')




app.run(debug=True)


