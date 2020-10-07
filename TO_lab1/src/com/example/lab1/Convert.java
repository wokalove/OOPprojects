package com.example.lab1;

import java.util.Scanner;

public class Convert {
    static double to_currency = 4.23;
    static double from_currency;
    static double user_input;

    static double convert(double value,String curr) {
        double new_value =0;
        if (curr.equals("EUR")){
            new_value=value/ to_currency;
            System.out.println(new_value);
        }
        return new_value;
    }

    static void ask_for_inputs(){
        Scanner input = new Scanner(System.in);
        double value1 = 0.00, value2 = 0.00;
        String currency;

        System.out.print("Enter a value: ");
        value1 = input.nextDouble();
        input.nextLine();
        System.out.print("EUR OR USD: ");
        currency = input.nextLine();
        System.out.println(currency);

        System.out.println(convert(value1, currency));

    }

    public static void main(String[] args) {
        ask_for_inputs();

    }
}
