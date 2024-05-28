
from flask import render_template, flash, send_file, request, redirect, url_for, session, jsonify, Blueprint
from app import app
from flask_bcrypt import Bcrypt
import requests
from views.dbrequest import DatabaseRequest
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
from datetime import date
import uuid
from werkzeug.datastructures import FileStorage
from datetime import datetime
import random
import pdfkit
from tempfile import NamedTemporaryFile
from functools import wraps 
from flask_wtf import CSRFProtect

app.secret_key = "8fe371ec0736a5e4a39f125a44686ae37c4a1f15"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cyberdb'
app.config['UPLOAD_FOLDER'] = 'static/uploads/topic_video'
app.config['SECRET_KEY'] = '8fe371ec0736a5e4a39f125a44686ae37c4a1f15'  
csrf = CSRFProtect(app)

bcrypt = Bcrypt(app)
mysql = MySQL(app)
db_request = DatabaseRequest(mysql)

@app.route('/')
def index():
    return render_template('index.html')

#---------------------------- Safe Guard ----------------------------#\
def requires_authentication_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated

def requires_authentication_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'admin_id' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated
#---------------------------- End Safe Guard ----------------------------#

#---------------------------- Login and Register Page ----------------------------#
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if all([username, email, password]):
            check_acc = db_request.get_detail('CHECK_ACCOUNT_DETAIL', (username, email))
            
            if check_acc:
                flash('Username or email already exists', 'danger')
                return redirect(url_for('register'))
            else:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                db_request.insert_data('REGISTER', (fullname, username, email, hashed_password))
                flash('You have successfully registered', 'success')
                return redirect(url_for('register'))
        
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['login-userName']
    password = request.form['login-password']
    
    if all([username, password]):
        get_account = db_request.get_detail('GET_ACCOUNT', (username,))
        if get_account:
            if bcrypt.check_password_hash(get_account['user_password'], password):
                        session['user_id'] =   get_account['user_id']
                        session['fullname'] = get_account['user_name']
                        session['email'] = get_account['user_email']
                        return redirect(url_for('user.dashboard'))
            else:
                flash('Incorrect password or email !', 'danger')
                return redirect(url_for('index'))
        else:
            flash('Incorrect password or email !', 'danger')
            return redirect(url_for('index'))
        
#---------------------------- End Login and Register Page ----------------------------#

#---------------------------------- Admin Blueprint ---------------------------------#
admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@admin_blueprint.route('/')
def admin_index():
    return render_template('/admin/index.html')

@admin_blueprint.route('/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if all([username, email, password]):
            check_acc = db_request.get_detail('CHECK_ACCOUNT_DETAIL_ADMIN', (username, email))
            
            if check_acc:
                flash('Username or email already exists', 'danger')
                return redirect(url_for('admin.admin_register'))
            else:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                db_request.insert_data('REGISTER_ADMIN', (username, email, hashed_password))
                flash('You have successfully registered', 'success')
                return redirect(url_for('admin.admin_register'))
        
    return render_template('/admin/register.html')


@admin_blueprint.route('/login', methods=['POST'])
def admin_login():
    username = request.form['login-userName']
    password = request.form['login-password']
    
    if all([username, password]):
        get_account = db_request.get_detail('GET_ACCOUNT_ADMIN', (username,))
        if get_account:
            if bcrypt.check_password_hash(get_account['admin_password'], password):
                session['admin_id'] =   get_account['admin_id']
                session['username'] = get_account['admin_username']
                session['email'] = get_account['admin_email']
                session['fullname'] = get_account['admin_name']
                return redirect(url_for('admin.admin_dashboard'))
             
            else:
                flash('Incorrect password or email !', 'danger')
                return redirect(url_for('admin.admin_index'))
        else:
            flash('Incorrect password or email !', 'danger')
            return redirect(url_for('admin.admin_index'))

@admin_blueprint.route('/dashboard')
@requires_authentication_admin
def admin_dashboard():
    get_count_all_topic = db_request.get_detail('GET_COUNT_ALL_TOPIC', ())[0]
    get_all_user = db_request.get_detail('GET_ALL_USER', ())
    total_user = len(get_all_user)
    activate_acc = sum(1 for d in get_all_user if d['account_status'] == 1)
    unactivate_acc = sum(1 for d in get_all_user if d['account_status'] == 0)
    get_all_topic = db_request.get_detail('GET_ALL_TOPIC', ())
    return render_template('/admin/dashboard.html',
                           get_count_all_topic=get_count_all_topic,
                           total_user=total_user,
                           activate_acc=activate_acc,
                           unactivate_acc=unactivate_acc,
                           get_all_topic=get_all_topic)

@admin_blueprint.route('/admin-profile')
@requires_authentication_admin
def admin_profile():
    return render_template('/admin/admin-profile.html')

@admin_blueprint.route('/add-material', methods=['GET', 'POST'])
@requires_authentication_admin
def add_material():
    if request.method == 'POST':
        topic_title = request.form['topic-title']
        topic_description = request.form['topic-description']
        topic_lesson = request.form['topic-lesson']
        topic_video = request.form.get('topic-video')

        questions = {}
        answers = {}
        for i in range(1, 11):
            questions[f'question_{i}'] = request.form.get(f'question-{i}')
            if i in range(1, 7):  # For multiple choice questions
                for j in range(1, 5):
                    answers[f'answer_q{i}_{j}'] = request.form.get(f'answer{j}-question{i}')
            else:  # For single answer questions
                answers[f'answer_q{i}_1'] = request.form.get(f'answer1-question{i}')

        if 'topic-video' not in request.files:
            flash('No file part')
            return redirect(request.url)
        topic_video = request.files['topic-video']

        if topic_video.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if topic_video and allowed_file(topic_video.filename) and all([topic_title, topic_description, topic_video, questions]):
            random_filename = str(uuid.uuid4())
            file_extension = os.path.splitext(topic_video.filename)[1]
            filename = secure_filename(random_filename + file_extension)
            topic_video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))   
            current_date = date.today()
            topic_id = db_request.insert_data('ADD_TOPIC', (topic_title, topic_description, topic_lesson, filename, current_date, session['admin_id']))
            question_id = db_request.insert_data('ADD_QUESTION', (topic_id, questions['question_1'], questions['question_2'], questions['question_3'], questions['question_4'], questions['question_5'],
                                                                questions['question_6'], questions['question_7'], questions['question_8'], questions['question_9'], questions['question_10']))
            answers_list = [question_id]
            for i in range(1, 11):  
                if i in range(1, 7):  # For multiple choice questions
                    for j in range(1, 5):
                        answers_list.append(answers[f'answer_q{i}_{j}'])
                else:  # For single answer questions
                    answers_list.append(answers[f'answer_q{i}_1'])
            db_request.insert_data('ADD_ANSWER', tuple(answers_list))
            flash('You have successfully added a new material', 'success')
                         
    return render_template('/admin/add-material.html')
    
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'wmv'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
                  
@admin_blueprint.route('/view-material', methods=['GET', 'POST'])
@requires_authentication_admin
def views_material():
    if request.method == 'POST':
        
        if 'edit-button' in request.form:
            topic_id = request.form['topic-id']
            question_id = request.form['question-id']
            answer_id = request.form['answer-id']
            topic_title = request.form['topic-title']
            topic_description = request.form['topic-description']
            topic_lesson = request.form['topic-lesson']
            topic_video = request.files.get('topic-video')
            popup_question = request.form.get('popup-question')
            popup_answer = request.form.get('popup-answer')
            
            if topic_video.filename == '':
                topic_video = request.form.get('topic-video-hidden')
                
            questions = {}
            answers = {}
            for i in range(1, 11):
                questions[f'question_{i}'] = request.form.get(f'question-{i}')
                if i in range(1, 7):  # For multiple choice questions
                    for j in range(1, 5):
                        answers[f'answer_q{i}_{j}'] = request.form.get(f'answer{j}-question{i}')
                else:  # For single answer questions
                    answers[f'answer_q{i}_1'] = request.form.get(f'answer1-question{i}')
            
            if all([topic_title, topic_description, topic_lesson, topic_video, questions]):
                if isinstance(topic_video, FileStorage):
                    random_filename = str(uuid.uuid4())
                    file_extension = os.path.splitext(topic_video.filename)[1]
                    filename = secure_filename(random_filename + file_extension)
                    topic_video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
                else:
                    filename = topic_video  
                    
                current_date = date.today()
                db_request.update_data('EDIT_TOPIC', (topic_id, topic_title, topic_description, topic_lesson, filename, current_date, session['admin_id'], popup_question, popup_answer))
                db_request.update_data('EDIT_QUESTION', (question_id, questions['question_1'], questions['question_2'], questions['question_3'], questions['question_4'], questions['question_5'],
                                                                    questions['question_6'], questions['question_7'], questions['question_8'], questions['question_9'], questions['question_10']))
                answers_list = [answer_id, question_id]
                for i in range(1, 11):  
                    if i in range(1, 7): 
                        for j in range(1, 5):
                            answers_list.append(answers[f'answer_q{i}_{j}'])
                    else:  
                        answers_list.append(answers[f'answer_q{i}_1'])
                db_request.update_data('EDIT_ANSWER', tuple(answers_list))
                flash('You have successfully edited the topic', 'success')
                
                
        elif 'delete-button' in request.form:
            topic_id = request.form['topic-id']
            question_id = request.form['question-id']
            answer_id = request.form['answer-id']
            
            db_request.delete_data('DELETE_ANSWER', (answer_id,))
            db_request.delete_data('DELETE_QUESTION', (question_id,))
            db_request.delete_data('DELETE_TOPIC', (topic_id,))
            
            flash('You have successfully deleted the topic', 'success')
        
        return redirect(url_for('admin.views_material'))
        
     
    get_all_topic = db_request.get_detail('GET_ALL_TOPIC', ())
    return render_template('/admin/view-material.html', get_all_topic=get_all_topic)

@admin_blueprint.route('/password-checker')
@requires_authentication_admin
def password_checker():
    return render_template('/admin/password-checker.html')

@admin_blueprint.route('/view-users', methods=['GET', 'POST'])
@requires_authentication_admin
def admin_view_users():
    if request.method == 'POST':
        if 'edit-button' in request.form:
            user_id = request.form['user-id']
            user_fullname = request.form['user-fullname']
            username = request.form['user-username']
            user_email = request.form['user-email']
            user_password = request.form['user-password']
            if all([user_fullname, username, user_email, user_password]):
                get_user_password = db_request.get_detail('GET_USER_PASSWORD', (user_id,))
                if get_user_password['user_password'] != user_password:
                    user_password = bcrypt.generate_password_hash(user_password).decode('utf-8')
                db_request.update_data('EDIT_USER', (user_id, user_fullname, username, user_email, user_password))
                flash('You have successfully edited the user', 'success')
            
        elif 'delete-button' in request.form:
            db_request.delete_data('DELETE_USER', (request.form['user-id'],))
            flash('You have successfully deleted the user', 'success')
        
        elif 'activate-button' in request.form:
            db_request.update_data('USER_ACCOUNT_STATUS', (request.form['user-id'], 1))
            flash('You have successfully activated the user', 'success')
            
        elif 'deactivate-button' in request.form:
            db_request.update_data('USER_ACCOUNT_STATUS', (request.form['user-id'], 0))
            flash('You have successfully activated the user', 'success')
            
        return redirect(url_for('admin.admin_view_users'))
        
    get_all_user = db_request.get_detail('GET_ALL_USER', ())
    get_count_all_topic = db_request.get_detail('GET_COUNT_ALL_TOPIC', ())[0]
    return render_template('/admin/view-users.html', get_all_user=get_all_user, get_count_all_topic=get_count_all_topic)

@admin_blueprint.route('/generate-report/<user_id>')
@requires_authentication_admin
def admin_generate_report(user_id):
    get_user_report = db_request.get_detail('GET_USER_REPORT', user_id,)
    total_topic = len(get_user_report)
    completed_topic = sum(1 for row in get_user_report if row['completed'] == 'Yes')
    today = datetime.today().strftime('%d %A %Y')
    
    for report in get_user_report:
        if report['first_score'] != 'None':
            report['first_score'] = int(report['first_score'])
        if report['second_score'] != 'None':
            report['second_score'] = int(report['second_score'])
            
    get_detail = db_request.get_detail('GET_USER_DETAIL', (user_id,))

    html = render_template('/admin/report-template.html', get_user_report=get_user_report, total_topic=total_topic, completed_topic=completed_topic, today=today, get_detail=get_detail)
    with NamedTemporaryFile(suffix=".pdf", delete=False) as temp:
        pdfkit.from_string(html, temp.name)

    get_full_name = db_request.get_detail('GET_FULL_NAME', (user_id,))[0]
    return send_file(temp.name, as_attachment=True, download_name=get_full_name + ' Report.pdf')


@admin_blueprint.route('/logout')
@requires_authentication_admin
def admin_logout():
    session.clear()
    return redirect(url_for('index'))

app.register_blueprint(admin_blueprint)
#------------------------------ End Of Admin Blueprint -------------------------------#

#------------------------------- User Blueprint ------------------------------------#
user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.route('/dashboard')
@requires_authentication_user
def dashboard():
    get_quiz_history = db_request.get_detail('GET_QUIZ_HISTORY', (session['user_id'],))
    get_user_report = db_request.get_detail('GET_USER_REPORT', (session['user_id'],))
    total_count = len(get_user_report)
    completed_count = sum(1 for d in get_user_report if d['completed'] == 'Yes')
    pass_count = sum(1 for d in get_user_report if d['status'] == 'PASS')
    fail_count = sum(1 for d in get_user_report if d['status'] == 'FAIL')
    return render_template('/user/dashboard.html', get_quiz_history=get_quiz_history,
                           total_count=total_count, completed_count=completed_count,
                           pass_count=pass_count, fail_count=fail_count)

@user_blueprint.route('/user-profile')
@requires_authentication_user
def user_profile():
    return render_template('/user/user-profile.html')

@user_blueprint.route('/password-checker')
@requires_authentication_user
def password_checker_user():
    return render_template('/user/password-checker.html')

@user_blueprint.route('/material')
@requires_authentication_user
def user_material():
    get_material = db_request.get_detail('GET_MATERIAL', (session['user_id'],))
    return render_template('/user/material.html', get_material=get_material)

@user_blueprint.route('/lesson/<topic_id>')
@requires_authentication_user
def lesson(topic_id):
    check_taken_quiz = db_request.get_detail('CHECK_TAKEN_QUIZ', (session['user_id'], topic_id))
    if check_taken_quiz:
        if check_taken_quiz['retake'] == 'true' and check_taken_quiz['retake_taken'] == 2:
            return redirect(url_for('user.user_material'))
        
    get_course_lesson = db_request.get_detail('GET_COURSE_LESSON', (topic_id,))
    return render_template('/user/lesson.html', get_course_lesson=get_course_lesson)

@user_blueprint.route('/lesson-video/<topic_id>')
@requires_authentication_user
def lesson_video(topic_id):
    check_taken_quiz = db_request.get_detail('CHECK_TAKEN_QUIZ', (session['user_id'], topic_id))
    if check_taken_quiz:
        if check_taken_quiz['retake'] == 'true' and check_taken_quiz['retake_taken'] == 2:
            return redirect(url_for('user.user_material'))
        
    get_course_lesson = db_request.get_detail('GET_COURSE_LESSON', (topic_id,))
    return render_template('/user/lesson-video.html', get_course_lesson=get_course_lesson)

@user_blueprint.route('/quiz/<topic_id>')
@requires_authentication_user
def quiz(topic_id):
    check_taken_quiz = db_request.get_detail('CHECK_TAKEN_QUIZ', (session['user_id'], topic_id))
    if check_taken_quiz:
        if check_taken_quiz['retake'] == 'true' and check_taken_quiz['retake_taken'] == 2:
            return redirect(url_for('user.user_material'))
        
    session['topic_id'] = topic_id
    get_qna = db_request.get_detail('GET_QNA', (topic_id,))
    return render_template('/user/quiz.html', get_qna=get_qna)

@user_blueprint.route('/quiz-result/<question_id>', methods=['POST', 'GET'])
@requires_authentication_user
def quiz_result(question_id):
        
    if request.method == 'POST':
        correct_answers = db_request.get_detail('GET_ANSWER', (question_id,))
        user_answers = {}
        for i in range(1, 11):
            answer = request.form.get('q_answer{}'.format(i))
            if answer:
                user_answers['question{}'.format(i)] = answer.strip().lower()
        score = calculate_score(correct_answers, user_answers)
        session['score'] = score
        
        retake = 'false'
        retake_taken = 1
        check_history = db_request.get_detail('CHECK_SCORE', (session['user_id'], session['topic_id']))
        old_score = None
        if check_history:
            if check_history['retake'] == 'false' and check_history['retake_taken'] == 1:
                retake = 'true'
                retake_taken = 2
                old_score = check_history['score1']
                db_request.delete_data('DELETE_DATA', (session['user_id'], session['topic_id']))
        
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        date_str, time_str = date_time_str.split()
        
        time_object = datetime.strptime(time_str, "%H:%M:%S")
        time_str = time_object.strftime("%I:%M:%S %p")
        
        db_request.insert_data('ADD_SCORE1', (
            session['user_id'], 
            session['topic_id'], 
            time_str,
            date_str,
            score,
            retake,
            retake_taken
            
        ))
        
        return redirect(url_for('user.quiz_result', question_id=question_id))
    
    return render_template('/user/quiz-result.html', question_id=question_id)


def calculate_score(correct_answers, user_answers):
    score = 0
    for i in range(1, 11):
        question_key = 'question{}_answer1_t'.format(i)
        user_answer_key = 'question{}'.format(i)

        if question_key in correct_answers and user_answer_key in user_answers:
            if correct_answers[question_key].strip().lower() == user_answers[user_answer_key]:
                score += 1
    return score

@user_blueprint.route('/individual-report')
@requires_authentication_user
def individual_report():
    get_user_report = db_request.get_detail('GET_USER_REPORT', (session['user_id'],))
    total_topic = len(get_user_report)
    completed_topic = sum(1 for row in get_user_report if row['completed'] == 'Yes')
    today = datetime.today().strftime('%d %A %Y')
    
    for report in get_user_report:
        if report['first_score'] != 'None':
            report['first_score'] = int(report['first_score'])
        if report['second_score'] != 'None':
            report['second_score'] = int(report['second_score'])
            
    return render_template('/user/individual-report.html', get_user_report=get_user_report, total_topic=total_topic, completed_topic=completed_topic, today=today)


@user_blueprint.route('/generate-report')
@requires_authentication_user
def generate_report():
    get_user_report = db_request.get_detail('GET_USER_REPORT', (session['user_id'],))
    total_topic = len(get_user_report)
    completed_topic = sum(1 for row in get_user_report if row['completed'] == 'Yes')
    today = datetime.today().strftime('%d %A %Y')
    
    for report in get_user_report:
        if report['first_score'] != 'None':
            report['first_score'] = int(report['first_score'])
        if report['second_score'] != 'None':
            report['second_score'] = int(report['second_score'])

    html = render_template('/user/report-template.html', get_user_report=get_user_report, total_topic=total_topic, completed_topic=completed_topic, today=today)
    with NamedTemporaryFile(suffix=".pdf", delete=False) as temp:
        pdfkit.from_string(html, temp.name)

    return send_file(temp.name, as_attachment=True, download_name=session['fullname'] + ' Report.pdf')


@user_blueprint.route('/logout')
@requires_authentication_user
def user_logout():
    session.clear()
    return redirect(url_for('index'))

def shuffle(seq):
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq

app.jinja_env.filters['shuffle'] = shuffle

app.register_blueprint(user_blueprint)

#------------------------------- End User Blueprint ------------------------------------#


@app.template_filter('format_date')
def format_date(value, format='%d %A %Y'):
    if value != 'None':
        return datetime.strptime(value, '%Y-%m-%d').strftime(format)
    return value