class DatabaseRequest:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_detail(self, query_type, data):
        cur = self.mysql.connection.cursor()
        
        if query_type == 'GET_ACCOUNT':
            USERNAME = data[0]

            sql_query = """
                SELECT user_id, user_name, user_email, user_password, account_status FROM users WHERE user_username = %s;
            """

            cur.execute(sql_query, (USERNAME,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'GET_USER_DETAIL':
            USER_ID = data[0]

            sql_query = """
                SELECT user_id, user_name, user_email FROM users WHERE user_id = %s;
            """

            cur.execute(sql_query, (USER_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        
        if query_type == 'CHECK_ACCOUNT_DETAIL':
            USERNAME = data[0]
            EMAIL = data[1]

            sql_query = """
                SELECT user_username, user_email FROM users WHERE user_username = %s or user_email = %s;
            """

            cur.execute(sql_query, (USERNAME, EMAIL))
            result = cur.fetchone()
            cur.close()
            return result
        
        if query_type == 'GET_ACCOUNT_ADMIN':
            USERNAME = data[0]

            sql_query = """
                SELECT admin_name, admin_id, admin_username, admin_email, admin_password FROM admin WHERE admin_username = %s;
            """

            cur.execute(sql_query, (USERNAME,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'CHECK_ACCOUNT_DETAIL_ADMIN':
            USERNAME = data[0]
            EMAIL = data[1]

            sql_query = """
                SELECT admin_username, admin_email FROM admin WHERE admin_username = %s or admin_email = %s;
            """

            cur.execute(sql_query, (USERNAME, EMAIL))
            result = cur.fetchone()
            cur.close()
            return result
    
        if query_type == 'GET_MATERIAL':
            USER_ID = data[0]
            
            sql_query = """
SELECT 
    tp.*,
    COALESCE(
        CASE
            WHEN q.retake_taken = 1 AND q.quiz_status = 'PASS' THEN 'No'
            WHEN q.retake_taken = 1 AND q.quiz_status = 'FAIL' THEN 'Yes'
            WHEN q.retake_taken = 2 THEN 'No'
            ELSE 'Yes' -- Return 'Yes' when there is no matching data in quiz_history
        END,
        'Yes' -- Default to 'Yes' when there is no matching data in quiz_history
    ) as retake_allowed,
    CASE
        WHEN q.topic_id IS NOT NULL THEN 'Yes'  -- Matching data exists
        ELSE 'No'  -- No matching data
    END as matching_data_exists
FROM 
    topic as tp
LEFT JOIN 
    quiz_history as q ON tp.topic_id = q.topic_id AND q.user_id = %s
ORDER BY
    tp.topic_id ASC;






            """

            cur.execute(sql_query, (USER_ID,))
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            results_dicts = [dict(zip(column_names, result)) for result in results] if column_names and results else []
            cur.close()
            return results_dicts

        if query_type == 'GET_ALL_TOPIC':
            
            sql_query = """
                SELECT
                t.*, 
                q.*,
                an.*,
                a.admin_name 
                FROM topic as t 
                JOIN admin as a ON t.topic_register_by = a.admin_id
                JOIN question as q on t.topic_id = q.topic_id
                JOIN answer as an on q.question_id = an.question_id;
            """

            cur.execute(sql_query)
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            results_dicts = [dict(zip(column_names, result)) for result in results] if column_names and results else []
            cur.close()
            return results_dicts
        
        if query_type == 'GET_COURSE_LESSON':
            TOPIC_ID = data[0]
            
            sql_query = """
                SELECT * FROM topic where topic_id = %s;
            """

            cur.execute(sql_query, (TOPIC_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict

        if query_type == 'GET_QNA':
            TOPIC_ID = data[0]

            sql_query = """
                SELECT
                tp.topic_id,
                tp.topic_title,
                qs.*,
                aw.*
                FROM question as qs
                JOIN answer aw ON qs.question_id = aw.question_id
                JOIN topic tp ON qs.topic_id = tp.topic_id
                WHERE qs.topic_id = %s;
            """

            cur.execute(sql_query, (TOPIC_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'GET_ANSWER':
            QUESTION_ID = data[0]
            
            sql_query = """
                SELECT 
                question1_answer1_t,
                question2_answer1_t,
                question3_answer1_t,
                question4_answer1_t,
                question5_answer1_t,
                question6_answer1_t,
                question7_answer1_t,
                question8_answer1_t,
                question9_answer1_t,
                question10_answer1_t
                FROM
                answer WHERE question_id = %s;
            """

            cur.execute(sql_query, (QUESTION_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'CHECK_SCORE':
            USER_ID = data[0]
            QUESTION_ID = data[1]
            
            sql_query = """
                SELECT 
                *
                FROM
                quiz_history WHERE user_id = %s AND topic_id = %s;
            """

            cur.execute(sql_query, (USER_ID, QUESTION_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'GET_QUIZ_HISTORY':
            USER_ID = data[0]
            
            sql_query = """
                SELECT 
                qh.*,
                tp.topic_title
                FROM `quiz_history` as qh
                JOIN topic as tp ON qh.topic_id = tp.topic_id
                WHERE user_id = %s;
            """

            cur.execute(sql_query, (USER_ID,))
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            results_dicts = [dict(zip(column_names, result)) for result in results] if column_names and results else []
            cur.close()
            return results_dicts
        
        if query_type == 'CHECK_TAKEN_QUIZ':
            USER_ID = data[0]
            TOPIC_ID = data[1]
            
            sql_query = """
                SELECT * FROM quiz_history WHERE user_id = %s AND topic_id = %s;
            """

            cur.execute(sql_query, (USER_ID, TOPIC_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        
        if query_type == 'GET_ALL_USER':
            
            sql_query = """
                SELECT
                u.*,
                COALESCE(COUNT(qh.topic_id), 0) AS completed_topic
                FROM
                users u
                LEFT JOIN
                quiz_history qh ON u.user_id = qh.user_id
                GROUP BY
                u.user_id, u.user_username, u.user_password, u.user_name, u.user_email, u.account_status;

            """

            cur.execute(sql_query)
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            results_dicts = [dict(zip(column_names, result)) for result in results] if column_names and results else []
            cur.close()
            return results_dicts
        
        if query_type == 'GET_USER_PASSWORD':
            USER_ID = data[0]
            
            sql_query = """
                SELECT user_password FROM users where user_id = %s;
            """

            cur.execute(sql_query, (USER_ID,))
            result = cur.fetchone()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            result_dict = dict(zip(column_names, result)) if column_names and result else {}
            cur.close()
            return result_dict
        
        if query_type == 'GET_USER_REPORT':
            USER_ID = data[0]
            
            sql_query = """
                SELECT
                t.topic_id AS 'module_id',
                t.topic_title AS 'topic_title',
                COALESCE(qh.retake, 'None') AS 'retake',
                COALESCE(qh.score1, 'None') AS 'first_score',
                COALESCE(qh.score2, 'None') AS 'second_score',
                COALESCE(qh.quiz_status, 'Not Attempted') AS 'status',
                CASE WHEN qh.topic_id IS NOT NULL THEN 'Yes' ELSE 'No' END AS 'completed',
                COALESCE(qh.date_complete, 'None') AS 'completion_date'
                FROM
                topic t
                LEFT JOIN
                quiz_history qh ON t.topic_id = qh.topic_id AND qh.user_id = %s
                ORDER BY
                t.topic_id ASC;

            """
            cur.execute(sql_query, (USER_ID,))
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description] if cur.description else []
            results_dicts = [dict(zip(column_names, result)) for result in results] if column_names and results else []
            cur.close()
            return results_dicts
        
        if query_type == 'GET_COUNT_ALL_TOPIC':
            
            sql_query = """
                SELECT COUNT(*) as total_count FROM topic;
            """

            cur.execute(sql_query)
            result = cur.fetchone()
            cur.close()
            return result
        
        if query_type == 'GET_FULL_NAME':
            USER_ID = data[0]
            
            sql_query = """
                SELECT user_name FROM users WHERE user_id = %s;
            """

            cur.execute(sql_query, (USER_ID,))
            result = cur.fetchone()
            cur.close()
            return result
        
        
    def insert_data(self, query_type, data):
        cur = self.mysql.connection.cursor()

        if query_type == 'REGISTER':
            FULLNAME = data[0]
            USERNAME = data[1]
            EMAIL = data[2]
            PASSWORD = data[3]
            
            sql_query = """
            INSERT INTO users (user_name, user_username, user_email, user_password)
            VALUES (%s, %s, %s, %s);
            """
            cur.execute(sql_query, (FULLNAME, USERNAME, EMAIL, PASSWORD))
            self.mysql.connection.commit()
            cur.close()

        if query_type == 'REGISTER_ADMIN':
            USERNAME = data[0]
            EMAIL = data[1]
            PASSWORD = data[2]
            
            sql_query = """
            INSERT INTO admin (admin_username, admin_email, admin_password)
            VALUES (%s, %s, %s);
            """
            cur.execute(sql_query, (USERNAME, EMAIL, PASSWORD))
            self.mysql.connection.commit()
            cur.close()

        if query_type == 'ADD_TOPIC':
            TOPIC_TITLE = data[0]
            TOPIC_DESCRIPTION = data[1]
            TOPIC_LESSON = data[2]
            TOPIC_VIDEO = data[3]
            TOPIC_UPLOAD_DATE = data[4]
            TOPIC_REGISTER_BY = data[5]
            
            sql_query = """
            INSERT INTO topic (topic_title, topic_description, topic_lesson, topic_video, topic_upload_date, topic_register_by)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cur.execute(sql_query, (TOPIC_TITLE, TOPIC_DESCRIPTION, TOPIC_LESSON, TOPIC_VIDEO, TOPIC_UPLOAD_DATE, TOPIC_REGISTER_BY))
            self.mysql.connection.commit()
            cur.execute("SELECT LAST_INSERT_ID();")
            topic_id = cur.fetchone()[0]
            cur.close()
            return topic_id
        
        if query_type == 'ADD_QUESTION':
            TOPIC_ID = data[0]
            QUESTION_1 = data[1]
            QUESTION_2 = data[2]
            QUESTION_3 = data[3]
            QUESTION_4 = data[4]
            QUESTION_5 = data[5]
            QUESTION_6 = data[6]
            QUESTION_7 = data[7]
            QUESTION_8 = data[8]
            QUESTION_9 = data[9]
            QUESTION_10 = data[10]
            
            sql_query = """
            INSERT INTO question (topic_id, question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cur.execute(sql_query, (TOPIC_ID, QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, QUESTION_6, QUESTION_7, QUESTION_8, QUESTION_9, QUESTION_10))
            self.mysql.connection.commit()
            cur.execute("SELECT LAST_INSERT_ID();")
            question_id = cur.fetchone()[0]
            cur.close()
            return question_id
            
        
        if query_type == 'ADD_ANSWER':
            columns = ['question_id']
            answers = [data[0]]  
            for i in range(1, 11):  
                if i in range(1, 7):  # For multiple choice questions
                    for j in range(1, 5):  
                        index = (i-1)*4+j 
                        if index < len(data):
                            answers.append(data[index])
                            columns.append(f'question{i}_answer{j}_{"t" if j == 1 else "f"}')
                        else:
                            print(f"Index {index} is out of range for the data list.")
                else:  # For single answer questions
                    index = 24 + i - 6  # Adjust the index calculation for single answer questions
                    if index < len(data):
                        answers.append(data[index])
                        columns.append(f'question{i}_answer1_t')
                    else:
                        print(f"Index {index} is out of range for the data list.")

            sql_query = f"""
            INSERT INTO answer 
            ({', '.join(columns)})
            VALUES 
            ({', '.join(['%s'] * len(columns))});
            """
            cur.execute(sql_query, tuple(answers))
            self.mysql.connection.commit()
            cur.close()
            
        if query_type == 'ADD_SCORE1':
            USER_ID = data[0]
            TOPIC_ID = data[1]
            TIME_COMPLETE = data[2]
            DATE_COMPLETE = data[3]
            SCORE = data[4]
            RETAKE = data[5]
            RETAKE_TAKEN = data[6]
            
            if SCORE >= 8:
                QUIZ_STATUS = 'PASS'
            else:
                QUIZ_STATUS = 'FAIL'
            
            sql_query = """
            INSERT INTO quiz_history (user_id, topic_id, time_complete, date_complete, score1, quiz_status, retake, retake_taken)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cur.execute(sql_query, (USER_ID, TOPIC_ID, TIME_COMPLETE, DATE_COMPLETE, SCORE, QUIZ_STATUS, RETAKE, RETAKE_TAKEN))
            self.mysql.connection.commit()
            cur.close()
            
        if query_type == 'ADD_SCORE2':
            USER_ID = data[0]
            TOPIC_ID = data[1]
            TIME_COMPLETE = data[2]
            DATE_COMPLETE = data[3]
            NEW_SCORE = data[4]
            RETAKE = data[5]
            RETAKE_TAKEN = data[6]
            OLD_SCORE = data[7]
            
            if NEW_SCORE >= 8:
                QUIZ_STATUS = 'PASS'
            else:
                QUIZ_STATUS = 'FAIL'
            
            sql_query = """
            INSERT INTO quiz_history (user_id, topic_id, time_complete, date_complete, score2, quiz_status, retake, retake_taken, score1)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cur.execute(sql_query, (USER_ID, TOPIC_ID, TIME_COMPLETE, DATE_COMPLETE, NEW_SCORE, QUIZ_STATUS, RETAKE, RETAKE_TAKEN, OLD_SCORE))
            self.mysql.connection.commit()
            cur.close()
             
    def update_data(self, query_type, data):
        cur = self.mysql.connection.cursor()
        
        if query_type == 'EDIT_TOPIC':
            TOPIC_ID = data[0]
            TOPIC_TITLE = data[1]
            TOPIC_DESCRIPTION = data[2]
            TOPIC_LESSON = data[3]
            TOPIC_VIDEO = data[4]
            TOPIC_UPLOAD_DATE = data[5]
            TOPIC_REGISTER_BY = data[6]
            POPUP_QUESTION = data[7]
            POPUP_ANSWER = data[8]

            sql_query = """
            UPDATE topic 
            SET topic_title = %s, topic_description = %s, topic_lesson = %s, topic_video = %s, topic_upload_date = %s, topic_register_by = %s, popup_question = %s, popup_answer = %s
            WHERE topic_id = %s;
            """
            cur.execute(sql_query, (TOPIC_TITLE, TOPIC_DESCRIPTION, TOPIC_LESSON, TOPIC_VIDEO, TOPIC_UPLOAD_DATE, TOPIC_REGISTER_BY, POPUP_QUESTION, POPUP_ANSWER, TOPIC_ID))
            self.mysql.connection.commit()
            cur.close()
        
        if query_type == 'EDIT_QUESTION':
            QUESTION_ID = data[0]
            QUESTION_1 = data[1]
            QUESTION_2 = data[2]
            QUESTION_3 = data[3]
            QUESTION_4 = data[4]
            QUESTION_5 = data[5]
            QUESTION_6 = data[6]
            QUESTION_7 = data[7]
            QUESTION_8 = data[8]
            QUESTION_9 = data[9]
            QUESTION_10 = data[10]

            sql_query = """
            UPDATE question 
            SET  question_1 = %s, question_2 = %s, question_3 = %s, question_4 = %s, question_5 = %s, question_6 = %s, question_7 = %s, question_8 = %s, question_9 = %s, question_10 = %s
            WHERE question_id = %s;
            """
            cur.execute(sql_query, (QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, QUESTION_6, QUESTION_7, QUESTION_8, QUESTION_9, QUESTION_10, QUESTION_ID))
            self.mysql.connection.commit()
            cur.close()
            return QUESTION_ID
        
        if query_type == 'EDIT_ANSWER':
            data_list = list(data)

            # Remove the first element and append it to the end
            first_element = data_list.pop(0)
            data_list.append(first_element)
            ANSWER_ID = data[0]
            columns = ['question_id']
            answers = [data[1]]  
            for i in range(1, 11):  
                if i in range(1, 7):  # For multiple choice questions
                    for j in range(1, 5):  
                        index = (i-1)*4+j 
                        if index < len(data):
                            answers.append(data[index])
                            columns.append(f'question{i}_answer{j}_{"t" if j == 1 else "f"}')
                        else:
                            print(f"Index {index} is out of range for the data list.")
                else:  # For single answer questions
                    index = 24 + (i - 7)  # Adjust the index calculation for single answer questions
                    if index < len(data):
                        answers.append(data[index])
                        columns.append(f'question{i}_answer1_t')
                    else:
                        print(f"Index {index} is out of range for the data list.")
            
            set_clause = ', '.join(f'{column} = %s' for column in columns)
            sql_query = f"""
            UPDATE answer 
            SET 
            {set_clause}
            WHERE answer_id = %s;
            """

            answers.append(ANSWER_ID)
            cur.execute(sql_query, tuple(data_list))
            self.mysql.connection.commit()
            cur.close()
        
        if query_type == 'EDIT_USER':
            USER_ID = data[0]
            USER_FULLNAME = data[1]
            USERNAME = data[2]
            USER_EMAIL = data[3]
            PASSWORD = data[4]
   
            sql_query = """
            UPDATE users 
            SET 
            user_username = %s, 
            user_email = %s, 
            user_password = %s, 
            user_name = %s
            WHERE user_id = %s;
            """
            cur.execute(sql_query, (USERNAME, USER_EMAIL, PASSWORD, USER_FULLNAME, USER_ID))
            self.mysql.connection.commit()
            cur.close()
        
        if query_type == 'USER_ACCOUNT_STATUS':
            USER_ID = data[0]
            STATUS =  data[1]
   
            sql_query = """
            UPDATE users 
            SET 
            account_status = %s
            WHERE user_id = %s;
            """
            cur.execute(sql_query, (STATUS, USER_ID))
            self.mysql.connection.commit()
            cur.close()
            
                
    def delete_data(self, query_type, data):
        cur = self.mysql.connection.cursor()
        
        if query_type == 'DELETE_DATA':
            USER_ID = data[0]
            TOPIC_ID = data[1]
            
            sql_query = """
            DELETE FROM quiz_history WHERE user_id = %s AND topic_id = %s;
            """
            cur.execute(sql_query, (USER_ID, TOPIC_ID))
            self.mysql.connection.commit()
            cur.close()
            
        if query_type == 'DELETE_TOPIC':
            TOPIC_ID = data[0]
            
            sql_query = """
            DELETE FROM topic WHERE topic_id = %s;
            """
            cur.execute(sql_query, (TOPIC_ID,))
            self.mysql.connection.commit()
            cur.close()
        
        if query_type == 'DELETE_QUESTION':
            QUESTION_ID = data[0]
            
            sql_query = """
            DELETE FROM question WHERE question_id = %s;
            """
            cur.execute(sql_query, (QUESTION_ID,))
            self.mysql.connection.commit()
            cur.close()
            
        if query_type == 'DELETE_ANSWER':
            ANSWER_ID = data[0]
            
            sql_query = """
            DELETE FROM answer WHERE answer_id = %s;
            """
            cur.execute(sql_query, (ANSWER_ID,))
            self.mysql.connection.commit()
            cur.close()
            
        if query_type == 'DELETE_USER':
            USER_ID = data[0]
            
            sql_query = """
            DELETE FROM users WHERE user_id = %s;
            """
            cur.execute(sql_query, (USER_ID,))
            self.mysql.connection.commit()
            cur.close()
        
        