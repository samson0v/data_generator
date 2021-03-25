# CSVFaker

## Installation and start up
1. Clone GitHub repository
2. Make virtual environment
3. Create your own .env file (you can use .env.example)
4. Download all pip packages fom requirements.txt
5. Make migrations
6. Run server

## Quick Guide
To create your fake data, firstly you have to login or sign up,
the next thing you must to do is create new Schema (go to http://127.0.0.1:8000/generator/create-schema/).
There you can create column in CVS file that include:
1. Column name
2. Column type (7 types)
3. From (for integer field)
4. To (for integer field)
5. Order

After filling out all fields, click on Create button and you will redirect to 
Schema List page.
The next thing is create new Data Set, so click on Schema name, you will
redirect to DataSet page, on top part of the page you will see form, there are:
1. Rows number
2. Create button

Fill out rows number field and click Generate button. Check status for CREATED
and appearing Download button, if they are, 🎉congratulations🎉, you have your
 fake data.