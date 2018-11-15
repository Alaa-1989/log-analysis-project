# Logs Analysis Project
   This project is for a newspaper site, we've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
   The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

## For who do i make it
   This project has been developed for Udacity to complete a Full Stack Web Developer Nanodegree.


## Tasks
   The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, we use "PostgreSQL" database, and use SQL queries to analyze the log data, and print out the answers to some questions.

### what are we reporting
   we answers in this project these three questions by this output specifications:
- What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    ##### Example:
          "Princess Shellfish Marries Prince Handsome" — 1201 views
          "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
          "Political Scandal Ends In Political Scandal" — 553 views


- Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

     ##### Example:
          Ursula La Multa — 2304 views
          Rudolf von Treppenwitz — 1985 views
          Markoff Chaney — 1723 views
          Anonymous Contributor — 1023 views

- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes) .

     ##### Example:
          July 29, 2016 — 2.5% errors

## Requirements
- Python 3.7.1
- vagrant 2.2.0
- Git bash  - _for Windows OS_
- Download the database file **newsdata.sql** from [here](https://up.top4top.net/downloadf-1048ta2w51-zip.html)
- PostgreSQL database
- psycopg2
- pycodestyle-2.4.0


## How to Run
#### The virtual machine
   To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze, so install the virtual machine.
   If you need to bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.

#### Newsdata database file
   You will need to unzip file newsdata after downloading it. The file inside is called newsdata.sql , Put this file into the vagrant directory, which is shared with your virtual machine.

   To build the reporting tool, you'll need to load the site's data into your local database.

   To load the data, `cd` into the `vagrant` directory and use the command.

`psql -d news -f newsdata.sql`

**Here's what this command does:**
- `psql` — the PostgreSQL command line program
- `-d`  news — connect to the database named news which has been set up for you
- `-f` newsdata.sql — run the SQL statements in the file newsdata.sql

   Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

#### psycopg2
   In your python code you need to import psycopg2 library and you need to install the package from the terminal/git bash if you have not yet:

**Run this code in your terminal**

`pip3 install psycopg2`



**This from my git bash after run the command to install psycopg2**

#### pycodestyle-2.4.0
   **Python	code:**  The code conforms to the PEP8 style recommendations.
   You can install the pycodestyle tool to test this, with `pip install pycodestyle` or `pip3 install pycodestyle` (Python 3).
   Use	a	style	standard	to	test	your	python	code	quality	like	**“pycodestyle”**.	Your	code	should	pass	the	style	standard	with	0	errors.

**Run this code in your terminal**

`pip3 install pycodestyle `


**This picture from  my git bash after run the command for PEP8 style to installed it**

## Notes
you will find a comments in the code file  after this char ` # ` described each command uses.

## Author

**Alaa Alaboud** - _GitHub Profile:_ [Alaa-1989](https://github.com/Alaa-1989)

## License

Licensed under the MIT License.
