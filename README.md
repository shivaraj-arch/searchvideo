# searchvideo

This is a simple search in video application using ccextractor, celery and django.
Please install python3, ccextractor , celery, rabbitmq and django before the following
To run this example:  

1. Clone the repository::  

     git clone https://github.com/tdsgit/searchvideo.git   
     cd searchvideo   

2. Create and activate a virtual environment ( if needed )::

     virtualenv env    
     source env/bin/activate   

3. Install requirements::   
     
     pip3 install -r 'requirements.txt'    

<<<<<<< HEAD
4. Run the application::  
     start message broker: rabbitmq-server    
     start celery : celery -A searchinvideo worker -l INFO -settings=celeryconfig    
     python3 makemigrations srt   
     python3 migrate   
     python3 manage.py runserver   
    
5. open localhost:8000/search_subtitle/ on browser and     
     Please place video and update location file_path in srt/proj/srtparse.py     
     Enter:    
     Search text : text to search in video   
     Av name : video name #not the path   
     Click on Submit    
=======
4. Run the application::

     python3 makemigrations srt  
     python3 migrate  
     python3 manage.py runserver   
    
5. open localhost:8000/search_subtitle/ on browser and    
     Please place video and update location file_path in srt/proj/srtparse.py   
     Enter:   
     Search text : text to search in video  
     Av name : video name #not the path  
     Click on Submit  
>>>>>>> 921b98e1f65bb28091155e4d410f4d2e203ff1b6
