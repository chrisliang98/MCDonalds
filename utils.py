import sqlite3
import md5;
import re;

#this is input sanitizing 
def sanitize(input):
    return re.sub('"', "  ", input)

#hashes and salts the pasword for permanent storage or retrieval
#returns hashed password
def encrypt(username,password):
    m = md5.new()
    m.update(username+password)
    return m.hexdigest()

#returns a boolean that describes whether the user has succesfully logged in.
def authenticate(username, password):
    username = sanitize(username)
    conn = sqlite3.connect("myDataBase.db")
    c = conn.cursor()
    ans = c.execute('select * from logins where username = "'+username+'" and password = "'+encrypt(username,password)+'";') 
    for r in ans:
        return True;
    return False;

#creates new user and adds to database
#return boolean whether the account has been created
def newUser(username,password):
    username = sanitize(username)
    conn = sqlite3.connect("myDataBase.db")
    c = conn.cursor()
    ans = c.execute('select * from logins where username = "%s";' % username)
    for r in ans:
        return False
    ans = c.execute('insert into logins values("'+username+'","'+encrypt(username,password)+'");')
    conn.commit()
    return True
