from flask import Flask, render_template,url_for,redirect,request
from models import Student

a = Flask(__name__)
@a.route('/index')
def index():
    student =Student.select().order_by(Student.id.desc())
    return render_template('sx.html',sts=student)
@a.route('/details/<int:id>')
def details(id):
    st = Student.get_by_id(id)
    return render_template('details.html', s=st)

@a.route('/delete/<int:id>')
def delete(id):
    st = Student.get_by_id(id)
    st.delete_instance()
    return redirect(url_for('index'))

@a.route('/create',methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        Student.create(sname=fname, sfamily=lname,age=age)
        return redirect('index')

    return render_template('create.html')

@a.route('/update/<int:id>', methods =['GET', 'POST'])
def update(id):
    st = Student.get_by_id(id)
    if request.method == 'POST':
        st.sname = request.form['name']
        st.sfamily = request.form['family']
        st.age = request.form['aage']
        st.save()
        return redirect(url_for('index'))
    return render_template('update.html', ss=st)


if __name__== "__main__":
    a.run(debug=True)


