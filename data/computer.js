window.COMPUTER_DATA = {
  "id": "computer-science",
  "title": "Computer Science",
  "icon": "terminal",
  "description": "C Programming: User-Defined Functions, Recursion, Structures & Unions, Pointers, and Low-Level & High-Level File Handling.",
  "sections": [
    {
      "name": "Function",
      "questions": [
        {
          "id": "cs-q1",
          "number": "1",
          "question": "WAP to check if a number is odd or even number using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nvoid checkOddEven(int num);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &n);\n\n    /* Function call */\n    checkOddEven(n);\n\n    return 0;\n}\n\n/* Function definition */\nvoid checkOddEven(int num)\n{\n    if(num % 2 == 0)\n    {\n        printf(\"%d is an EVEN number.\\n\", num);\n    }\n    else\n    {\n        printf(\"%d is an ODD number.\\n\", num);\n    }\n}\n```"
        },
        {
          "id": "cs-q2",
          "number": "2",
          "question": "WAP to check if a number is positive, negative or zero using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nvoid checkSign(int num);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter a number: \");\n    scanf(\"%d\", &n);\n\n    /* Function call */\n    checkSign(n);\n\n    return 0;\n}\n\n/* Function definition */\nvoid checkSign(int num)\n{\n    if(num > 0)\n    {\n        printf(\"%d is POSITIVE.\\n\", num);\n    }\n    else if(num < 0)\n    {\n        printf(\"%d is NEGATIVE.\\n\", num);\n    }\n    else\n    {\n        printf(\"The number is ZERO.\\n\");\n    }\n}\n```"
        },
        {
          "id": "cs-q3",
          "number": "3",
          "question": "WAP to check if a number is Armstrong or not using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nint isArmstrong(int num);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter a positive integer: \");\n    scanf(\"%d\", &n);\n\n    if(isArmstrong(n))\n    {\n        printf(\"%d is an ARMSTRONG number.\\n\", n);\n    }\n    else\n    {\n        printf(\"%d is NOT an Armstrong number.\\n\", n);\n    }\n\n    return 0;\n}\n\n/* Function definition */\nint isArmstrong(int num)\n{\n    int original, rem, sum;\n\n    original = num;\n    sum = 0;\n\n    while(num != 0)\n    {\n        rem = num % 10;\n        sum += (rem * rem * rem);\n        num /= 10;\n    }\n\n    if(sum == original)\n    {\n        return 1;\n    }\n    else\n    {\n        return 0;\n    }\n}\n```"
        },
        {
          "id": "cs-q4",
          "number": "4",
          "question": "WAP to check if a number is prime or composite using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nint checkPrime(int num);\n\nint main()\n{\n    int n, result;\n\n    printf(\"Enter an integer greater than 1: \");\n    scanf(\"%d\", &n);\n\n    if(n <= 1)\n    {\n        printf(\"Neither prime nor composite.\\n\");\n        return 0;\n    }\n\n    result = checkPrime(n);\n\n    if(result == 1)\n    {\n        printf(\"%d is a PRIME number.\\n\", n);\n    }\n    else\n    {\n        printf(\"%d is a COMPOSITE number.\\n\", n);\n    }\n\n    return 0;\n}\n\n/* Function definition */\nint checkPrime(int num)\n{\n    int i;\n\n    for(i = 2; i <= num / 2; i++)\n    {\n        if(num % i == 0)\n        {\n            return 0; /* Composite */\n        }\n    }\n\n    return 1; /* Prime */\n}\n```"
        },
        {
          "id": "cs-q5",
          "number": "5",
          "question": "WAP to check if a number is palindrome or not using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nint isPalindrome(int num);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &n);\n\n    if(isPalindrome(n))\n    {\n        printf(\"%d is a PALINDROME number.\\n\", n);\n    }\n    else\n    {\n        printf(\"%d is NOT a palindrome number.\\n\", n);\n    }\n\n    return 0;\n}\n\n/* Function definition */\nint isPalindrome(int num)\n{\n    int original, rev, rem;\n\n    original = num;\n    rev = 0;\n\n    while(num != 0)\n    {\n        rem = num % 10;\n        rev = (rev * 10) + rem;\n        num /= 10;\n    }\n\n    if(original == rev)\n    {\n        return 1;\n    }\n    else\n    {\n        return 0;\n    }\n}\n```"
        },
        {
          "id": "cs-q6",
          "number": "6",
          "question": "WAP to input 10 numbers in an array and find maximum and minimum number using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nvoid findMaxMin(int arr[], int size);\n\nint main()\n{\n    int arr[10];\n    int i;\n\n    printf(\"Enter 10 integers:\\n\");\n    for(i = 0; i < 10; i++)\n    {\n        printf(\"Element %d: \", i + 1);\n        scanf(\"%d\", &arr[i]);\n    }\n\n    /* Function call */\n    findMaxMin(arr, 10);\n\n    return 0;\n}\n\n/* Function definition */\nvoid findMaxMin(int arr[], int size)\n{\n    int i, max, min;\n\n    max = arr[0];\n    min = arr[0];\n\n    for(i = 1; i < size; i++)\n    {\n        if(arr[i] > max)\n        {\n            max = arr[i];\n        }\n        if(arr[i] < min)\n        {\n            min = arr[i];\n        }\n    }\n\n    printf(\"\\nMaximum value = %d\\n\", max);\n    printf(\"Minimum value = %d\\n\", min);\n}\n```"
        },
        {
          "id": "cs-q7",
          "number": "7",
          "question": "WAP to input 10 numbers in an array and sort them in ascending order using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nvoid sortAscending(int arr[], int size);\n\nint main()\n{\n    int arr[10];\n    int i;\n\n    printf(\"Enter 10 integers to sort:\\n\");\n    for(i = 0; i < 10; i++)\n    {\n        printf(\"Element %d: \", i + 1);\n        scanf(\"%d\", &arr[i]);\n    }\n\n    /* Sort using function */\n    sortAscending(arr, 10);\n\n    printf(\"\\nArray in ascending order:\\n\");\n    for(i = 0; i < 10; i++)\n    {\n        printf(\"%d \", arr[i]);\n    }\n    printf(\"\\n\");\n\n    return 0;\n}\n\n/* Function definition (Bubble Sort) */\nvoid sortAscending(int arr[], int size)\n{\n    int i, j, temp;\n\n    for(i = 0; i < size - 1; i++)\n    {\n        for(j = 0; j < size - i - 1; j++)\n        {\n            if(arr[j] > arr[j + 1])\n            {\n                temp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = temp;\n            }\n        }\n    }\n}\n```"
        },
        {
          "id": "cs-q8",
          "number": "8",
          "question": "WAP to input a 3x3 matrix and find transpose of it using function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration */\nvoid transposeMatrix(int mat[3][3]);\n\nint main()\n{\n    int mat[3][3];\n    int i, j;\n\n    printf(\"Enter elements of 3x3 matrix:\\n\");\n    for(i = 0; i < 3; i++)\n    {\n        for(j = 0; j < 3; j++)\n        {\n            printf(\"Element [%d][%d]: \", i, j);\n            scanf(\"%d\", &mat[i][j]);\n        }\n    }\n\n    printf(\"\\nOriginal Matrix:\\n\");\n    for(i = 0; i < 3; i++)\n    {\n        for(j = 0; j < 3; j++)\n        {\n            printf(\"%4d\", mat[i][j]);\n        }\n        printf(\"\\n\");\n    }\n\n    /* Transpose function call */\n    transposeMatrix(mat);\n\n    return 0;\n}\n\n/* Function definition */\nvoid transposeMatrix(int mat[3][3])\n{\n    int trans[3][3];\n    int i, j;\n\n    for(i = 0; i < 3; i++)\n    {\n        for(j = 0; j < 3; j++)\n        {\n            trans[j][i] = mat[i][j];\n        }\n    }\n\n    printf(\"\\nTranspose of the Matrix:\\n\");\n    for(i = 0; i < 3; i++)\n    {\n        for(j = 0; j < 3; j++)\n        {\n            printf(\"%4d\", trans[i][j]);\n        }\n        printf(\"\\n\");\n    }\n}\n```"
        },
        {
          "id": "cs-q9",
          "number": "9",
          "question": "WAP to input a string and check if it is palindrome or not using function.",
          "answer": "```c\n#include <stdio.h>\n#include <string.h>\n\n/* Function declaration */\nint checkStringPalindrome(char str[]);\n\nint main()\n{\n    char str[100];\n\n    printf(\"Enter a string: \");\n    scanf(\"%s\", str);\n\n    if(checkStringPalindrome(str))\n    {\n        printf(\"\\\"%s\\\" is a PALINDROME string.\\n\", str);\n    }\n    else\n    {\n        printf(\"\\\"%s\\\" is NOT a palindrome string.\\n\", str);\n    }\n\n    return 0;\n}\n\n/* Function definition */\nint checkStringPalindrome(char str[])\n{\n    int i, len;\n\n    len = strlen(str);\n\n    for(i = 0; i < len / 2; i++)\n    {\n        if(str[i] != str[len - 1 - i])\n        {\n            return 0; /* Not a palindrome */\n        }\n    }\n\n    return 1; /* Palindrome */\n}\n```"
        }
      ]
    },
    {
      "name": "Recursive Function",
      "questions": [
        {
          "id": "cs-q10",
          "number": "10",
          "question": "WAP to find factorial of a given number using recursive function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Recursive function declaration */\nlong factorial(int n);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter a non-negative integer: \");\n    scanf(\"%d\", &n);\n\n    if(n < 0)\n    {\n        printf(\"Factorial of a negative number does not exist.\\n\");\n    }\n    else\n    {\n        printf(\"Factorial of %d = %ld\\n\", n, factorial(n));\n    }\n\n    return 0;\n}\n\n/* Recursive function definition */\nlong factorial(int n)\n{\n    /* Base case */\n    if(n == 0 || n == 1)\n    {\n        return 1;\n    }\n    /* Recursive case */\n    return (n * factorial(n - 1));\n}\n```"
        },
        {
          "id": "cs-q11",
          "number": "11",
          "question": "WAP to find nth Fibonacci term using recursive function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Recursive function declaration */\nint fibonacci(int n);\n\nint main()\n{\n    int n;\n\n    printf(\"Enter term position (n >= 1): \");\n    scanf(\"%d\", &n);\n\n    if(n <= 0)\n    {\n        printf(\"Invalid input. Please enter n >= 1.\\n\");\n    }\n    else\n    {\n        printf(\"The %d-th Fibonacci term is: %d\\n\", n, fibonacci(n));\n    }\n\n    return 0;\n}\n\n/* Recursive function definition */\nint fibonacci(int n)\n{\n    /* Base cases */\n    if(n == 1)\n    {\n        return 0;\n    }\n    if(n == 2)\n    {\n        return 1;\n    }\n    /* Recursive relation */\n    return (fibonacci(n - 1) + fibonacci(n - 2));\n}\n```"
        },
        {
          "id": "cs-q12",
          "number": "12",
          "question": "WAP to find sum of digits of a given number using recursive function.",
          "answer": "```c\n#include <stdio.h>\n\n/* Recursive function declaration */\nint sumOfDigits(int n);\n\nint main()\n{\n    int n, result;\n\n    printf(\"Enter an integer: \");\n    scanf(\"%d\", &n);\n\n    /* Absolute value for negative numbers */\n    if(n < 0)\n    {\n        n = -n;\n    }\n\n    result = sumOfDigits(n);\n    printf(\"Sum of digits = %d\\n\", result);\n\n    return 0;\n}\n\n/* Recursive function definition */\nint sumOfDigits(int n)\n{\n    /* Base case */\n    if(n == 0)\n    {\n        return 0;\n    }\n    /* Recursive case: last digit + sum of remaining digits */\n    return ((n % 10) + sumOfDigits(n / 10));\n}\n```"
        }
      ]
    },
    {
      "name": "Structure and Union",
      "questions": [
        {
          "id": "cs-q13",
          "number": "13",
          "question": "WAP to input id, name and salary of 10 employees and display them using structure.",
          "answer": "```c\n#include <stdio.h>\n\nstruct employee\n{\n    int id;\n    char name[40];\n    float salary;\n};\n\nint main()\n{\n    struct employee emp[10];\n    int i;\n\n    /* Input employee details */\n    printf(\"Enter details of 10 employees:\\n\");\n    for(i = 0; i < 10; i++)\n    {\n        printf(\"\\nEmployee %d:\\n\", i + 1);\n        printf(\"Enter ID: \");\n        scanf(\"%d\", &emp[i].id);\n        printf(\"Enter Name: \");\n        scanf(\"%s\", emp[i].name);\n        printf(\"Enter Salary: \");\n        scanf(\"%f\", &emp[i].salary);\n    }\n\n    /* Display employee details */\n    printf(\"\\n================ EMPLOYEE RECORDS ================\\n\");\n    printf(\"%-8s %-20s %-12s\\n\", \"ID\", \"Name\", \"Salary\");\n    printf(\"-------------------------------------------------\\n\");\n\n    for(i = 0; i < 10; i++)\n    {\n        printf(\"%-8d %-20s Rs. %-10.2f\\n\",\n               emp[i].id, emp[i].name, emp[i].salary);\n    }\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q14",
          "number": "14",
          "question": "WAP to input roll, name and marks in 3 subjects of a student and calculate total and percentage using structure.",
          "answer": "```c\n#include <stdio.h>\n\nstruct student\n{\n    int roll;\n    char name[40];\n    float marks[3];\n    float total;\n    float percentage;\n};\n\nint main()\n{\n    struct student s;\n    int i;\n\n    /* Input student details */\n    printf(\"Enter Roll Number: \");\n    scanf(\"%d\", &s.roll);\n\n    printf(\"Enter Name: \");\n    scanf(\"%s\", s.name);\n\n    s.total = 0;\n    printf(\"Enter marks in 3 subjects:\\n\");\n    for(i = 0; i < 3; i++)\n    {\n        printf(\"Subject %d: \", i + 1);\n        scanf(\"%f\", &s.marks[i]);\n        s.total += s.marks[i];\n    }\n\n    /* Calculate percentage */\n    s.percentage = (s.total / 300.0) * 100.0;\n\n    /* Display mark sheet */\n    printf(\"\\n========== STUDENT REPORT CARD ==========\\n\");\n    printf(\"Roll Number : %d\\n\", s.roll);\n    printf(\"Name        : %s\\n\", s.name);\n    printf(\"Marks       : %.1f, %.1f, %.1f\\n\",\n           s.marks[0], s.marks[1], s.marks[2]);\n    printf(\"Total Marks : %.2f / 300.00\\n\", s.total);\n    printf(\"Percentage  : %.2f%%\\n\", s.percentage);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q15",
          "number": "15",
          "question": "WAP to input id, name and price of 5 books and display the book with highest price using structure.",
          "answer": "```c\n#include <stdio.h>\n\nstruct book\n{\n    int id;\n    char name[50];\n    float price;\n};\n\nint main()\n{\n    struct book b[5];\n    int i, maxIndex;\n\n    /* Input details of 5 books */\n    printf(\"Enter details of 5 books:\\n\");\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"\\nBook %d:\\n\", i + 1);\n        printf(\"Enter Book ID: \");\n        scanf(\"%d\", &b[i].id);\n        printf(\"Enter Book Name: \");\n        scanf(\"%s\", b[i].name);\n        printf(\"Enter Price: \");\n        scanf(\"%f\", &b[i].price);\n    }\n\n    /* Find the book with maximum price */\n    maxIndex = 0;\n    for(i = 1; i < 5; i++)\n    {\n        if(b[i].price > b[maxIndex].price)\n        {\n            maxIndex = i;\n        }\n    }\n\n    /* Display highest priced book */\n    printf(\"\\n========== MOST EXPENSIVE BOOK ==========\\n\");\n    printf(\"Book ID   : %d\\n\", b[maxIndex].id);\n    printf(\"Title     : %s\\n\", b[maxIndex].name);\n    printf(\"Price     : Rs. %.2f\\n\", b[maxIndex].price);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q16",
          "number": "16",
          "question": "WAP to demonstrate the difference between structure and union.",
          "answer": "```c\n#include <stdio.h>\n\n/* Structure definition */\nstruct DemoStruct\n{\n    int i;\n    float f;\n    char c;\n};\n\n/* Union definition */\nunion DemoUnion\n{\n    int i;\n    float f;\n    char c;\n};\n\nint main()\n{\n    struct DemoStruct s;\n    union DemoUnion u;\n\n    /* 1. Difference in memory size */\n    printf(\"Size of Structure = %lu bytes\\n\", sizeof(s));\n    printf(\"Size of Union     = %lu bytes\\n\", sizeof(u));\n\n    /* 2. Difference in member accessibility */\n    printf(\"\\n--- Structure Demonstration ---\\n\");\n    s.i = 101;\n    s.f = 75.50;\n    s.c = 'A';\n    printf(\"Structure members can hold values simultaneously:\\n\");\n    printf(\"s.i = %d, s.f = %.2f, s.c = %c\\n\", s.i, s.f, s.c);\n\n    printf(\"\\n--- Union Demonstration ---\\n\");\n    u.i = 101;\n    printf(\"u.i = %d\\n\", u.i);\n\n    u.f = 75.50;\n    printf(\"u.f = %.2f (u.i is now corrupted: %d)\\n\", u.f, u.i);\n\n    u.c = 'A';\n    printf(\"u.c = %c (u.f and u.i are overwritten)\\n\", u.c);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q17",
          "number": "17",
          "question": "WAP to demonstrate nested structure.",
          "answer": "```c\n#include <stdio.h>\n\n/* Inner structure */\nstruct Date\n{\n    int day;\n    int month;\n    int year;\n};\n\n/* Outer structure containing inner structure */\nstruct Employee\n{\n    int id;\n    char name[40];\n    float salary;\n    struct Date joinDate;\n};\n\nint main()\n{\n    struct Employee emp;\n\n    /* Input employee details */\n    printf(\"Enter Employee ID: \");\n    scanf(\"%d\", &emp.id);\n\n    printf(\"Enter Employee Name: \");\n    scanf(\"%s\", emp.name);\n\n    printf(\"Enter Salary: \");\n    scanf(\"%f\", &emp.salary);\n\n    printf(\"Enter Joining Date (Day Month Year): \");\n    scanf(\"%d %d %d\", &emp.joinDate.day, &emp.joinDate.month, &emp.joinDate.year);\n\n    /* Display employee details */\n    printf(\"\\n========== EMPLOYEE DETAILS ==========\\n\");\n    printf(\"ID           : %d\\n\", emp.id);\n    printf(\"Name         : %s\\n\", emp.name);\n    printf(\"Salary       : Rs. %.2f\\n\", emp.salary);\n    printf(\"Joining Date : %02d/%02d/%04d\\n\",\n           emp.joinDate.day, emp.joinDate.month, emp.joinDate.year);\n\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "Pointer",
      "questions": [
        {
          "id": "cs-q18",
          "number": "18",
          "question": "WAP to find sum and average of two numbers using pointer.",
          "answer": "```c\n#include <stdio.h>\n\nint main()\n{\n    float num1, num2;\n    float *p1, *p2;\n    float sum, avg;\n\n    /* Assign addresses to pointers */\n    p1 = &num1;\n    p2 = &num2;\n\n    printf(\"Enter first number: \");\n    scanf(\"%f\", p1);\n\n    printf(\"Enter second number: \");\n    scanf(\"%f\", p2);\n\n    /* Calculation using dereference operator */\n    sum = *p1 + *p2;\n    avg = sum / 2.0;\n\n    printf(\"\\nSum     = %.2f\\n\", sum);\n    printf(\"Average = %.2f\\n\", avg);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q19",
          "number": "19",
          "question": "WAP to swap two numbers using call by reference (pointer).",
          "answer": "```c\n#include <stdio.h>\n\n/* Function declaration using pointers */\nvoid swap(int *a, int *b);\n\nint main()\n{\n    int x, y;\n\n    printf(\"Enter two numbers (x and y): \");\n    scanf(\"%d %d\", &x, &y);\n\n    printf(\"\\nBefore Swapping: x = %d, y = %d\\n\", x, y);\n\n    /* Call by reference */\n    swap(&x, &y);\n\n    printf(\"After Swapping : x = %d, y = %d\\n\", x, y);\n\n    return 0;\n}\n\n/* Function definition */\nvoid swap(int *a, int *b)\n{\n    int temp;\n\n    temp = *a;\n    *a = *b;\n    *b = temp;\n}\n```"
        },
        {
          "id": "cs-q20",
          "number": "20",
          "question": "WAP to find largest number among elements of an array using pointer.",
          "answer": "```c\n#include <stdio.h>\n\nint main()\n{\n    int arr[10];\n    int n, i;\n    int *ptr, max;\n\n    printf(\"Enter number of elements (1 to 10): \");\n    scanf(\"%d\", &n);\n\n    ptr = arr; /* Point to first element */\n\n    printf(\"Enter %d integers:\\n\", n);\n    for(i = 0; i < n; i++)\n    {\n        printf(\"Element %d: \", i + 1);\n        scanf(\"%d\", (ptr + i));\n    }\n\n    /* Find largest element using pointer */\n    max = *ptr;\n    for(i = 1; i < n; i++)\n    {\n        if(*(ptr + i) > max)\n        {\n            max = *(ptr + i);\n        }\n    }\n\n    printf(\"\\nLargest element = %d\\n\", max);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q21",
          "number": "21",
          "question": "WAP to find length of a string using pointer.",
          "answer": "```c\n#include <stdio.h>\n\nint main()\n{\n    char str[100];\n    char *ptr;\n    int length;\n\n    printf(\"Enter a string: \");\n    scanf(\"%s\", str);\n\n    /* Initialize pointer to the beginning of string */\n    ptr = str;\n    length = 0;\n\n    /* Count characters until null terminator '\\0' */\n    while(*ptr != '\\0')\n    {\n        length++;\n        ptr++;\n    }\n\n    printf(\"Length of the string = %d\\n\", length);\n\n    return 0;\n}\n```"
        }
      ]
    },
    {
      "name": "File Handling",
      "questions": [
        {
          "id": "cs-q22",
          "number": "22",
          "question": "Write down the C program for the following file handling function a. putw() and getw() b. fputc() and fgetc() c. fputs() and fgets()",
          "answer": "### a. Demonstration of putw() and getw() (Integer I/O)\n```c\n#include <stdio.h>\n\nint main()\n{\n    FILE *fp;\n    int num;\n\n    /* Open file for writing binary integers */\n    fp = fopen(\"numbers.dat\", \"wb\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Writing integers to file using putw():\\n\");\n    putw(100, fp);\n    putw(250, fp);\n    putw(500, fp);\n    fclose(fp);\n\n    /* Open file for reading */\n    fp = fopen(\"numbers.dat\", \"rb\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Reading integers from file using getw():\\n\");\n    while((num = getw(fp)) != EOF)\n    {\n        printf(\"%d\\n\", num);\n    }\n\n    fclose(fp);\n\n    return 0;\n}\n```\n\n### b. Demonstration of fputc() and fgetc() (Character I/O)\n```c\n#include <stdio.h>\n\nint main()\n{\n    FILE *fp;\n    char ch;\n    char text[] = \"Studyroom Class 12 NEB\";\n    int i;\n\n    /* Open file for character write */\n    fp = fopen(\"chars.txt\", \"w\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    /* Write character by character using fputc */\n    for(i = 0; text[i] != '\\0'; i++)\n    {\n        fputc(text[i], fp);\n    }\n    fclose(fp);\n\n    /* Read character by character using fgetc */\n    fp = fopen(\"chars.txt\", \"r\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Read characters:\\n\");\n    while((ch = fgetc(fp)) != EOF)\n    {\n        putchar(ch);\n    }\n    printf(\"\\n\");\n\n    fclose(fp);\n\n    return 0;\n}\n```\n\n### c. Demonstration of fputs() and fgets() (String I/O)\n```c\n#include <stdio.h>\n\nint main()\n{\n    FILE *fp;\n    char line[100];\n\n    /* Open file for string write */\n    fp = fopen(\"strings.txt\", \"w\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    /* Write strings using fputs */\n    fputs(\"Kathmandu, Nepal\\n\", fp);\n    fputs(\"Fluorescent SS College\\n\", fp);\n    fclose(fp);\n\n    /* Read strings using fgets */\n    fp = fopen(\"strings.txt\", \"r\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\\n\");\n        return 1;\n    }\n\n    printf(\"Read lines:\\n\");\n    while(fgets(line, sizeof(line), fp) != NULL)\n    {\n        printf(\"%s\", line);\n    }\n\n    fclose(fp);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q23",
          "number": "23",
          "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same reading from the file using file handling function. (use structure)",
          "answer": "```c\n#include <stdio.h>\n\nstruct student\n{\n    int id;\n    char name[30];\n    float percentage;\n};\n\nint main()\n{\n    struct student s;\n    FILE *fp;\n    int i;\n\n    /* Open file for writing */\n    fp = fopen(\"student.txt\", \"w\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    /* Input and store records */\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter ID, Name and Percentage: \");\n        scanf(\"%d %s %f\", &s.id, s.name, &s.percentage);\n\n        fprintf(fp, \"%d %s %.2f\\n\",\n                s.id, s.name, s.percentage);\n    }\n\n    fclose(fp);\n\n    /* Open file for reading */\n    fp = fopen(\"student.txt\", \"r\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    printf(\"\\nStudent Records:\\n\");\n\n    /* Read and display records */\n    while(fscanf(fp, \"%d %s %f\",\n                 &s.id, s.name, &s.percentage) != EOF)\n    {\n        printf(\"ID: %d\\n\", s.id);\n        printf(\"Name: %s\\n\", s.name);\n        printf(\"Percentage: %.2f\\n\\n\", s.percentage);\n    }\n\n    fclose(fp);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q24",
          "number": "24",
          "question": "Write down a C program to input book_id, name and price of 5 books and store it in a file. Display the same reading from the file using file handling function. (don’t use structure)",
          "answer": "```c\n#include <stdio.h>\n\nint main()\n{\n    FILE *fp;\n    int book_id;\n    char name[50];\n    float price;\n    int i;\n\n    /* Open file for writing without structure */\n    fp = fopen(\"books_record.txt\", \"w\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    /* Input and write 5 books */\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter Book ID, Name and Price: \");\n        scanf(\"%d %s %f\", &book_id, name, &price);\n\n        fprintf(fp, \"%d %s %.2f\\n\", book_id, name, price);\n    }\n\n    fclose(fp);\n\n    /* Open file for reading */\n    fp = fopen(\"books_record.txt\", \"r\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    printf(\"\\nBook Records from File:\\n\");\n\n    /* Read and display records */\n    while(fscanf(fp, \"%d %s %f\", &book_id, name, &price) != EOF)\n    {\n        printf(\"Book ID : %d\\n\", book_id);\n        printf(\"Title   : %s\\n\", name);\n        printf(\"Price   : Rs. %.2f\\n\\n\", price);\n    }\n\n    fclose(fp);\n\n    return 0;\n}\n```"
        },
        {
          "id": "cs-q25",
          "number": "25",
          "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same using file handling function. (use structure and fread() and fwrite() function)",
          "answer": "```c\n#include <stdio.h>\n\nstruct student\n{\n    int id;\n    char name[30];\n    float percentage;\n};\n\nint main()\n{\n    struct student s;\n    FILE *fp;\n    int i;\n\n    /* Open binary file for writing */\n    fp = fopen(\"students.dat\", \"wb\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    /* Input and write binary records using fwrite() */\n    for(i = 0; i < 5; i++)\n    {\n        printf(\"Enter ID, Name and Percentage: \");\n        scanf(\"%d %s %f\", &s.id, s.name, &s.percentage);\n\n        fwrite(&s, sizeof(struct student), 1, fp);\n    }\n\n    fclose(fp);\n\n    /* Open binary file for reading */\n    fp = fopen(\"students.dat\", \"rb\");\n\n    if(fp == NULL)\n    {\n        printf(\"File cannot be opened.\");\n        return 1;\n    }\n\n    printf(\"\\nStudent Records read using fread():\\n\");\n\n    /* Read binary records using fread() */\n    while(fread(&s, sizeof(struct student), 1, fp) == 1)\n    {\n        printf(\"ID         : %d\\n\", s.id);\n        printf(\"Name       : %s\\n\", s.name);\n        printf(\"Percentage : %.2f%%\\n\\n\", s.percentage);\n    }\n\n    fclose(fp);\n\n    return 0;\n}\n```"
        }
      ]
    }
  ]
};
