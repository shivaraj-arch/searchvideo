# searchvideo

This is a simple search in video application using ccextractor, celery and django.
To run this example:

1. Clone the repository::

     git clone https://github.com/tdsgit/searchvideo.git  
     cd searchvideo

2. Create and activate a virtual environment::

     virtualenv env  
     source env/bin/activate 

3. Install requirements::  
     
     pip3 install -r 'requirements.txt'  

4. Run the application::

     python3 makemigrations srt
     python3 migrate
     python3 manage.py runserver
    
5. open localhost:8000/search_subtitle/ on browser and    
     Please place video and update location file_path in srt/proj/srtparse.py 
     Enter:
     Search text : <text to search in video>
     Av name : <video name> not the path
     Click on Submit
