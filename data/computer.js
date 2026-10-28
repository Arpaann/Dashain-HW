window.COMPUTER_DATA = {
  "id": "computer-science",
  "title": "Computer Science",
  "icon": "terminal",
  "description": "C Programming: User-Defined Functions, Recursion, Structures & Unions, Pointers, and File Handling.",
  "sections": [
    {
      "name": "Function",
      "questions": [
        {
          "id": "cs-q1",
          "number": "1",
          "question": "WAP to check a number is odd or even number using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid checkOddEven(int n)\n{\n    if(n % 2 == 0)\n    {\n        printf(\"%d is Even\\n\", n);\n    }\n    else\n    {\n        printf(\"%d is Odd\\n\", n);\n    }\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &num);\n    checkOddEven(num);\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q2",
          "number": "2",
          "question": "WAP to display 2, 4, 6, 8, 10…..up to nth items using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid displayEvenSeries(int n)\n{\n    int i;\n    for(i = 1; i <= n; i++)\n    {\n        printf(\"%d \", 2 * i);\n    }\n    printf(\"\\n\");\n}\n\nint main()\n{\n    int n;\n    printf(\"Enter number of terms: \");\n    scanf(\"%d\", &n);\n    printf(\"Series: \");\n    displayEvenSeries(n);\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q3",
          "number": "3",
          "question": "WAP to find out the factorial of a number using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nlong getFactorial(int n)\n{\n    long fact = 1;\n    int i;\n    for(i = 1; i <= n; i++)\n    {\n        fact = fact * i;\n    }\n    return fact;\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter a positive integer: \");\n    scanf(\"%d\", &num);\n    printf(\"Factorial of %d = %ld\\n\", num, getFactorial(num));\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q4",
          "number": "4",
          "question": "WAP to display Fibonacci Series up to nth term using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid displayFibonacci(int n)\n{\n    int a = 0, b = 1, c, i;\n    for(i = 1; i <= n; i++)\n    {\n        printf(\"%d \", a);\n        c = a + b;\n        a = b;\n        b = c;\n    }\n    printf(\"\\n\");\n}\n\nint main()\n{\n    int n;\n    printf(\"Enter number of terms: \");\n    scanf(\"%d\", &n);\n    printf(\"Fibonacci Series: \");\n    displayFibonacci(n);\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q5",
          "number": "5",
          "question": "WAP to find Multiplication table of the given number using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid printTable(int n)\n{\n    int i;\n    for(i = 1; i <= 10; i++)\n    {\n        printf(\"%d x %d = %d\\n\", n, i, n * i);\n    }\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter a number: \");\n    scanf(\"%d\", &num);\n    printf(\"Multiplication Table of %d:\\n\", num);\n    printTable(num);\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q6",
          "number": "6",
          "question": "WAP to check if a number is palindrome or not using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint checkPalindrome(int n)\n{\n    int original = n, rev = 0, rem;\n    while(n != 0)\n    {\n        rem = n % 10;\n        rev = rev * 10 + rem;\n        n = n / 10;\n    }\n    if(original == rev)\n    {\n        return 1;\n    }\n    else\n    {\n        return 0;\n    }\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &num);\n    if(checkPalindrome(num) == 1)\n    {\n        printf(\"%d is Palindrome\\n\", num);\n    }\n    else\n    {\n        printf(\"%d is Not Palindrome\\n\", num);\n    }\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q7",
          "number": "7",
          "question": "WAP to check if a number is prime or composite using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint isPrime(int n)\n{\n    int i;\n    if(n <= 1)\n    {\n        return -1;\n    }\n    for(i = 2; i <= n / 2; i++)\n    {\n        if(n % i == 0)\n        {\n            return 0;\n        }\n    }\n    return 1;\n}\n\nint main()\n{\n    int num, status;\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &num);\n    status = isPrime(num);\n    if(status == 1)\n    {\n        printf(\"%d is a Prime Number\\n\", num);\n    }\n    else if(status == 0)\n    {\n        printf(\"%d is a Composite Number\\n\", num);\n    }\n    else\n    {\n        printf(\"%d is neither Prime nor Composite\\n\", num);\n    }\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q8",
          "number": "8",
          "question": "WAP to check if a number is Armstrong or not using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint isArmstrong(int n)\n{\n    int original = n, sum = 0, rem;\n    while(n != 0)\n    {\n        rem = n % 10;\n        sum = sum + (rem * rem * rem);\n        n = n / 10;\n    }\n    if(sum == original)\n    {\n        return 1;\n    }\n    else\n    {\n        return 0;\n    }\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &num);\n    if(isArmstrong(num) == 1)\n    {\n        printf(\"%d is an Armstrong Number\\n\", num);\n    }\n    else\n    {\n        printf(\"%d is Not an Armstrong Number\\n\", num);\n    }\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q9",
          "number": "9",
          "question": "WAP to display prime numbers up to nth items using function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint checkPrime(int n)\n{\n    int i;\n    if(n <= 1)\n    {\n        return 0;\n    }\n    for(i = 2; i <= n / 2; i++)\n    {\n        if(n % i == 0)\n        {\n            return 0;\n        }\n    }\n    return 1;\n}\n\nvoid displayPrimes(int n)\n{\n    int count = 0, num = 2;\n    while(count < n)\n    {\n        if(checkPrime(num) == 1)\n        {\n            printf(\"%d \", num);\n            count++;\n        }\n        num++;\n    }\n    printf(\"\\n\");\n}\n\nint main()\n{\n    int n;\n    printf(\"Enter number of prime items to display: \");\n    scanf(\"%d\", &n);\n    printf(\"First %d Prime Numbers: \", n);\n    displayPrimes(n);\n    getch();\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "Recursive Function",
      "questions": [
        {
          "id": "cs-q10",
          "number": "10",
          "question": "WAP to find factorial of a number using recursive function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nlong fact(int n)\n{\n    if(n == 0 || n == 1)\n    {\n        return 1;\n    }\n    else\n    {\n        return n * fact(n - 1);\n    }\n}\n\nint main()\n{\n    int num;\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &num);\n    printf(\"Factorial of %d = %ld\\n\", num, fact(num));\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q11",
          "number": "11",
          "question": "WAP to find sum of numbers up to n using recursive function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint sum(int n)\n{\n    if(n == 1)\n    {\n        return 1;\n    }\n    else\n    {\n        return n + sum(n - 1);\n    }\n}\n\nint main()\n{\n    int n;\n    printf(\"Enter value of n: \");\n    scanf(\"%d\", &n);\n    printf(\"Sum from 1 to %d = %d\\n\", n, sum(n));\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q12",
          "number": "12",
          "question": "WAP to display Fibonacci Series up to nth term using recursive function.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint fibo(int n)\n{\n    if(n == 1)\n    {\n        return 0;\n    }\n    else if(n == 2)\n    {\n        return 1;\n    }\n    else\n    {\n        return fibo(n - 1) + fibo(n - 2);\n    }\n}\n\nint main()\n{\n    int n, i;\n    printf(\"Enter number of terms: \");\n    scanf(\"%d\", &n);\n    printf(\"Fibonacci Series: \");\n    for(i = 1; i <= n; i++)\n    {\n        printf(\"%d \", fibo(i));\n    }\n    printf(\"\\n\");\n    getch();\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "Structure and Union",
      "questions": [
        {
          "id": "cs-q13",
          "number": "13",
          "question": "WAP to store name, roll number, age and address of a student and display it using structure.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nstruct student\n{\n    char name[40];\n    int roll;\n    int age;\n    char address[50];\n};\n\nint main()\n{\n    struct student s;\n\n    printf(\"Enter student name: \");\n    scanf(\"%s\", s.name);\n    printf(\"Enter roll number: \");\n    scanf(\"%d\", &s.roll);\n    printf(\"Enter age: \");\n    scanf(\"%d\", &s.age);\n    printf(\"Enter address: \");\n    scanf(\"%s\", s.address);\n\n    printf(\"\\n--- Student Details ---\\n\");\n    printf(\"Name: %s\\n\", s.name);\n    printf(\"Roll: %d\\n\", s.roll);\n    printf(\"Age: %d\\n\", s.age);\n    printf(\"Address: %s\\n\", s.address);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q14",
          "number": "14",
          "question": "WAP to store name, roll number, age and address of nth students and sort them according to the age using structure.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nstruct student\n{\n    char name[40];\n    int roll;\n    int age;\n    char address[50];\n};\n\nint main()\n{\n    struct student s[50], temp;\n    int n, i, j;\n\n    printf(\"Enter number of students: \");\n    scanf(\"%d\", &n);\n\n    for(i = 0; i < n; i++)\n    {\n        printf(\"\\nEnter details of student %d:\\n\", i + 1);\n        printf(\"Name: \");\n        scanf(\"%s\", s[i].name);\n        printf(\"Roll: \");\n        scanf(\"%d\", &s[i].roll);\n        printf(\"Age: \");\n        scanf(\"%d\", &s[i].age);\n        printf(\"Address: \");\n        scanf(\"%s\", s[i].address);\n    }\n\n    for(i = 0; i < n - 1; i++)\n    {\n        for(j = 0; j < n - i - 1; j++)\n        {\n            if(s[j].age > s[j + 1].age)\n            {\n                temp = s[j];\n                s[j] = s[j + 1];\n                s[j + 1] = temp;\n            }\n        }\n    }\n\n    printf(\"\\n--- Students Sorted by Age ---\\n\");\n    for(i = 0; i < n; i++)\n    {\n        printf(\"Name: %s, Roll: %d, Age: %d, Address: %s\\n\",\n               s[i].name, s[i].roll, s[i].age, s[i].address);\n    }\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q15",
          "number": "15",
          "question": "WAP to store name, employee id, salary and address of nth employees and sort them in alphabetical order based on their name using structure.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n#include <string.h>\n\nstruct employee\n{\n    char name[40];\n    int id;\n    float salary;\n    char address[50];\n};\n\nint main()\n{\n    struct employee emp[50], temp;\n    int n, i, j;\n\n    printf(\"Enter number of employees: \");\n    scanf(\"%d\", &n);\n\n    for(i = 0; i < n; i++)\n    {\n        printf(\"\\nEnter details of employee %d:\\n\", i + 1);\n        printf(\"Name: \");\n        scanf(\"%s\", emp[i].name);\n        printf(\"ID: \");\n        scanf(\"%d\", &emp[i].id);\n        printf(\"Salary: \");\n        scanf(\"%f\", &emp[i].salary);\n        printf(\"Address: \");\n        scanf(\"%s\", emp[i].address);\n    }\n\n    for(i = 0; i < n - 1; i++)\n    {\n        for(j = 0; j < n - i - 1; j++)\n        {\n            if(strcmp(emp[j].name, emp[j + 1].name) > 0)\n            {\n                temp = emp[j];\n                emp[j] = emp[j + 1];\n                emp[j + 1] = temp;\n            }\n        }\n    }\n\n    printf(\"\\n--- Employees Sorted Alphabetically by Name ---\\n\");\n    for(i = 0; i < n; i++)\n    {\n        printf(\"Name: %s | ID: %d | Salary: %.2f | Address: %s\\n\",\n               emp[i].name, emp[i].id, emp[i].salary, emp[i].address);\n    }\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q16",
          "number": "16",
          "question": "Develop a program in C using structure to ask the information of any 12 students with roll_number, name and marks scored in sub1, sub2, and sub3. Also, display them in proper format along with the calculation of total and percentage. [Note: the full marks of each subject is 100].",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nstruct student\n{\n    int roll;\n    char name[30];\n    float sub1;\n    float sub2;\n    float sub3;\n    float total;\n    float percentage;\n};\n\nint main()\n{\n    struct student s[12];\n    int i;\n\n    for(i = 0; i < 12; i++)\n    {\n        printf(\"\\nEnter information of student %d:\\n\", i + 1);\n        printf(\"Roll Number: \");\n        scanf(\"%d\", &s[i].roll);\n        printf(\"Name: \");\n        scanf(\"%s\", s[i].name);\n        printf(\"Marks in Sub1, Sub2, Sub3: \");\n        scanf(\"%f %f %f\", &s[i].sub1, &s[i].sub2, &s[i].sub3);\n\n        s[i].total = s[i].sub1 + s[i].sub2 + s[i].sub3;\n        s[i].percentage = (s[i].total / 300.0) * 100.0;\n    }\n\n    printf(\"\\n==================== STUDENT RESULT SHEET ====================\\n\");\n    printf(\"%-6s %-15s %-8s %-8s %-8s %-8s %-8s\\n\",\n           \"Roll\", \"Name\", \"Sub1\", \"Sub2\", \"Sub3\", \"Total\", \"Percent\");\n    printf(\"-------------------------------------------------------------\\n\");\n\n    for(i = 0; i < 12; i++)\n    {\n        printf(\"%-6d %-15s %-8.1f %-8.1f %-8.1f %-8.1f %-7.2f%%\\n\",\n               s[i].roll, s[i].name, s[i].sub1, s[i].sub2, s[i].sub3, s[i].total, s[i].percentage);\n    }\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q17",
          "number": "17",
          "question": "WAP to demonstrate the use of union.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nunion data\n{\n    int i;\n    float f;\n    char ch;\n};\n\nint main()\n{\n    union data d;\n\n    d.i = 10;\n    printf(\"d.i = %d\\n\", d.i);\n\n    d.f = 220.5;\n    printf(\"d.f = %.2f\\n\", d.f);\n\n    d.ch = 'A';\n    printf(\"d.ch = %c\\n\", d.ch);\n\n    printf(\"Size of union data = %lu bytes\\n\", sizeof(d));\n\n    getch();\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "Pointer",
      "questions": [
        {
          "id": "cs-q18",
          "number": "18",
          "question": "WAP to find out the area of rectangle using Pointer.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    float l, b, area;\n    float *p1, *p2;\n\n    p1 = &l;\n    p2 = &b;\n\n    printf(\"Enter length of rectangle: \");\n    scanf(\"%f\", p1);\n    printf(\"Enter breadth of rectangle: \");\n    scanf(\"%f\", p2);\n\n    area = (*p1) * (*p2);\n\n    printf(\"Area of Rectangle = %.2f\\n\", area);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q19",
          "number": "19",
          "question": "WAP to check a number is odd or even number using Pointer.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    int n;\n    int *ptr;\n\n    ptr = &n;\n\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", ptr);\n\n    if(*ptr % 2 == 0)\n    {\n        printf(\"%d is Even\\n\", *ptr);\n    }\n    else\n    {\n        printf(\"%d is Odd\\n\", *ptr);\n    }\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q20",
          "number": "20",
          "question": "WAP to swap two numbers using call by reference.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid swap(int *a, int *b)\n{\n    int temp;\n    temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main()\n{\n    int x, y;\n\n    printf(\"Enter two numbers: \");\n    scanf(\"%d %d\", &x, &y);\n\n    printf(\"Before swap: x = %d, y = %d\\n\", x, y);\n    swap(&x, &y);\n    printf(\"After swap: x = %d, y = %d\\n\", x, y);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q21",
          "number": "21",
          "question": "WAP to swap two numbers using call by value.",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nvoid swap(int a, int b)\n{\n    int temp;\n    temp = a;\n    a = b;\n    b = temp;\n    printf(\"Inside swap function: a = %d, b = %d\\n\", a, b);\n}\n\nint main()\n{\n    int x, y;\n\n    printf(\"Enter two numbers: \");\n    scanf(\"%d %d\", &x, &y);\n\n    printf(\"Before calling swap: x = %d, y = %d\\n\", x, y);\n    swap(x, y);\n    printf(\"After calling swap: x = %d, y = %d\\n\", x, y);\n\n    getch();\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "File Handling",
      "questions": [
        {
          "id": "cs-q22",
          "number": "22",
          "question": "Write down the C program for file handling functions: putw() and getw().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    int num, i;\n\n    fp = fopen(\"numbers.dat\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    for(i = 1; i <= 5; i++)\n    {\n        putw(i * 10, fp);\n    }\n    fclose(fp);\n\n    fp = fopen(\"numbers.dat\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Data read from file using getw():\\n\");\n    while((num = getw(fp)) != EOF)\n    {\n        printf(\"%d\\n\", num);\n    }\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q23",
          "number": "23",
          "question": "Write down the C program for file handling functions: fputc() and fgetc().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    char ch;\n    char text[] = \"Nepal\";\n    int i;\n\n    fp = fopen(\"char.txt\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    for(i = 0; text[i] != '\\0'; i++)\n    {\n        fputc(text[i], fp);\n    }\n    fclose(fp);\n\n    fp = fopen(\"char.txt\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Characters read using fgetc(): \");\n    while((ch = fgetc(fp)) != EOF)\n    {\n        putchar(ch);\n    }\n    printf(\"\\n\");\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q24",
          "number": "24",
          "question": "Write down the C program for file handling functions: fputs() and fgets().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    char str[100];\n\n    fp = fopen(\"text.txt\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    fputs(\"Kathmandu\\n\", fp);\n    fputs(\"Fluorescent College\\n\", fp);\n    fclose(fp);\n\n    fp = fopen(\"text.txt\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Lines read using fgets():\\n\");\n    while(fgets(str, sizeof(str), fp) != NULL)\n    {\n        printf(\"%s\", str);\n    }\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q25",
          "number": "25",
          "question": "Write down a C program to write integer data to a file using putw().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    int num, i, n;\n\n    fp = fopen(\"data.dat\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"How many integers to write: \");\n    scanf(\"%d\", &n);\n\n    for(i = 0; i < n; i++)\n    {\n        printf(\"Enter integer %d: \", i + 1);\n        scanf(\"%d\", &num);\n        putw(num, fp);\n    }\n\n    fclose(fp);\n    printf(\"Data written successfully.\\n\");\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q26",
          "number": "26",
          "question": "Write down a C program to read integer data from a file using getw().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    int num;\n\n    fp = fopen(\"data.dat\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Reading integers from data.dat:\\n\");\n    while((num = getw(fp)) != EOF)\n    {\n        printf(\"%d\\n\", num);\n    }\n\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q27",
          "number": "27",
          "question": "Write down a C program to copy characters from one file to another using fputc() and fgetc().",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *src, *dest;\n    char ch;\n\n    src = fopen(\"source.txt\", \"w\");\n    fputs(\"Programming in C\", src);\n    fclose(src);\n\n    src = fopen(\"source.txt\", \"r\");\n    dest = fopen(\"dest.txt\", \"w\");\n\n    if(src == NULL || dest == NULL)\n    {\n        printf(\"File error.\\n\");\n        return 1;\n    }\n\n    while((ch = fgetc(src)) != EOF)\n    {\n        fputc(ch, dest);\n    }\n\n    fclose(src);\n    fclose(dest);\n\n    printf(\"File copied successfully.\\n\");\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q28",
          "number": "28",
          "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same reading from the file using file handling function. (use structure)",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nstruct student\n{\n    int id;\n    char name[30];\n    float percentage;\n};\n\nint main()\n{\n    struct student s;\n    FILE *fp;\n    int i;\n\n    fp = fopen(\"student.txt\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter ID, Name and Percentage: \");\n        scanf(\"%d %s %f\", &s.id, s.name, &s.percentage);\n        fprintf(fp, \"%d %s %.2f\\n\", s.id, s.name, s.percentage);\n    }\n    fclose(fp);\n\n    fp = fopen(\"student.txt\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    printf(\"\\nStudent Records:\\n\");\n    while(fscanf(fp, \"%d %s %f\", &s.id, s.name, &s.percentage) != EOF)\n    {\n        printf(\"ID: %d\\n\", s.id);\n        printf(\"Name: %s\\n\", s.name);\n        printf(\"Percentage: %.2f\\n\\n\", s.percentage);\n    }\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q29",
          "number": "29",
          "question": "Write down a C program to input book_id, name and price of 5 books and store it in a file. Display the same reading from the file using file handling function. (don’t use structure)",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nint main()\n{\n    FILE *fp;\n    int book_id;\n    char name[40];\n    float price;\n    int i;\n\n    fp = fopen(\"books.txt\", \"w\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter Book ID, Name and Price: \");\n        scanf(\"%d %s %f\", &book_id, name, &price);\n        fprintf(fp, \"%d %s %.2f\\n\", book_id, name, price);\n    }\n    fclose(fp);\n\n    fp = fopen(\"books.txt\", \"r\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"\\n--- Book Records from File ---\\n\");\n    while(fscanf(fp, \"%d %s %f\", &book_id, name, &price) != EOF)\n    {\n        printf(\"Book ID: %d | Name: %s | Price: %.2f\\n\", book_id, name, price);\n    }\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q30",
          "number": "30",
          "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same using file handling function. (use structure and fread() and fwrite() function)",
          "answer": "```c\n#include <stdio.h>\n#include <conio.h>\n\nstruct student\n{\n    int id;\n    char name[30];\n    float percentage;\n};\n\nint main()\n{\n    struct student s;\n    FILE *fp;\n    int i;\n\n    fp = fopen(\"student.dat\", \"wb\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter ID, Name and Percentage: \");\n        scanf(\"%d %s %f\", &s.id, s.name, &s.percentage);\n        fwrite(&s, sizeof(struct student), 1, fp);\n    }\n    fclose(fp);\n\n    fp = fopen(\"student.dat\", \"rb\");\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    printf(\"\\n--- Student Records (Binary fread) ---\\n\");\n    while(fread(&s, sizeof(struct student), 1, fp) == 1)\n    {\n        printf(\"ID: %d\\n\", s.id);\n        printf(\"Name: %s\\n\", s.name);\n        printf(\"Percentage: %.2f\\n\\n\", s.percentage);\n    }\n    fclose(fp);\n\n    getch();\n    return 0;\n}\n```"
        }
      ]
    }
  ]
};
