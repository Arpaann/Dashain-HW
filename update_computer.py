import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

programs = [
    # Q1
    {
        "id": "cs-q1",
        "number": "1",
        "question": "WAP to check if a number is odd or even number using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
void checkOddEven(int num);

int main()
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    /* Function call */
    checkOddEven(n);

    return 0;
}

/* Function definition */
void checkOddEven(int num)
{
    if(num % 2 == 0)
    {
        printf("%d is an EVEN number.\\n", num);
    }
    else
    {
        printf("%d is an ODD number.\\n", num);
    }
}
```"""
    },
    # Q2
    {
        "id": "cs-q2",
        "number": "2",
        "question": "WAP to check if a number is positive, negative or zero using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
void checkSign(int num);

int main()
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    /* Function call */
    checkSign(n);

    return 0;
}

/* Function definition */
void checkSign(int num)
{
    if(num > 0)
    {
        printf("%d is POSITIVE.\\n", num);
    }
    else if(num < 0)
    {
        printf("%d is NEGATIVE.\\n", num);
    }
    else
    {
        printf("The number is ZERO.\\n");
    }
}
```"""
    },
    # Q3
    {
        "id": "cs-q3",
        "number": "3",
        "question": "WAP to check if a number is Armstrong or not using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
int isArmstrong(int num);

int main()
{
    int n;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if(isArmstrong(n))
    {
        printf("%d is an ARMSTRONG number.\\n", n);
    }
    else
    {
        printf("%d is NOT an Armstrong number.\\n", n);
    }

    return 0;
}

/* Function definition */
int isArmstrong(int num)
{
    int original, rem, sum;

    original = num;
    sum = 0;

    while(num != 0)
    {
        rem = num % 10;
        sum += (rem * rem * rem);
        num /= 10;
    }

    if(sum == original)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
```"""
    },
    # Q4
    {
        "id": "cs-q4",
        "number": "4",
        "question": "WAP to check if a number is prime or composite using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
int checkPrime(int num);

int main()
{
    int n, result;

    printf("Enter an integer greater than 1: ");
    scanf("%d", &n);

    if(n <= 1)
    {
        printf("Neither prime nor composite.\\n");
        return 0;
    }

    result = checkPrime(n);

    if(result == 1)
    {
        printf("%d is a PRIME number.\\n", n);
    }
    else
    {
        printf("%d is a COMPOSITE number.\\n", n);
    }

    return 0;
}

/* Function definition */
int checkPrime(int num)
{
    int i;

    for(i = 2; i <= num / 2; i++)
    {
        if(num % i == 0)
        {
            return 0; /* Composite */
        }
    }

    return 1; /* Prime */
}
```"""
    },
    # Q5
    {
        "id": "cs-q5",
        "number": "5",
        "question": "WAP to check if a number is palindrome or not using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
int isPalindrome(int num);

int main()
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if(isPalindrome(n))
    {
        printf("%d is a PALINDROME number.\\n", n);
    }
    else
    {
        printf("%d is NOT a palindrome number.\\n", n);
    }

    return 0;
}

/* Function definition */
int isPalindrome(int num)
{
    int original, rev, rem;

    original = num;
    rev = 0;

    while(num != 0)
    {
        rem = num % 10;
        rev = (rev * 10) + rem;
        num /= 10;
    }

    if(original == rev)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
```"""
    },
    # Q6
    {
        "id": "cs-q6",
        "number": "6",
        "question": "WAP to input 10 numbers in an array and find maximum and minimum number using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
void findMaxMin(int arr[], int size);

int main()
{
    int arr[10];
    int i;

    printf("Enter 10 integers:\\n");
    for(i = 0; i < 10; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    /* Function call */
    findMaxMin(arr, 10);

    return 0;
}

/* Function definition */
void findMaxMin(int arr[], int size)
{
    int i, max, min;

    max = arr[0];
    min = arr[0];

    for(i = 1; i < size; i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
        if(arr[i] < min)
        {
            min = arr[i];
        }
    }

    printf("\\nMaximum value = %d\\n", max);
    printf("Minimum value = %d\\n", min);
}
```"""
    },
    # Q7
    {
        "id": "cs-q7",
        "number": "7",
        "question": "WAP to input 10 numbers in an array and sort them in ascending order using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
void sortAscending(int arr[], int size);

int main()
{
    int arr[10];
    int i;

    printf("Enter 10 integers to sort:\\n");
    for(i = 0; i < 10; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    /* Sort using function */
    sortAscending(arr, 10);

    printf("\\nArray in ascending order:\\n");
    for(i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\\n");

    return 0;
}

/* Function definition (Bubble Sort) */
void sortAscending(int arr[], int size)
{
    int i, j, temp;

    for(i = 0; i < size - 1; i++)
    {
        for(j = 0; j < size - i - 1; j++)
        {
            if(arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```"""
    },
    # Q8
    {
        "id": "cs-q8",
        "number": "8",
        "question": "WAP to input a 3x3 matrix and find transpose of it using function.",
        "answer": """```c
#include <stdio.h>

/* Function declaration */
void transposeMatrix(int mat[3][3]);

int main()
{
    int mat[3][3];
    int i, j;

    printf("Enter elements of 3x3 matrix:\\n");
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }

    printf("\\nOriginal Matrix:\\n");
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            printf("%4d", mat[i][j]);
        }
        printf("\\n");
    }

    /* Transpose function call */
    transposeMatrix(mat);

    return 0;
}

/* Function definition */
void transposeMatrix(int mat[3][3])
{
    int trans[3][3];
    int i, j;

    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            trans[j][i] = mat[i][j];
        }
    }

    printf("\\nTranspose of the Matrix:\\n");
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            printf("%4d", trans[i][j]);
        }
        printf("\\n");
    }
}
```"""
    },
    # Q9
    {
        "id": "cs-q9",
        "number": "9",
        "question": "WAP to input a string and check if it is palindrome or not using function.",
        "answer": """```c
#include <stdio.h>
#include <string.h>

/* Function declaration */
int checkStringPalindrome(char str[]);

int main()
{
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    if(checkStringPalindrome(str))
    {
        printf("\\\"%s\\\" is a PALINDROME string.\\n", str);
    }
    else
    {
        printf("\\\"%s\\\" is NOT a palindrome string.\\n", str);
    }

    return 0;
}

/* Function definition */
int checkStringPalindrome(char str[])
{
    int i, len;

    len = strlen(str);

    for(i = 0; i < len / 2; i++)
    {
        if(str[i] != str[len - 1 - i])
        {
            return 0; /* Not a palindrome */
        }
    }

    return 1; /* Palindrome */
}
```"""
    },
    # Q10 (Recursion)
    {
        "id": "cs-q10",
        "number": "10",
        "question": "WAP to find factorial of a given number using recursive function.",
        "answer": """```c
#include <stdio.h>

/* Recursive function declaration */
long factorial(int n);

int main()
{
    int n;

    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    if(n < 0)
    {
        printf("Factorial of a negative number does not exist.\\n");
    }
    else
    {
        printf("Factorial of %d = %ld\\n", n, factorial(n));
    }

    return 0;
}

/* Recursive function definition */
long factorial(int n)
{
    /* Base case */
    if(n == 0 || n == 1)
    {
        return 1;
    }
    /* Recursive case */
    return (n * factorial(n - 1));
}
```"""
    },
    # Q11
    {
        "id": "cs-q11",
        "number": "11",
        "question": "WAP to find nth Fibonacci term using recursive function.",
        "answer": """```c
#include <stdio.h>

/* Recursive function declaration */
int fibonacci(int n);

int main()
{
    int n;

    printf("Enter term position (n >= 1): ");
    scanf("%d", &n);

    if(n <= 0)
    {
        printf("Invalid input. Please enter n >= 1.\\n");
    }
    else
    {
        printf("The %d-th Fibonacci term is: %d\\n", n, fibonacci(n));
    }

    return 0;
}

/* Recursive function definition */
int fibonacci(int n)
{
    /* Base cases */
    if(n == 1)
    {
        return 0;
    }
    if(n == 2)
    {
        return 1;
    }
    /* Recursive relation */
    return (fibonacci(n - 1) + fibonacci(n - 2));
}
```"""
    },
    # Q12
    {
        "id": "cs-q12",
        "number": "12",
        "question": "WAP to find sum of digits of a given number using recursive function.",
        "answer": """```c
#include <stdio.h>

/* Recursive function declaration */
int sumOfDigits(int n);

int main()
{
    int n, result;

    printf("Enter an integer: ");
    scanf("%d", &n);

    /* Absolute value for negative numbers */
    if(n < 0)
    {
        n = -n;
    }

    result = sumOfDigits(n);
    printf("Sum of digits = %d\\n", result);

    return 0;
}

/* Recursive function definition */
int sumOfDigits(int n)
{
    /* Base case */
    if(n == 0)
    {
        return 0;
    }
    /* Recursive case: last digit + sum of remaining digits */
    return ((n % 10) + sumOfDigits(n / 10));
}
```"""
    },
    # Q13 (Structure & Union)
    {
        "id": "cs-q13",
        "number": "13",
        "question": "WAP to input id, name and salary of 10 employees and display them using structure.",
        "answer": """```c
#include <stdio.h>

struct employee
{
    int id;
    char name[40];
    float salary;
};

int main()
{
    struct employee emp[10];
    int i;

    /* Input employee details */
    printf("Enter details of 10 employees:\\n");
    for(i = 0; i < 10; i++)
    {
        printf("\\nEmployee %d:\\n", i + 1);
        printf("Enter ID: ");
        scanf("%d", &emp[i].id);
        printf("Enter Name: ");
        scanf("%s", emp[i].name);
        printf("Enter Salary: ");
        scanf("%f", &emp[i].salary);
    }

    /* Display employee details */
    printf("\\n================ EMPLOYEE RECORDS ================\\n");
    printf("%-8s %-20s %-12s\\n", "ID", "Name", "Salary");
    printf("-------------------------------------------------\\n");

    for(i = 0; i < 10; i++)
    {
        printf("%-8d %-20s Rs. %-10.2f\\n",
               emp[i].id, emp[i].name, emp[i].salary);
    }

    return 0;
}
```"""
    },
    # Q14
    {
        "id": "cs-q14",
        "number": "14",
        "question": "WAP to input roll, name and marks in 3 subjects of a student and calculate total and percentage using structure.",
        "answer": """```c
#include <stdio.h>

struct student
{
    int roll;
    char name[40];
    float marks[3];
    float total;
    float percentage;
};

int main()
{
    struct student s;
    int i;

    /* Input student details */
    printf("Enter Roll Number: ");
    scanf("%d", &s.roll);

    printf("Enter Name: ");
    scanf("%s", s.name);

    s.total = 0;
    printf("Enter marks in 3 subjects:\\n");
    for(i = 0; i < 3; i++)
    {
        printf("Subject %d: ", i + 1);
        scanf("%f", &s.marks[i]);
        s.total += s.marks[i];
    }

    /* Calculate percentage */
    s.percentage = (s.total / 300.0) * 100.0;

    /* Display mark sheet */
    printf("\\n========== STUDENT REPORT CARD ==========\\n");
    printf("Roll Number : %d\\n", s.roll);
    printf("Name        : %s\\n", s.name);
    printf("Marks       : %.1f, %.1f, %.1f\\n",
           s.marks[0], s.marks[1], s.marks[2]);
    printf("Total Marks : %.2f / 300.00\\n", s.total);
    printf("Percentage  : %.2f%%\\n", s.percentage);

    return 0;
}
```"""
    },
    # Q15
    {
        "id": "cs-q15",
        "number": "15",
        "question": "WAP to input id, name and price of 5 books and display the book with highest price using structure.",
        "answer": """```c
#include <stdio.h>

struct book
{
    int id;
    char name[50];
    float price;
};

int main()
{
    struct book b[5];
    int i, maxIndex;

    /* Input details of 5 books */
    printf("Enter details of 5 books:\\n");
    for(i = 0; i < 5; i++)
    {
        printf("\\nBook %d:\\n", i + 1);
        printf("Enter Book ID: ");
        scanf("%d", &b[i].id);
        printf("Enter Book Name: ");
        scanf("%s", b[i].name);
        printf("Enter Price: ");
        scanf("%f", &b[i].price);
    }

    /* Find the book with maximum price */
    maxIndex = 0;
    for(i = 1; i < 5; i++)
    {
        if(b[i].price > b[maxIndex].price)
        {
            maxIndex = i;
        }
    }

    /* Display highest priced book */
    printf("\\n========== MOST EXPENSIVE BOOK ==========\\n");
    printf("Book ID   : %d\\n", b[maxIndex].id);
    printf("Title     : %s\\n", b[maxIndex].name);
    printf("Price     : Rs. %.2f\\n", b[maxIndex].price);

    return 0;
}
```"""
    },
    # Q16
    {
        "id": "cs-q16",
        "number": "16",
        "question": "WAP to demonstrate the difference between structure and union.",
        "answer": """```c
#include <stdio.h>

/* Structure definition */
struct DemoStruct
{
    int i;
    float f;
    char c;
};

/* Union definition */
union DemoUnion
{
    int i;
    float f;
    char c;
};

int main()
{
    struct DemoStruct s;
    union DemoUnion u;

    /* 1. Difference in memory size */
    printf("Size of Structure = %lu bytes\\n", sizeof(s));
    printf("Size of Union     = %lu bytes\\n", sizeof(u));

    /* 2. Difference in member accessibility */
    printf("\\n--- Structure Demonstration ---\\n");
    s.i = 101;
    s.f = 75.50;
    s.c = 'A';
    printf("Structure members can hold values simultaneously:\\n");
    printf("s.i = %d, s.f = %.2f, s.c = %c\\n", s.i, s.f, s.c);

    printf("\\n--- Union Demonstration ---\\n");
    u.i = 101;
    printf("u.i = %d\\n", u.i);

    u.f = 75.50;
    printf("u.f = %.2f (u.i is now corrupted: %d)\\n", u.f, u.i);

    u.c = 'A';
    printf("u.c = %c (u.f and u.i are overwritten)\\n", u.c);

    return 0;
}
```"""
    },
    # Q17
    {
        "id": "cs-q17",
        "number": "17",
        "question": "WAP to demonstrate nested structure.",
        "answer": """```c
#include <stdio.h>

/* Inner structure */
struct Date
{
    int day;
    int month;
    int year;
};

/* Outer structure containing inner structure */
struct Employee
{
    int id;
    char name[40];
    float salary;
    struct Date joinDate;
};

int main()
{
    struct Employee emp;

    /* Input employee details */
    printf("Enter Employee ID: ");
    scanf("%d", &emp.id);

    printf("Enter Employee Name: ");
    scanf("%s", emp.name);

    printf("Enter Salary: ");
    scanf("%f", &emp.salary);

    printf("Enter Joining Date (Day Month Year): ");
    scanf("%d %d %d", &emp.joinDate.day, &emp.joinDate.month, &emp.joinDate.year);

    /* Display employee details */
    printf("\\n========== EMPLOYEE DETAILS ==========\\n");
    printf("ID           : %d\\n", emp.id);
    printf("Name         : %s\\n", emp.name);
    printf("Salary       : Rs. %.2f\\n", emp.salary);
    printf("Joining Date : %02d/%02d/%04d\\n",
           emp.joinDate.day, emp.joinDate.month, emp.joinDate.year);

    return 0;
}
```"""
    },
    # Q18 (Pointers)
    {
        "id": "cs-q18",
        "number": "18",
        "question": "WAP to find sum and average of two numbers using pointer.",
        "answer": """```c
#include <stdio.h>

int main()
{
    float num1, num2;
    float *p1, *p2;
    float sum, avg;

    /* Assign addresses to pointers */
    p1 = &num1;
    p2 = &num2;

    printf("Enter first number: ");
    scanf("%f", p1);

    printf("Enter second number: ");
    scanf("%f", p2);

    /* Calculation using dereference operator */
    sum = *p1 + *p2;
    avg = sum / 2.0;

    printf("\\nSum     = %.2f\\n", sum);
    printf("Average = %.2f\\n", avg);

    return 0;
}
```"""
    },
    # Q19
    {
        "id": "cs-q19",
        "number": "19",
        "question": "WAP to swap two numbers using call by reference (pointer).",
        "answer": """```c
#include <stdio.h>

/* Function declaration using pointers */
void swap(int *a, int *b);

int main()
{
    int x, y;

    printf("Enter two numbers (x and y): ");
    scanf("%d %d", &x, &y);

    printf("\\nBefore Swapping: x = %d, y = %d\\n", x, y);

    /* Call by reference */
    swap(&x, &y);

    printf("After Swapping : x = %d, y = %d\\n", x, y);

    return 0;
}

/* Function definition */
void swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}
```"""
    },
    # Q20
    {
        "id": "cs-q20",
        "number": "20",
        "question": "WAP to find largest number among elements of an array using pointer.",
        "answer": """```c
#include <stdio.h>

int main()
{
    int arr[10];
    int n, i;
    int *ptr, max;

    printf("Enter number of elements (1 to 10): ");
    scanf("%d", &n);

    ptr = arr; /* Point to first element */

    printf("Enter %d integers:\\n", n);
    for(i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", (ptr + i));
    }

    /* Find largest element using pointer */
    max = *ptr;
    for(i = 1; i < n; i++)
    {
        if(*(ptr + i) > max)
        {
            max = *(ptr + i);
        }
    }

    printf("\\nLargest element = %d\\n", max);

    return 0;
}
```"""
    },
    # Q21
    {
        "id": "cs-q21",
        "number": "21",
        "question": "WAP to find length of a string using pointer.",
        "answer": """```c
#include <stdio.h>

int main()
{
    char str[100];
    char *ptr;
    int length;

    printf("Enter a string: ");
    scanf("%s", str);

    /* Initialize pointer to the beginning of string */
    ptr = str;
    length = 0;

    /* Count characters until null terminator '\\0' */
    while(*ptr != '\\0')
    {
        length++;
        ptr++;
    }

    printf("Length of the string = %d\\n", length);

    return 0;
}
```"""
    },
    # Q22 (File Handling)
    {
        "id": "cs-q22",
        "number": "22",
        "question": "Write down the C program for the following file handling function a. putw() and getw() b. fputc() and fgetc() c. fputs() and fgets()",
        "answer": """### a. Demonstration of putw() and getw() (Integer I/O)
```c
#include <stdio.h>

int main()
{
    FILE *fp;
    int num;

    /* Open file for writing binary integers */
    fp = fopen("numbers.dat", "wb");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    printf("Writing integers to file using putw():\\n");
    putw(100, fp);
    putw(250, fp);
    putw(500, fp);
    fclose(fp);

    /* Open file for reading */
    fp = fopen("numbers.dat", "rb");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    printf("Reading integers from file using getw():\\n");
    while((num = getw(fp)) != EOF)
    {
        printf("%d\\n", num);
    }

    fclose(fp);

    return 0;
}
```

### b. Demonstration of fputc() and fgetc() (Character I/O)
```c
#include <stdio.h>

int main()
{
    FILE *fp;
    char ch;
    char text[] = "Studyroom Class 12 NEB";
    int i;

    /* Open file for character write */
    fp = fopen("chars.txt", "w");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    /* Write character by character using fputc */
    for(i = 0; text[i] != '\\0'; i++)
    {
        fputc(text[i], fp);
    }
    fclose(fp);

    /* Read character by character using fgetc */
    fp = fopen("chars.txt", "r");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    printf("Read characters:\\n");
    while((ch = fgetc(fp)) != EOF)
    {
        putchar(ch);
    }
    printf("\\n");

    fclose(fp);

    return 0;
}
```

### c. Demonstration of fputs() and fgets() (String I/O)
```c
#include <stdio.h>

int main()
{
    FILE *fp;
    char line[100];

    /* Open file for string write */
    fp = fopen("strings.txt", "w");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    /* Write strings using fputs */
    fputs("Kathmandu, Nepal\\n", fp);
    fputs("Fluorescent SS College\\n", fp);
    fclose(fp);

    /* Read strings using fgets */
    fp = fopen("strings.txt", "r");

    if(fp == NULL)
    {
        printf("File cannot be opened.\\n");
        return 1;
    }

    printf("Read lines:\\n");
    while(fgets(line, sizeof(line), fp) != NULL)
    {
        printf("%s", line);
    }

    fclose(fp);

    return 0;
}
```"""
    },
    # Q23 (EXACT format requested by user!)
    {
        "id": "cs-q23",
        "number": "23",
        "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same reading from the file using file handling function. (use structure)",
        "answer": """```c
#include <stdio.h>

struct student
{
    int id;
    char name[30];
    float percentage;
};

int main()
{
    struct student s;
    FILE *fp;
    int i;

    /* Open file for writing */
    fp = fopen("student.txt", "w");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    /* Input and store records */
    for(i = 0; i < 5; i++)
    {
        printf("Enter ID, Name and Percentage: ");
        scanf("%d %s %f", &s.id, s.name, &s.percentage);

        fprintf(fp, "%d %s %.2f\\n",
                s.id, s.name, s.percentage);
    }

    fclose(fp);

    /* Open file for reading */
    fp = fopen("student.txt", "r");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    printf("\\nStudent Records:\\n");

    /* Read and display records */
    while(fscanf(fp, "%d %s %f",
                 &s.id, s.name, &s.percentage) != EOF)
    {
        printf("ID: %d\\n", s.id);
        printf("Name: %s\\n", s.name);
        printf("Percentage: %.2f\\n\\n", s.percentage);
    }

    fclose(fp);

    return 0;
}
```"""
    },
    # Q24
    {
        "id": "cs-q24",
        "number": "24",
        "question": "Write down a C program to input book_id, name and price of 5 books and store it in a file. Display the same reading from the file using file handling function. (don’t use structure)",
        "answer": """```c
#include <stdio.h>

int main()
{
    FILE *fp;
    int book_id;
    char name[50];
    float price;
    int i;

    /* Open file for writing without structure */
    fp = fopen("books_record.txt", "w");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    /* Input and write 5 books */
    for(i = 0; i < 5; i++)
    {
        printf("Enter Book ID, Name and Price: ");
        scanf("%d %s %f", &book_id, name, &price);

        fprintf(fp, "%d %s %.2f\\n", book_id, name, price);
    }

    fclose(fp);

    /* Open file for reading */
    fp = fopen("books_record.txt", "r");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    printf("\\nBook Records from File:\\n");

    /* Read and display records */
    while(fscanf(fp, "%d %s %f", &book_id, name, &price) != EOF)
    {
        printf("Book ID : %d\\n", book_id);
        printf("Title   : %s\\n", name);
        printf("Price   : Rs. %.2f\\n\\n", price);
    }

    fclose(fp);

    return 0;
}
```"""
    },
    # Q25
    {
        "id": "cs-q25",
        "number": "25",
        "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same using file handling function. (use structure and fread() and fwrite() function)",
        "answer": """```c
#include <stdio.h>

struct student
{
    int id;
    char name[30];
    float percentage;
};

int main()
{
    struct student s;
    FILE *fp;
    int i;

    /* Open binary file for writing */
    fp = fopen("students.dat", "wb");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    /* Input and write binary records using fwrite() */
    for(i = 0; i < 5; i++)
    {
        printf("Enter ID, Name and Percentage: ");
        scanf("%d %s %f", &s.id, s.name, &s.percentage);

        fwrite(&s, sizeof(struct student), 1, fp);
    }

    fclose(fp);

    /* Open binary file for reading */
    fp = fopen("students.dat", "rb");

    if(fp == NULL)
    {
        printf("File cannot be opened.");
        return 1;
    }

    printf("\\nStudent Records read using fread():\\n");

    /* Read binary records using fread() */
    while(fread(&s, sizeof(struct student), 1, fp) == 1)
    {
        printf("ID         : %d\\n", s.id);
        printf("Name       : %s\\n", s.name);
        printf("Percentage : %.2f%%\\n\\n", s.percentage);
    }

    fclose(fp);

    return 0;
}
```"""
    }
]

# Group into sections
computer_data = {
    "id": "computer-science",
    "title": "Computer Science",
    "icon": "terminal",
    "description": "C Programming: User-Defined Functions, Recursion, Structures & Unions, Pointers, and Low-Level & High-Level File Handling.",
    "sections": [
        {
            "name": "Function",
            "questions": programs[0:9]
        },
        {
            "name": "Recursive Function",
            "questions": programs[9:12]
        },
        {
            "name": "Structure and Union",
            "questions": programs[12:17]
        },
        {
            "name": "Pointer",
            "questions": programs[17:21]
        },
        {
            "name": "File Handling",
            "questions": programs[21:25]
        }
    ]
}

js_content = "window.COMPUTER_DATA = " + json.dumps(computer_data, indent=2, ensure_ascii=False) + ";\n"
out_file = os.path.join(out_dir, "computer.js")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated updated {out_file} with {len(programs)} programs in requested format.")
