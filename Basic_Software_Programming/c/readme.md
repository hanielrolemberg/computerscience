# Fahrenheit to Celsius Converter

This is a simple C program that converts temperatures from Fahrenheit to Celsius. The program demonstrates basic functionality by converting a pre-set Fahrenheit value and printing both the Fahrenheit and Celsius values.

## File Name

`converter.c`

## How It Works

The program uses a function `toCelsius()` to convert a Fahrenheit value to Celsius using the formula:


In the `main()` function, a Fahrenheit value of `98.8` is passed to the `toCelsius()` function, and both the Fahrenheit and Celsius values are printed to the console.

## Code Example

```c
#include <stdio.h>

// Function to convert Fahrenheit to Celsius
float toCelsius(float fahrenheit) {
  return (5.0 / 9.0) * (fahrenheit - 32.0);
}

int main() {
  // Set a fahrenheit value
  float f_value = 98.8;
  
  // Call the function with the fahrenheit value
  float result = toCelsius(f_value);

  // Print the fahrenheit value
  printf("Fahrenheit: %.2f\n", f_value);
  
  // Print the result
  printf("Convert Fahrenheit to Celsius: %.2f\n", result);

  return 0;
}
