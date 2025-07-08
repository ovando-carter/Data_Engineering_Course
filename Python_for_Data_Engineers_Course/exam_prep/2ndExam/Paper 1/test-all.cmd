@echo off
REM This script runs all the test scripts

REM Messages for each Return Code
set RC0=Passed all tests
set RC1=FAILED unit testing!!
set RC2=FAILED : .py file not found
set RC3=FAILED : function not found in .py file
set RC4=FAILED : Import failed (probably due to syntax errors)

REM Header
echo ===================================================  > python-%USERNAME%.txt
echo Python TEST for: %USERNAME%                         >> python-%USERNAME%.txt
echo =================================================== >> python-%USERNAME%.txt
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >> python-%USERNAME%.txt

REM Run Q1 unit tests
echo ========================================
echo Running tests for question 1:
python q1-test.py
if %ERRORLEVEL%==0 echo Q1 : %RC0% >> python-%USERNAME%.txt
if %ERRORLEVEL%==1 echo Q1 : %RC1% >> python-%USERNAME%.txt
if %ERRORLEVEL%==2 echo Q1 : %RC2% >> python-%USERNAME%.txt
if %ERRORLEVEL%==3 echo Q1 : %RC3% >> python-%USERNAME%.txt
if %ERRORLEVEL%==4 echo Q1 : %RC4% >> python-%USERNAME%.txt

REM Run Q2 unit tests
echo ========================================
echo Running tests for question 2:
python q2-test.py
if %ERRORLEVEL%==0 echo Q2 : %RC0% >> python-%USERNAME%.txt
if %ERRORLEVEL%==1 echo Q2 : %RC1% >> python-%USERNAME%.txt
if %ERRORLEVEL%==2 echo Q2 : %RC2% >> python-%USERNAME%.txt
if %ERRORLEVEL%==3 echo Q2 : %RC3% >> python-%USERNAME%.txt
if %ERRORLEVEL%==4 echo Q2 : %RC4% >> python-%USERNAME%.txt

REM Run Q3 unit tests
echo ========================================
echo Running tests for question 3:
python q3-test.py
if %ERRORLEVEL%==0 echo Q3 : %RC0% >> python-%USERNAME%.txt
if %ERRORLEVEL%==1 echo Q3 : %RC1% >> python-%USERNAME%.txt
if %ERRORLEVEL%==2 echo Q3 : %RC2% >> python-%USERNAME%.txt
if %ERRORLEVEL%==3 echo Q3 : %RC3% >> python-%USERNAME%.txt
if %ERRORLEVEL%==4 echo Q3 : %RC4% >> python-%USERNAME%.txt

REM Run Q4 unit tests
echo ========================================
echo Running tests for question 4:
python q4-test.py
if %ERRORLEVEL%==0 echo Q4 : %RC0% >> python-%USERNAME%.txt
if %ERRORLEVEL%==1 echo Q4 : %RC1% >> python-%USERNAME%.txt
if %ERRORLEVEL%==2 echo Q4 : %RC2% >> python-%USERNAME%.txt
if %ERRORLEVEL%==3 echo Q4 : %RC3% >> python-%USERNAME%.txt
if %ERRORLEVEL%==4 echo Q4 : %RC4% >> python-%USERNAME%.txt

REM Run Q5 unit tests
echo ========================================
echo Running tests for question 5:
python q5-test.py
if %ERRORLEVEL%==0 echo Q5 : %RC0% >> python-%USERNAME%.txt
if %ERRORLEVEL%==1 echo Q5 : %RC1% >> python-%USERNAME%.txt
if %ERRORLEVEL%==2 echo Q5 : %RC2% >> python-%USERNAME%.txt
if %ERRORLEVEL%==3 echo Q5 : %RC3% >> python-%USERNAME%.txt
if %ERRORLEVEL%==4 echo Q5 : %RC4% >> python-%USERNAME%.txt

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ >> python-%USERNAME%.txt

REM Add the Q1 code to the test file
echo ============================================================= >> python-%USERNAME%.txt
echo Question 1                                                    >> python-%USERNAME%.txt
echo ------------------------------------------------------------- >> python-%USERNAME%.txt
type q1.py >> python-%USERNAME%.txt
@echo:     >> python-%USERNAME%.txt

REM Add the Q2 code to the test file
echo ============================================================= >> python-%USERNAME%.txt
echo Question 2                                                    >> python-%USERNAME%.txt
echo ------------------------------------------------------------- >> python-%USERNAME%.txt
type q2.py >> python-%USERNAME%.txt
@echo:     >> python-%USERNAME%.txt

REM Add the Q3 code to the test file
echo ============================================================= >> python-%USERNAME%.txt
echo Question 3                                                    >> python-%USERNAME%.txt
echo ------------------------------------------------------------- >> python-%USERNAME%.txt
type q3.py >> python-%USERNAME%.txt
@echo:     >> python-%USERNAME%.txt

REM Add the Q4 code to the test file
echo ============================================================= >> python-%USERNAME%.txt
echo Question 4                                                    >> python-%USERNAME%.txt
echo ------------------------------------------------------------- >> python-%USERNAME%.txt
type q4.py >> python-%USERNAME%.txt
@echo:     >> python-%USERNAME%.txt

REM Add the Q5 code to the test file
echo ============================================================= >> python-%USERNAME%.txt
echo Question 5                                                    >> python-%USERNAME%.txt
echo ------------------------------------------------------------- >> python-%USERNAME%.txt
type q5.py >> python-%USERNAME%.txt
@echo:     >> python-%USERNAME%.txt

REM End of output
echo =================================================== >> python-%USERNAME%.txt
