#include <stdio.h>

int main() {
    
    // Conditional Statement

    
    /* Traffic Light Control System

    Problem: Simulate a basic traffic light that changes behavior based on light color input (Red, Yellow, Green). */

    



    // print if a number is even or odd.

    /* int number;
    scanf("%d", &number);

    if (number % 2 == 0) {
        printf("Even Number");
    } else {
        printf("Odd Number");
    } */

    
    // positive, negative, zero.

    // printf("Enter the number here: ");

    // int number;
    // scanf("%d", &number);

    // if (number > 0) {
    //     printf("Positive");
    // } else if (number < 0) {
    //     printf("Negative");
    // } else {
    //     printf("Zero");
    // }

    printf("Enter your marks? ");

    int marks;
    scanf("%d", &marks);

    if (marks > 100 || marks < 0) {
        printf("Wrong marks entered");
    } else if (marks >= 90) {
        printf("A");
    } else if (marks >= 80) {
        printf("B");
    } else if (marks >= 70) {
        printf("C");
    } else if (marks >= 60) {
        printf("D");
    } else if (marks >= 50) {
        printf("E");
    } else {
        printf("F");
    }

    return 0;
}