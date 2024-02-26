# crawling

import mysql
import mysql.connector
from random import randint
from datetime import datetime
import sensitive

def get_user_posts(username):
    mydb = get_database()

    cursor = mydb.cursor()
    statmt = "select * FROM posts WHERE username = %s"
    cursor.execute(statmt, (username,))
    posts = []

    for item in cursor:
        if (item[4] == username):
            posts.append(item)
    return posts

def get_database():
    return mysql.connector.connect(
        host=sensitive.get_server_name(),
        # localhost or 192.168.0.26 for remote in home
        user="doadmin",
        password=sensitive.get_server_password(),
        database="collec",
        port=25060
    )


def custom_post_id():
    post_id = randint(100000000000000, 999999999999999)

    mydb = get_database()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM posts")

    for item in cursor:
        if item[2] == post_id:
            post_id = randint(100000000000000, 999999999999999)

    return int(post_id)


def create_post(community, post_title, username, details, visibility, catagory, off_name, origin_country,
                date_created, value):
    mydb = get_database()

    public = "public"

    id_num = custom_post_id()
    photo_name = str(id_num) + ".jpg"

    post_type = "post"

    if off_name != "no data" or origin_country != "no data" or date_created != "no data" or value != "no data":
        post_type = "entry"

    if community == "Choose Community":
        community = "No Community"

    mycursor = mydb.cursor()
    mycursor.execute('''

            INSERT INTO posts
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, %s);

        ''', (
        photo_name, community, id_num, post_title, username, details, post_type, visibility, catagory, off_name,
        origin_country,
        date_created, value, public, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    mydb.commit()

    return id_num