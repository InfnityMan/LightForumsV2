import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='lightForums',
    port=3306
)

cursor = mydb.cursor()


def add_thread(author, title, content):
    # SQL Query
    command = 'insert into threads(author, title, content) values(%s, %s, %s)'

    # Parameters
    values = (author, title, content)

    # Add Thread to Database
    cursor.execute(command, values)
    mydb.commit()


def add_comment(thread_id, author, content):
    # Inserting the Comment
    insert_command = 'insert into comments(threadID, author, content) values (%s, %s, %s)'
    insert_values = (thread_id, author, content)
    cursor.execute(insert_command, insert_values)
    mydb.commit()

    # Updating the Number of Comments
    update_command = 'update threads set comment_count = comment_count + 1 where id = %s'
    update_values = (thread_id,)
    cursor.execute(update_command, update_values)
    mydb.commit()

    return show_thread(thread_id)


def show_all_threads():
    # SQL Query
    command = 'select * from threads order by creationDate desc'

    # Parameters
    cursor.execute(command)

    # Result
    result = cursor.fetchall()
    threads = {}

    # Data that Will be Sent to the Website
    for thread in result:
        print(thread)
        threads[thread[0]] = {'user': thread[1], 'title': thread[4], 'creationDate': thread[2], 'content': thread[3], 'comments': thread[5]}

    print(threads)
    return threads


def show_thread(thread_id):
    # SQL Queries
    thread_command = 'select * from threads where id = %s'
    comment_command = 'select * from comments where threadID = %s order by creationDate desc'

    # SQL Query Parameters
    thread_value = (thread_id,)
    comment_value = (thread_id,)

    # Fetches Threads
    cursor.execute(thread_command, thread_value)
    thread_result = cursor.fetchone()

    # Fetches Comments
    cursor.execute(comment_command, comment_value)
    comment_result = cursor.fetchall()

    # Data that Will be Sent to the Website
    comments = {}
    for comment in comment_result:
        comments[comment[0]] = {
            'threadID': comment[1],
            'user': comment[2],
            'creationDate': comment[3],
            'content': comment[4]
        }

    thread = {
        'id': thread_id,
        'user': thread_result[1],
        'title': thread_result[4],
        'creationDate': thread_result[2],
        'content': thread_result[3],
        'comment_count': thread_result[5],
        'comments': comments
    }
    return thread


def add_account(username, password):
    # SQL Query
    command = 'insert into accounts(userName, userPassword) values(%s, %s)'

    # Parameters
    values = (username, password)

    # Command Execution
    cursor.execute(command, values)
    mydb.commit()


def login(username, password):
    # SQL Query
    command = 'select * from accounts where username LIKE %s and userPassword LIKE %s'

    # Parameters
    values = (username, password)

    # Command Execution
    cursor.execute(command, values)
    result = cursor.fetchall()

    # Makes Sure There is an Account with the Correct Details
    if not result == []:
        return result[0]


def add_question(author, title, content, num_answers, num_likes):
    # SQL Query
    command = 'insert into questions(author, title, content, num_answers, num_likes) values(%s, %s, %s, %s, %s)'

    # Parameters
    values = (author, title, content, num_answers, num_likes)

    # Command Execution
    cursor.execute(command, values)
    mydb.commit()

