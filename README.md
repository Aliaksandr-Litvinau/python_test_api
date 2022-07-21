# python_test_api

### url: https://stores-tests-api.herokuapp.com

### How to start (use python 3.9 + create and activate virtual environments)
- python3.9 -m venv env
- source env/bin/activate
- pip install -r requirements.txt

### Run all tests
- pytest

### Allure integration with pytest  
- download the latest allure package tgz or zip file from the allure-framework [GitHub repo](https://github.com/allure-framework/allure2/releases)
- unzip the downloaded tgz or zip file
- copy the path till bin
- add it to the path environment variable

### Open your terminal and run
- allure --version   
(If you see the allure version printed then your setup is successful!!)

### Generating Allure report using pytest  
In your project directory, you first need to generate a folder to save the allure reports, you can automatically generate this with a command
- allure generate  
This will create a folder named allure-report in your project directory.

### You are now set to run your test with pytest runner by specifying the directory path to save your allure report, for example :
- pytest --alluredir=allure_report  
Once test execution completes, all the test results would get stored in allure-report directory.  

### You can now view the allure-report in the browser with the command –
- allure serve allure_report  

This will open up the report in your default browser automatically and would look like  

![alt text](https://qxf2.com/blog/wp-content/uploads/2021/07/allure-browser.png) 
