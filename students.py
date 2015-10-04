from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length = 255, unique = True)
    points = IntegerField(default = 0)

    class Meta:
        ''' Class inside of a class. Describing the class it belongs to'''
        # Set database to the one defined
        database = db

students = [
    {'username': 'kevingann',
    'points': 666},
    {'username': 'username2',
    'points': 555},
    {'username': 'username3',
    'points': 444},
    {'username': 'username4',
    'points': 333}
]

def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                        points=student['points'])
        except IntegrityError:
            student_record = Student.get(username = student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


# If file is name is run directly and not imported.
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe = True)
    add_students()
    print("Top student! {0.username}".format(top_student()))


# Notes!
# model - A code object that represents a database table
# SqliteDatabase - The class from Peewee that lets us connect to an SQLite database
# Model - The Peewee class that we extend to make a model
# CharField - A Peewee field that holds onto characters. It's a varchar in SQL terms
# max_length - The maximum number of characters in a CharField
# IntegerField - A Peewee field that holds an integer
# default - A default value for the field if one isn't provided
# unique - Whether the value in the field can be repeated in the table
# .connect() - A database method that connects to the database
# .create_tables() - A database method to create the tables for the specified models.
# safe - Whether or not to throw errors if the table(s) you're attempting to create already exist

# .create() - creates a new instance all at once
# .select() - finds records in a table
# .save() - updates an existing row in the database
# .get() - finds a single record in a table
# .delete_instance() - deletes a single record from the table
# .order_by() - specify how to sort the records
# if __name__ == '__main__' - a common pattern for making code only run with the script is run and not when it's imported
# db.close() - not a method we used, but often a good idea. Explicitly closes the connection to the database.
# .update() - also something we didn't use. Offers a way to update a record without .get() and .save(). Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()



# sqlite3 students.db
# SQLite version 3.8.5 2014-08-15 22:37:57
# Enter ".help" for usage hints.
# sqlite> select * from student;
# sqlite> .tables
# student
# sqlite> .exit
