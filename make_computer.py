import json
import os

out_dir = r"C:\Users\Arpan\.gemini\antigravity\scratch\studyroom\data"
os.makedirs(out_dir, exist_ok=True)

computer_data = {
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
                    "answer": """```c
#include <stdio.h>

// Function declaration
void checkOddEven(int num);

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    
    // Function call
    checkOddEven(n);
    
    return 0;
}

// Function definition
void checkOddEven(int num) {
    if (num % 2 == 0) {
        printf("%d is an EVEN number.\\n", num);
    } else {
        printf("%d is an ODD number.\\n", num);
    }
}
```"""
                },
                {
                    "id": "cs-q2",
                    "number": "2",
                    "question": "WAP to display 2, 4, 6, 8, 10……………..….up to nth items using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
void displayEvenSeries(int n);

int main() {
    int terms;
    printf("Enter the number of terms (n): ");
    scanf("%d", &terms);
    
    printf("The series up to %d terms is:\\n", terms);
    displayEvenSeries(terms);
    
    return 0;
}

// Function definition
void displayEvenSeries(int n) {
    for (int i = 1; i <= n; i++) {
        printf("%d", 2 * i);
        if (i < n) {
            printf(", ");
        }
    }
    printf("\\n");
}
```"""
                },
                {
                    "id": "cs-q3",
                    "number": "3",
                    "question": "WAP to find out the factorial of a number using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
long long findFactorial(int n);

int main() {
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    
    if (num < 0) {
        printf("Error: Factorial of a negative number does not exist.\\n");
    } else {
        long long fact = findFactorial(num);
        printf("Factorial of %d = %lld\\n", num, fact);
    }
    
    return 0;
}

// Function definition
long long findFactorial(int n) {
    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
```"""
                },
                {
                    "id": "cs-q4",
                    "number": "4",
                    "question": "WAP to display Fibonacci Series up to nth term using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
void printFibonacci(int n);

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    
    printFibonacci(n);
    
    return 0;
}

// Function definition
void printFibonacci(int n) {
    long long first = 0, second = 1, next;
    
    printf("Fibonacci Series up to %d terms:\\n", n);
    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            printf("%lld", first);
        } else if (i == 2) {
            printf(", %lld", second);
        } else {
            next = first + second;
            first = second;
            second = next;
            printf(", %lld", next);
        }
    }
    printf("\\n");
}
```"""
                },
                {
                    "id": "cs-q5",
                    "number": "5",
                    "question": "WAP to find Multiplication table of the given number using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
void printMultiplicationTable(int num);

int main() {
    int n;
    printf("Enter a number to generate its multiplication table: ");
    scanf("%d", &n);
    
    printMultiplicationTable(n);
    
    return 0;
}

// Function definition
void printMultiplicationTable(int num) {
    printf("\\n--- Multiplication Table of %d ---\\n", num);
    for (int i = 1; i <= 10; i++) {
        printf("%d x %2d = %3d\\n", num, i, num * i);
    }
}
```"""
                },
                {
                    "id": "cs-q6",
                    "number": "6",
                    "question": "WAP to check if a number is palindrome or not using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
int isPalindrome(int num);

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    
    if (isPalindrome(n)) {
        printf("%d is a PALINDROME number.\\n", n);
    } else {
        printf("%d is NOT a palindrome number.\\n", n);
    }
    
    return 0;
}

// Function definition
int isPalindrome(int num) {
    int original = num;
    int reversed = 0, remainder;
    
    if (num < 0) return 0; // Negative numbers are generally not palindromes
    
    while (num > 0) {
        remainder = num % 10;
        reversed = reversed * 10 + remainder;
        num /= 10;
    }
    
    return (original == reversed);
}
```"""
                },
                {
                    "id": "cs-q7",
                    "number": "7",
                    "question": "WAP to check if a number is prime or composite using function.",
                    "answer": """```c
#include <stdio.h>

// Function declaration
void checkPrimeComposite(int num);

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    
    checkPrimeComposite(n);
    
    return 0;
}

// Function definition
void checkPrimeComposite(int num) {
    if (num <= 1) {
        printf("%d is neither prime nor composite.\\n", num);
        return;
    }
    
    int isPrime = 1;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            isPrime = 0;
            break;
        }
    }
    
    if (isPrime) {
        printf("%d is a PRIME number.\\n", num);
    } else {
        printf("%d is a COMPOSITE number.\\n", num);
    }
}
```"""
                },
                {
                    "id": "cs-q8",
                    "number": "8",
                    "question": "WAP to check if a number is Armstrong or not using function.",
                    "answer": """```c
#include <stdio.h>
#include <math.h>

// Function declaration
int isArmstrong(int num);

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    
    if (isArmstrong(n)) {
        printf("%d is an ARMSTRONG number.\\n", n);
    } else {
        printf("%d is NOT an Armstrong number.\\n", n);
    }
    
    return 0;
}

// Function definition
int isArmstrong(int num) {
    int original = num;
    int temp = num;
    int digits = 0;
    int sum = 0;
    
    if (num < 0) return 0;
    
    // Count digits
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    
    temp = num;
    while (temp > 0) {
        int rem = temp % 10;
        sum += (int)round(pow(rem, digits));
        temp /= 10;
    }
    
    return (sum == original);
}
```"""
                },
                {
                    "id": "cs-q9",
                    "number": "9",
                    "question": "WAP to display prime numbers up to nth items using function.",
                    "answer": """```c
#include <stdio.h>

// Function declarations
int isPrime(int num);
void displayFirstNPrimes(int n);

int main() {
    int n;
    printf("Enter the number of prime items to display: ");
    scanf("%d", &n);
    
    displayFirstNPrimes(n);
    
    return 0;
}

int isPrime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

void displayFirstNPrimes(int n) {
    int count = 0;
    int candidate = 2;
    
    printf("First %d prime numbers are:\\n", n);
    while (count < n) {
        if (isPrime(candidate)) {
            printf("%d", candidate);
            count++;
            if (count < n) printf(", ");
        }
        candidate++;
    }
    printf("\\n");
}
```"""
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
                    "answer": """```c
#include <stdio.h>

// Recursive function declaration
long long factorialRec(int n);

int main() {
    int num;
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);
    
    if (num < 0) {
        printf("Error: Factorial of a negative number is undefined.\\n");
    } else {
        printf("Factorial of %d = %lld\\n", num, factorialRec(num));
    }
    
    return 0;
}

// Recursive function definition
long long factorialRec(int n) {
    if (n == 0 || n == 1) {
        return 1; // Base case
    }
    return n * factorialRec(n - 1); // Recursive step
}
```"""
                },
                {
                    "id": "cs-q11",
                    "number": "11",
                    "question": "WAP to find sum of numbers up to n using recursive function.",
                    "answer": """```c
#include <stdio.h>

// Recursive function declaration
int sumOfN(int n);

int main() {
    int n;
    printf("Enter a positive integer n: ");
    scanf("%d", &n);
    
    if (n < 1) {
        printf("Please enter a positive integer.\\n");
    } else {
        printf("Sum of natural numbers up to %d = %d\\n", n, sumOfN(n));
    }
    
    return 0;
}

// Recursive function definition
int sumOfN(int n) {
    if (n == 1) {
        return 1; // Base case
    }
    return n + sumOfN(n - 1); // Recursive step
}
```"""
                },
                {
                    "id": "cs-q12",
                    "number": "12",
                    "question": "WAP to display Fibonacci Series up to nth term using recursive function.",
                    "answer": """```c
#include <stdio.h>

// Recursive function to return the nth Fibonacci number (0-indexed)
int fibonacciRec(int n);

int main() {
    int terms;
    printf("Enter the number of terms (n): ");
    scanf("%d", &terms);
    
    printf("Fibonacci Series up to %d terms:\\n", terms);
    for (int i = 0; i < terms; i++) {
        printf("%d", fibonacciRec(i));
        if (i < terms - 1) {
            printf(", ");
        }
    }
    printf("\\n");
    
    return 0;
}

// Recursive definition
int fibonacciRec(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);
}
```"""
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
                    "answer": """```c
#include <stdio.h>

// Structure definition
struct Student {
    char name[50];
    int roll;
    int age;
    char address[100];
};

int main() {
    struct Student s;
    
    printf("Enter Student Name: ");
    scanf(" %[^\\n]", s.name);
    
    printf("Enter Roll Number: ");
    scanf("%d", &s.roll);
    
    printf("Enter Age: ");
    scanf("%d", &s.age);
    
    printf("Enter Address: ");
    scanf(" %[^\\n]", s.address);
    
    // Display student information
    printf("\\n--- Student Information ---\\n");
    printf("Name    : %s\\n", s.name);
    printf("Roll No : %d\\n", s.roll);
    printf("Age     : %d\\n", s.age);
    printf("Address : %s\\n", s.address);
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q14",
                    "number": "14",
                    "question": "WAP to store name, roll number, age and address of nth students and sort them according to the age using structure.",
                    "answer": """```c
#include <stdio.h>

struct Student {
    char name[50];
    int roll;
    int age;
    char address[100];
};

int main() {
    int n;
    printf("Enter the number of students: ");
    scanf("%d", &n);
    
    struct Student s[n], temp;
    
    for (int i = 0; i < n; i++) {
        printf("\\nEnter details for student %d:\\n", i + 1);
        printf("Name: ");
        scanf(" %[^\\n]", s[i].name);
        printf("Roll Number: ");
        scanf("%d", &s[i].roll);
        printf("Age: ");
        scanf("%d", &s[i].age);
        printf("Address: ");
        scanf(" %[^\\n]", s[i].address);
    }
    
    // Bubble sort ascending by age
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (s[j].age > s[j + 1].age) {
                temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
        }
    }
    
    // Display sorted records
    printf("\\n\\n%-5s %-20s %-8s %-5s %-20s\\n", "S.N.", "Name", "Roll", "Age", "Address");
    printf("------------------------------------------------------------\\n");
    for (int i = 0; i < n; i++) {
        printf("%-5d %-20s %-8d %-5d %-20s\\n", i + 1, s[i].name, s[i].roll, s[i].age, s[i].address);
    }
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q15",
                    "number": "15",
                    "question": "WAP to store name, employee id, salary and address of nth employees and sort them in alphabetical order based on their name using structure.",
                    "answer": """```c
#include <stdio.h>
#include <string.h>

struct Employee {
    char name[50];
    int emp_id;
    float salary;
    char address[100];
};

int main() {
    int n;
    printf("Enter number of employees: ");
    scanf("%d", &n);
    
    struct Employee emp[n], temp;
    
    for (int i = 0; i < n; i++) {
        printf("\\nEnter details for employee %d:\\n", i + 1);
        printf("Name: ");
        scanf(" %[^\\n]", emp[i].name);
        printf("Employee ID: ");
        scanf("%d", &emp[i].emp_id);
        printf("Salary: ");
        scanf("%f", &emp[i].salary);
        printf("Address: ");
        scanf(" %[^\\n]", emp[i].address);
    }
    
    // Alphabetical sort by Name
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (strcmp(emp[j].name, emp[j + 1].name) > 0) {
                temp = emp[j];
                emp[j] = emp[j + 1];
                emp[j + 1] = temp;
            }
        }
    }
    
    // Display sorted employees
    printf("\\n--- Employees in Alphabetical Order ---\\n");
    printf("%-5s %-20s %-8s %-12s %-20s\\n", "S.N.", "Name", "ID", "Salary", "Address");
    printf("-----------------------------------------------------------------\\n");
    for (int i = 0; i < n; i++) {
        printf("%-5d %-20s %-8d Rs.%-9.2f %-20s\\n", i + 1, emp[i].name, emp[i].emp_id, emp[i].salary, emp[i].address);
    }
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q16",
                    "number": "16",
                    "question": "Develop a program in C using structure to ask the information of any 12 students with roll_number, name and marks scored in sub1, sub2, and sub3. Also, display them in proper format along with the calculation of total and percentage. [Note: the full marks of each subject is 100].",
                    "answer": """```c
#include <stdio.h>

#define NUM_STUDENTS 12

struct StudentRecord {
    int roll_number;
    char name[50];
    float sub1;
    float sub2;
    float sub3;
    float total;
    float percentage;
};

int main() {
    struct StudentRecord s[NUM_STUDENTS];
    
    printf("Enter details for %d students:\\n", NUM_STUDENTS);
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("\\n--- Student %d ---\\n", i + 1);
        printf("Roll Number: ");
        scanf("%d", &s[i].roll_number);
        printf("Name: ");
        scanf(" %[^\\n]", s[i].name);
        printf("Marks in Subject 1 (FM: 100): ");
        scanf("%f", &s[i].sub1);
        printf("Marks in Subject 2 (FM: 100): ");
        scanf("%f", &s[i].sub2);
        printf("Marks in Subject 3 (FM: 100): ");
        scanf("%f", &s[i].sub3);
        
        s[i].total = s[i].sub1 + s[i].sub2 + s[i].sub3;
        s[i].percentage = (s[i].total / 300.0f) * 100.0f;
    }
    
    // Display tabulated academic results
    printf("\\n\\n=================================== ACADEMIC MARKSHEET ===================================\\n");
    printf("%-5s %-8s %-20s %-8s %-8s %-8s %-8s %-8s\\n", 
           "S.N.", "Roll", "Name", "Sub1", "Sub2", "Sub3", "Total", "Percent");
    printf("-----------------------------------------------------------------------------------------\\n");
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("%-5d %-8d %-20s %-8.1f %-8.1f %-8.1f %-8.1f %-7.2f%%\\n",
               i + 1, s[i].roll_number, s[i].name, s[i].sub1, s[i].sub2, s[i].sub3, s[i].total, s[i].percentage);
    }
    printf("=========================================================================================\\n");
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q17",
                    "number": "17",
                    "question": "WAP to demonstrate the use of union.",
                    "answer": """```c
#include <stdio.h>
#include <string.h>

// Union definition: members share the exact same memory location
union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    union Data data;
    
    printf("Size of union Data = %lu bytes (size of largest member)\\n\\n", sizeof(data));
    
    // Assigning integer
    data.i = 10;
    printf("After assigning data.i = 10:\\n");
    printf("data.i : %d\\n", data.i);
    
    // Assigning float overwrites integer
    data.f = 220.5;
    printf("\\nAfter assigning data.f = 220.5:\\n");
    printf("data.f : %.2f\\n", data.f);
    printf("data.i (corrupted) : %d\\n", data.i);
    
    // Assigning string overwrites float
    strcpy(data.str, "C Programming");
    printf("\\nAfter assigning data.str = \\"C Programming\\":\\n");
    printf("data.str : %s\\n", data.str);
    printf("data.f (corrupted) : %.2f\\n", data.f);
    
    return 0;
}
```"""
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
                    "answer": """```c
#include <stdio.h>

int main() {
    float length, breadth, area;
    float *ptrL = &length;
    float *ptrB = &breadth;
    float *ptrA = &area;
    
    printf("Enter length of rectangle: ");
    scanf("%f", ptrL);
    
    printf("Enter breadth of rectangle: ");
    scanf("%f", ptrB);
    
    // Calculate area dereferencing pointers
    *ptrA = (*ptrL) * (*ptrB);
    
    printf("\\nArea of Rectangle = %.2f square units\\n", *ptrA);
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q19",
                    "number": "19",
                    "question": "WAP to check a number is odd or even number using Pointer.",
                    "answer": """```c
#include <stdio.h>

int main() {
    int num;
    int *ptr = &num;
    
    printf("Enter an integer: ");
    scanf("%d", ptr);
    
    if (*ptr % 2 == 0) {
        printf("%d is an EVEN number.\\n", *ptr);
    } else {
        printf("%d is an ODD number.\\n", *ptr);
    }
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q20",
                    "number": "20",
                    "question": "WAP to swap two numbers using call by reference.",
                    "answer": """```c
#include <stdio.h>

// Function declaration taking memory addresses
void swapByReference(int *a, int *b);

int main() {
    int x, y;
    printf("Enter two numbers (x and y): ");
    scanf("%d %d", &x, &y);
    
    printf("Before swapping: x = %d, y = %d\\n", x, y);
    
    // Calling by passing references (addresses)
    swapByReference(&x, &y);
    
    printf("After swapping : x = %d, y = %d\\n", x, y);
    
    return 0;
}

// Function definition dereferencing pointers
void swapByReference(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```"""
                },
                {
                    "id": "cs-q21",
                    "number": "21",
                    "question": "WAP to swap two numbers using call by value.",
                    "answer": """```c
#include <stdio.h>

// Function declaration taking copies of values
void swapByValue(int a, int b);

int main() {
    int x, y;
    printf("Enter two numbers (x and y): ");
    scanf("%d %d", &x, &y);
    
    printf("Before swapping in main: x = %d, y = %d\\n", x, y);
    
    // Calling by value
    swapByValue(x, y);
    
    printf("After swapping in main (unchanged): x = %d, y = %d\\n", x, y);
    
    return 0;
}

// Function definition modifying only local copies
void swapByValue(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swapByValue function: a = %d, b = %d\\n", a, b);
}
```"""
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
                    "answer": """### a. Demonstration of putw() and getw() (Integer I/O)
```c
#include <stdio.h>

int main() {
    FILE *fp;
    int num;
    
    // Writing integers
    fp = fopen("numbers.dat", "wb");
    if (fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    
    printf("Writing integers 10, 20, 30 to numbers.dat...\\n");
    putw(10, fp);
    putw(20, fp);
    putw(30, fp);
    fclose(fp);
    
    // Reading integers
    fp = fopen("numbers.dat", "rb");
    printf("Reading integers from file:\\n");
    while ((num = getw(fp)) != EOF) {
        printf("%d ", num);
    }
    printf("\\n");
    fclose(fp);
    
    return 0;
}
```

---

### b. Demonstration of fputc() and fgetc() (Character I/O)
```c
#include <stdio.h>

int main() {
    FILE *fp;
    char ch;
    
    // Writing characters
    fp = fopen("char_test.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    
    char text[] = "Hello NEB Class 12!";
    for (int i = 0; text[i] != '\\0'; i++) {
        fputc(text[i], fp);
    }
    fclose(fp);
    
    // Reading characters
    fp = fopen("char_test.txt", "r");
    printf("Reading file character by character:\\n");
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }
    printf("\\n");
    fclose(fp);
    
    return 0;
}
```

---

### c. Demonstration of fputs() and fgets() (String I/O)
```c
#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[100];
    
    // Writing string lines
    fp = fopen("strings.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    
    fputs("First line written using fputs().\\n", fp);
    fputs("Fluorescent SS/+2 College, Tokha.\\n", fp);
    fclose(fp);
    
    // Reading string lines
    fp = fopen("strings.txt", "r");
    printf("Reading file line by line using fgets():\\n");
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    fclose(fp);
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q23",
                    "number": "23",
                    "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same reading from the file using file handling function. (use structure)",
                    "answer": """```c
#include <stdio.h>

struct Student {
    int id;
    char name[50];
    float percent;
};

int main() {
    struct Student s[5], r;
    FILE *fp;
    
    // Input 5 students
    printf("Enter details of 5 students:\\n");
    for (int i = 0; i < 5; i++) {
        printf("\\nStudent %d:\\n", i + 1);
        printf("ID: ");
        scanf("%d", &s[i].id);
        printf("Name: ");
        scanf(" %[^\\n]", s[i].name);
        printf("Percentage: ");
        scanf("%f", &s[i].percent);
    }
    
    // Writing to file using fprintf
    fp = fopen("students_info.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    for (int i = 0; i < 5; i++) {
        fprintf(fp, "%d %s %f\\n", s[i].id, s[i].name, s[i].percent);
    }
    fclose(fp);
    
    // Reading from file using fscanf
    fp = fopen("students_info.txt", "r");
    if (fp == NULL) {
        printf("Error reading file!\\n");
        return 1;
    }
    
    printf("\\n\\n--- Records Read From File ---\\n");
    printf("%-8s %-20s %-12s\\n", "ID", "Name", "Percentage");
    printf("----------------------------------------\\n");
    while (fscanf(fp, "%d %s %f", &r.id, r.name, &r.percent) == 3) {
        printf("%-8d %-20s %-6.2f%%\\n", r.id, r.name, r.percent);
    }
    fclose(fp);
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q24",
                    "number": "24",
                    "question": "Write down a C program to input book_id, name and price of 5 books and store it in a file. Display the same reading from the file using file handling function. (don’t use structure)",
                    "answer": """```c
#include <stdio.h>

int main() {
    FILE *fp;
    int book_id;
    char name[50];
    float price;
    
    // Writing 5 books without structure
    fp = fopen("books_record.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    
    printf("Enter details for 5 books:\\n");
    for (int i = 0; i < 5; i++) {
        printf("\\nBook %d:\\n", i + 1);
        printf("Book ID: ");
        scanf("%d", &book_id);
        printf("Book Name (single-word or underscored): ");
        scanf("%s", name);
        printf("Price: ");
        scanf("%f", &price);
        
        fprintf(fp, "%d %s %.2f\\n", book_id, name, price);
    }
    fclose(fp);
    
    // Reading and displaying from file
    fp = fopen("books_record.txt", "r");
    if (fp == NULL) {
        printf("Error opening file for reading!\\n");
        return 1;
    }
    
    printf("\\n\\n--- Book Inventory from File ---\\n");
    printf("%-10s %-25s %-10s\\n", "Book ID", "Title", "Price (Rs)");
    printf("----------------------------------------------\\n");
    while (fscanf(fp, "%d %s %f", &book_id, name, &price) == 3) {
        printf("%-10d %-25s Rs. %-8.2f\\n", book_id, name, price);
    }
    fclose(fp);
    
    return 0;
}
```"""
                },
                {
                    "id": "cs-q25",
                    "number": "25",
                    "question": "Write down a C program to input id, name and percent of 5 students and store it in a file. Display the same using file handling function. (use structure and fread() and fwrite() function)",
                    "answer": """```c
#include <stdio.h>

struct Student {
    int id;
    char name[50];
    float percent;
};

int main() {
    struct Student s[5], temp;
    FILE *fp;
    
    // Input 5 students
    printf("Enter details of 5 students for binary storage:\\n");
    for (int i = 0; i < 5; i++) {
        printf("\\nStudent %d:\\n", i + 1);
        printf("ID: ");
        scanf("%d", &s[i].id);
        printf("Name: ");
        scanf(" %[^\\n]", s[i].name);
        printf("Percentage: ");
        scanf("%f", &s[i].percent);
    }
    
    // Binary write using fwrite()
    fp = fopen("students.bin", "wb");
    if (fp == NULL) {
        printf("Error opening file for writing!\\n");
        return 1;
    }
    fwrite(s, sizeof(struct Student), 5, fp);
    fclose(fp);
    printf("\\nRecords successfully written to binary file.\\n");
    
    // Binary read using fread()
    fp = fopen("students.bin", "rb");
    if (fp == NULL) {
        printf("Error opening file for reading!\\n");
        return 1;
    }
    
    printf("\\n--- Displaying Records Read via fread() ---\\n");
    printf("%-8s %-25s %-12s\\n", "ID", "Name", "Percentage");
    printf("----------------------------------------------\\n");
    while (fread(&temp, sizeof(struct Student), 1, fp) == 1) {
        printf("%-8d %-25s %-6.2f%%\\n", temp.id, temp.name, temp.percent);
    }
    fclose(fp);
    
    return 0;
}
```"""
                }
            ]
        }
    ]
}

with open(os.path.join(out_dir, "computer.js"), "w", encoding="utf-8") as f:
    f.write("window.COMPUTER_DATA = " + json.dumps(computer_data, indent=2, ensure_ascii=False) + ";\n")

print("Wrote computer.js successfully")
