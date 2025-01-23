from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="AIML_LIB",
        user="postgres",
        password="Khedkar@123",
        host="localhost",
        port="5432"
    )
    return conn

# Home route: Display books
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Books')  # Fetch all books
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('books.html', books=books)

# Request a book
@app.route('/request_book', methods=['POST'])
def request_book():
    student_name = request.form['student_name']
    prn = int(request.form['prn'])
    book_id = int(request.form['book_id'])  # Book ID from dropdown

    conn = get_db_connection()
    cur = conn.cursor()

    # Insert the book request
    cur.execute(
        'INSERT INTO RequestBook (StudentName, PRN, Book_ID) VALUES (%s, %s, %s)',
        (student_name, prn, book_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/requests')

# View all requests with book details
@app.route('/requests')
def view_requests():
    conn = get_db_connection()
    cur = conn.cursor()

    # Join RequestBook with Books to fetch detailed data
    cur.execute('''
        SELECT 
            r.Request_ID, r.StudentName, r.PRN, b.Book_Name, b.Author 
        FROM 
            RequestBook r
        INNER JOIN 
            Books b
        ON 
            r.Book_ID = b.Book_ID
    ''')
    requests = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('requests.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True)
