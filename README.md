# marlow_navigation

Code implementation of UI Selenium Test from Marlow Navigation

Prerequisites:

    Chrome
    
    Python3.x (I have Python 3.8.6 in my MacOS and Windows)
 
    If Python3.x is installed in Windows, please set enviroment variables 
    C:\set PATH=python_installed_directory\Python_version;%PATH%
    C:\set PYTHONPATH=%PYTHONPATH%;
    C:\set PATH=python_installed_directory\Python_version\Scripts\;%PATH%

   Please check this link for more detail: https://docs.python.org/3/using/windows.html    
    
1. Installation and Execution

      git clone https://github.com/bttiato/marlow_navigation.git

      cd marlow_navigation
      
      python3 -m venv venv (if python2.x and python3.x installed ) 
      or python -m venv venv (if only python3.x installed)
      
      - On MacOS/Linux
            source venv/bin/activate 
                   
      - On Windows
            venv\Scripts\activate 

       pip3 install -r requirements.txt

  To run the test, use command:
  
  - On Mac/Linux:
  
        python test/test_product_price.py' (if only python3.x running)
        
        or python3 test/test_product_price.py (if python2.x and python3.x
         running)
         
  - On Windows:
  
        python test\test_product_price.py (if only python3.x running)

After finishing test execution, deactivate venv by using command: deactivate

2. Notes

    - Document of Code Design, Implementation, Test Execution, and  Test Result is specified in file marlow_navigation/Test_Implementation_Design.docx

    - To run the test with headless mode: Go to marlow_navigation/config/input.conf, edit 'headless: 1'

    - Data-driven test: to add/modify parameterized data for testing, edit file marlow_navigation/data/data.csv

    - The test execution was verified on both MacOS and Windows 10

