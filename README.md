# GLIF Website Project
Website for academic association GLIF of Sungkyunkwan Univ. at Seoul, South Korea.
 
## Project Introduction
![main](./screenshots/main.png)
This Project aims to build communication channel for GLIFers.
This Project was built using Python Django Project, and plan to provide:
- Introduction of GLIF
- Session Materials
 
## Quick Start
  
### Activate Virtual Environment
set current directory as this git repo, GLIF_Website_Project.
1. Create venv:
```
python -n venv .venv
```
This command will create a virtual environment with dirname '.venv'

2.  Collect Dependencies. Dependencies are listed in **requirements.txt**, so following command will do necessary tasks.
```
pip install -r requirements.txt
```

3. activate
activate using command:
```
$ source .venv/Scripts/activate
(.venv) $ 
```

### Run the server
In virtual environment, send the command:
```
(.venv) $ python manage.py runserver
```

And this command will render pages as follows:
```
(.venv) (base) dongmin@dongmin-ThinkPad-E495:~/Projects/GLIF_Website_Project$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 3 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth.
Run 'python manage.py migrate' to apply them.
May 20, 2021 - 01:37:00
Django version 3.1.3, using settings 'website.settings'
Starting development server at http://127.0.0.1:8000/
```