# IFSC DETAILER

IFSC Detailer is a webapp which can be used to find some of the details of any bank by entering the corresponding IFSC Code.

## Instructions

1. Get the source code on your pc via git and navigate inside the folder through your terminal.

```
  git clone https://github.com/altruistcoder/
```
2. Create a virtual environment and navigate inside it.

```
  virtualenv venv
```
3. Move the contents of cloned repository inside virtual environment folder.

4. Activate the virtual environment (You have to activate it everytime you are working on project).

```
  For mac users:

    source bin/activate  

  For windows users:

    .\Scripts\activate
```

5. Now, install python dependencies.

```
  pip install -r requirements.txt
```
6. Now, navigate to the directory containing manage.py file.

7. Run following command:

```
  python manage.py migrate
  python manage.py runserver
```
8. That's it, IFSC Detailer is ready. You can run it at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).