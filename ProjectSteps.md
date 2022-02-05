1. Create a project folder called TNP-AZURE-APIM
2. Create a python virtual environment - venv
3. Upgrade the pip of venv by "python -m pip install --upgrade pip"
4. Activate the venv by venv\Scripts\activate.bat
5. Install flask in venv as framework to build RESTful API by "pip install Flask"
6. Capture python dependencies into requirements.txt by "pip freeze > requirements.txt"
7. Create a app.py file for main RESTful API start.
8. Build the RESTful API using Flask Framework
9. Set the FLASK_APP env variable by "set FLASK_APP=app"
10. Run the WSGi Server for Flask RESTful API by "flask run" - Starts the dev server
11. As soon as server starts, test the API using Postman collection