from flask import Flask, render_template, request, session, redirect
from flask_pymongo import PyMongo
import bson
# import os
# import io
# from PIL import Image

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['MONGO_URI'] = 'mongodb://localhost/hk_chd'
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user' in session:
        result = mongo.db.twits.find()
        list_r = list(result)
        print(list_r)
        # mongo.send_file()
        return render_template('home.html', posts=list_r)
    if request.method == 'POST':
        username = request.form.get('email')
        userpass = request.form.get('pass')
        re = mongo.db.users.find_one({"email": username, "password": userpass})
        if re is None:
            return render_template('login.html', i="invalid Id/Password")
        else:
            session['user'] = username
            result = mongo.db.twits.find()
            list_r = list(result)
            print(list_r)
            # mongo.send_file()
            return render_template('home.html', posts=list_r)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        content = request.form
        profile = content['username']
        msg = content['tweet']
        # print(img)
        # image = Image.open(io.BytesIO(img))
        # image.save("./")
        #mongo.save_file(img.filename, img)
        #mongo.db.twits.insert({'profile': profile, 'tweet': msg, 'profile_img': img.filename})
        # if 'profile_image' in request.files:
        #     profile_image = request.files['profile_image']
        #     mongo.save_file(profile_image.filename, profile_image)
        mongo.db.twits.insert({'profile': profile, 'tweet': msg})

        return 'Done!'


@app.route('/send')
def send():
    return '''
        <form method = "POST" action = "/create" enctype = "multipart/form-data">
            <input type = "text" name = "profile">
            <textarea name="msg">Enter text here...</textarea>
            <input type = "file" name = "profile_image">
            <input type = "submit" value = "submit">
        </form>
    '''


@app.route('/create', methods=['POST'])
def create():
    profile = request.form.get('profile')
    msg = request.form.get('msg')
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.twits.insert({'profile': profile, 'tweet': msg, 'profile_img': profile_image.filename})

    return 'Done!'


@app.route('/profile/<id>')
def file(id):
    print(id)
    re = mongo.db.twits.find_one({"_id": bson.ObjectId(oid=str(id))})
    print(re)
    return mongo.send_file(re['profile_img'])


'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        passw = request.form.get('pass')
        result = mongo.db.nt.find_one({"passw": passw, "email": email})
        print(result)
    return render_template('login.html')
'''

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


