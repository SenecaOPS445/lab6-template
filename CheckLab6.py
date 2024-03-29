#!/usr/bin/env python3
'''
Name: CheckLab6.py
Updated: October 26, 2019 by Raymond Chan
Reasons: (1) updated for python version 3.6.8
         (2) add report header with user and system information
         (3) add checking for author id for lab scripts
Usage:
Check all sections for the lab 6
./CheckLab6.py -f -v
Check a specific lab section
./CheckLab6.py -f -v lab6x -- x: a

Description:
This script is used to give students more feedback and hints while working
on Lab 6. Python scripts for Lab 6 and this script should be in the same 
directory. All the Python scripts must use the correct naming scheme.
'''

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request
import socket
import time

class lab6a(unittest.TestCase):
    """All test cases for lab6a - sets"""
    
    def test_0(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - Test for file creation: ./lab6a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab6a.py'), msg=error_output)

    def test_a(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating a Class - Test for errors running: ./lab6a.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab6a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - Test for correct shebang line: ./lab6a.py"""
        lab_file = open('./lab6a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_instantiate_class_0(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - instantiating object with 0 arguments fails"""
        with self.assertRaises(Exception) as context:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student()

    def test_a_instantiate_class_1(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - instantiating object with 1 arguments fails"""
        with self.assertRaises(Exception) as context:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John')

    def test_b1_displayStudent(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayStudent() provides the correct output"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: displayStudent() does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '013454900')
            string1 = student.displayStudent()
        except:
            self.fail(error_fail)
        answer = 'Student Name: John\nStudent Number: 013454900'
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_b2_displayStudent(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayStudent() does not fail if self.number is an integer"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: make sure the displayStudent() does not fail when self.number is an integer)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', 12345)
            string1 = student.displayStudent()
        except:
            self.fail(error_fail)
        answer = 'Student Name: John\nStudent Number: 12345'
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_c_displayStudent(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayStudent() does not fail if self.number is an integer"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: make sure the displayStudent() does not fail when self.number is an integer)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', 543210)
            string1 = student.displayStudent()
        except:
            self.fail(error_fail)
        answer = 'Student Name: John\nStudent Number: 543210'
        self.assertEqual(string1, answer, msg=error_output)

    def test_d_displayGPA(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayGPA() provides the correct output"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            student.addGrade('uli101', 4.0)
            student.addGrade('ipc144', 4.0)
            string1 = student.displayGPA()
        except:
            self.fail(error_fail)
        answer = 'GPA of student John is 4.0'
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_e_displayGPA(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayGPA() handles ZeroDivisionError successfully"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            string1 = student.displayGPA()
        except:
            self.fail(error_fail)
        answer = 'GPA of student John is 0.0'
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_f_displayGPA(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayGPA() handles ZeroDivisionError successfully"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            student.addGrade('uli101', 0.0)
            student.addGrade('ipc144', 0.0)
            string1 = student.displayGPA()
        except:
            self.fail(error_fail)
        answer = 'GPA of student John is 0.0'
        self.assertEqual(string1, answer, msg=error_output)

    def test_g1_displayCourses(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayCourses() provides the correct output"""
        error_fail = 'lab6a.py contains errors(HINT: error occurs when addGrade() never gets run)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            string1 = set(student.displayCourses())
        except:
            self.fail(error_fail)
        answer = set([])
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_g2_displayCourses(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayCourses() provides the correct output"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            student.addGrade('uli101', 4.0)
            student.addGrade('ops235', 1.0)
            string1 = set(student.displayCourses())
        except:
            self.fail(error_fail)
        answer = set(['uli101', 'ops235'])
        self.assertEqual(string1, answer, msg=error_output)
    
    def test_h_displayCourses(self):
        """[Lab 6] - [Investigation 1] - [Part 2] - Creating Classes - displayCourses() provides the correct output"""
        error_fail = 'lab6a.py contains errors(HINT: run the script and fix errors)'
        error_output = 'your program has an error(HINT: does not have correct output)'
        try:
            import lab6a as lab6aStudent
            student = lab6aStudent.Student('John', '12345')
            student.addGrade('uli101', 4.0)
            student.addGrade('ipc144', 0.0)
            student.addGrade('ops535', 4.0)
            student.addGrade('ops445', 0.0)
            string1 = set(student.displayCourses())
        except:
            self.fail(error_fail)
        answer = set(['uli101', 'ops535'])
        self.assertEqual(string1, answer, msg=error_output)
    
   

def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab6.py'
        lab_num = 'lab6'
        print('Checking for updates...')
        if ChecksumLatest(url='https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for ' + lab_name + ' please consider updating:')
            print(' cd ~/ops445/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return


def displayReportHeader():
    report_heading = 'OPS445 Lab Report - System Information for running '+sys.argv[0]
    print(report_heading)
    print(len(report_heading) * '=')
    import getpass
    print('    User login name:', getpass.getuser())
    print('    Linux system name:', socket.gethostname())
    print('    Python executable:',sys.executable)
    print('    Python version: ',sys.version_info.major,sys.version_info.minor,sys.version_info.micro,sep='')
    print('    OS Platform:',sys.platform)
    print('    Working Directory:',os.getcwd())
    print('    Start at:',time.asctime())
    print(len(report_heading) * '=')
    return

if __name__ == '__main__':
    #CheckForUpdates()
    #wait = input('Press ENTER to run the Lab Check...')
    if len(sys.argv) == 3:
       report_header = displayReportHeader()
    unittest.main()


