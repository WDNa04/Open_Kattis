import sys

Jon = sys.stdin.readline()
doctor = sys.stdin.readline()
Jon_count = Jon.count('a')
doctor_count = doctor.count('a')
if doctor_count <= Jon_count:
    print("go")
else:
    print("no")

