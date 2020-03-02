Test execution : 

pytest TestLogin.py

pytest --junitxml=junitResult.xml TestLogin.py

pytest --html=report.html TestLogin.py. //This will work only if pytest-html installed

pytest -n 3 --html=report.html TestLogin.py

pytest -n 3 --rerun 2 --html=report.html TestLogin.py
