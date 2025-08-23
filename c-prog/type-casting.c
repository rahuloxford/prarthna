#include <stdio.h>

int main() {

    // type casting? [convert one type of data into another]

    // automatic (implicit casting)
    int number = 43.25;
    printf("number: %d\n", number);

    float number2 = 29;
    printf("number2: %f\n", number2);

    // manual (explicit casting)
    float result = (float)5 / 2; // (int / int = int)
    printf("result: %f", result);


    return 0;
}