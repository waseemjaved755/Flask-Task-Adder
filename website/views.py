from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Task
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/' , methods = ['GET' , 'POST'])
@login_required
def home():
    print("Running Home views (((((((())))))))")
    if request.method == 'POST': 
        task = request.form.get('task')#Gets the note from the HTML 

        if len(task) < 1:
            flash('🚫 Bhai kuch likho gay to Save Hoga Na!😃', category='error') 
        else:
            new_task = Task(data=task, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_task) #adding the note to the database 
            db.session.commit()
            flash('✅ Yooooooooo Task Added Successfully! ', category='success')




    return render_template("home.html",user=current_user)   

@views.route('/deletetask', methods=['POST'])
def delete_task(): 
    print("Inside deleting Task") 
    data = request.get_json()  # Use get_json() instead of json.loads(request.data)
    taskId = data.get('taskId')

    task = Task.query.get(taskId)
    if task:
        print("Task to be deleted:", task)
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            flash('❌ Yooooooooo Task Deleted Successfully!', category='error')


    return jsonify({})