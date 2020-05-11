import pickle
from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from password import db
from password.models import BlogPost
from password.blog_posts.forms import BlogPostForm
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import load_model
from pickle import dump,load
import keras.backend.tensorflow_backend as tb
import numpy as np
import tensorflow
tb._SYMBOLIC_SCOPE.value = True

def custom1(input):
    List1=[]
    for i in input:
        List1.append(i)
    return List1

blog_posts = Blueprint('blog_posts',__name__)

def custom1(input):
    List1=[]
    for i in input:
        List1.append(i)
    return List1
@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        Username = form.Username.data
        Password = form.Password.data
        k=[Password]
        model = tensorflow.keras.models.load_model("C:\\Users\\hp\\Desktop\\dbmsproject\\Final_Project\\password\\blog_posts\\model2.h5")
        
       
        vc=pickle.load(open("C:\\Users\\hp\\Desktop\\dbmsproject\\Final_Project\\password\\blog_posts\\finally.pickle",'rb'))
        p=vc.transform(k)
        p=p.toarray()
        Strength=model.predict_classes(p,verbose=0)[0]
        Strength=int.from_bytes(Strength, "little")
        if Strength == 0:
            Strength = 'WEAK'
        elif Strength == 1:
            Strength = 'WEAK'
        else:
            Strength = 'Strong'
        # Add new Puppy to database
        new_pup = BlogPost(Username=Username,Password=Password,user_id=current_user.id,Strength=Strength)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('users.user_posts'))

    return render_template('create_post.html',form=form)
