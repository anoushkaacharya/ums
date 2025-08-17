# University-Management-System

"University Management System" is a website with main goal to inculcate technology in the process of managing University data and activites. "UMS" is a platform where the students can access their academic information and interact with faculty in order to streamline the daily activities of an educational institute.<br>
The project consists of multiple subsystems -
1. Academic Information Delivery System
2. Assignment Creation and Submission
3. Grading System
4. Admin Section(For managing students, faculty, courses and departments)


This project is developed by-
Anoushka Aditi Acharya <br>
Honey <br>
Smrutishree <br>
<hr>

 

> Note for every id field

      user-id = 1
      password = 1234
      
Link for Instruction Manual: [Instruction Manual](https://github.com/ronnie-36/University-Management-System/blob/main/documents/Instruction-manual-P012_190001011_190001029_190001030_190001049.pdf)

# Steps To Install 

## Installing Requirements  
      1. Mysql (preferably use Mysql Workbench 8.0)  
      
      2. Python 3.8 / 3.7 / 3.6 ( Not compatible with python 3.9 )  
 <br ><br ><br > 

## STEP 1  (CLONING AND SETTING ENVIRONMENT VARIABLES)
      1. Clone this project 
      
      2. Create a .env file similar to .env.example file and populate variables in it.

      > MAIL_USERNAME and MAIL_PASSWORD fields in .env file should contain a GOOGLE Email ID and its password required for forgot password feature in authentication    
<br ><br ><br >
  


### MANUAL  

      if possible use venv

      pip install -r requirements.txt

      Ensure you have created db.yaml, .env and imported mysql 

      Run the application by executing the command python app.py

      Use python 3.7 u

      The application runs on localhost:5000

#### Libraries used 
  
      unittest
      flask_testing
      

#### STEPS: 

    pip install -r requirements.txt
    python test.py



## Contributions
Contributions are encouraged. If you want to contribute then follow these steps:
1. Fork this repository and make a copy of your own .
2. Follow the steps given in Steps To Install to clone from forked repo and set up the project
3. Make changes to the project
4. Always remember to pull before you commit
5. Commit final changes to forked repository
6. Create a pull request and if contributors agree then your code will be merged with the main repository
