
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char category;
    int tempSelect;
    float tempF, tempC, FahrenheitToCelsius, CelsiusToFahrenheit;
    int currencySelect;
    float amountINR, amountUSD, amountEURO, INRtoUSD, USDtoINR, INRtoEURO, EUROtoINR;
    int massSelect;
    float massKg, massPounds, PoundstoKG, KGtoPounds;
    int lengthSelect;
    float lengthKm, KMtoMiles, lengthMiles, MilestoKm, lengthCm, CMtoFeet, lengthFeet, FeettoCM;F

    printf("\n*** Unit Convertor Calculator ***\n\n");
    printf("List of conversions to choose from:\n ");
    printf("1. Temperature(T)\n 2. Currency(C)\n 3. Mass(M)\n 4. Length(L)\n ");
    printf("Enter the letter you want to convert: ");
    scanf("%c", &category);

    if (category == 'T')
    {
        printf("\n** Temperature Converter **\n");
        printf("Enter 1 for Celsius to Fahrenheit.\n");
        printf("Enter 2 for Fahrenheit to Celsius.\n\n");
        scanf("%d", &tempSelect);
        if (tempSelect == 1)
        {
            printf("Enter the temperature in Celsius: ");
            scanf("%f", &tempC);
            CelsiusToFahrenheit = ((9.0 / 5.0) * tempC + 32);
            printf("%0.2f Celcius  in Fahrenheit is: %0.2f", tempC, CelsiusToFahrenheit);
        }
        else if (tempSelect == 2)
        {
            printf("Enter the temperature in Fahrenheit: ");
            scanf("%f", &tempF);
            FahrenheitToCelsius = ((tempF - 32) * (5.0 / 9.0));
            printf("%0.2f Fahrenheit in Celcius is: %0.2f", tempF, FahrenheitToCelsius);
        }
        else
        {
            printf("Wrong Input! Please enter the correct input.\n");
        }
    }

    else if (category == 'C')
    {
        printf("\n** Currency Converter **\n");
        printf("Enter 1 for INR to USD.\n");
        printf("Enter 2 for USD to INR.\n");
        printf("Enter 3 for INR to EURO.\n");
        printf("Enter 4 for EURO to INR.\n\n");
        scanf("%d", &currencySelect);

        if (currencySelect == 1)
        {
            printf("Enter amount in INR: ");
            scanf("%f", &amountINR);
            INRtoUSD = amountINR * 0.013;
            printf("RS. %0.2f is equal to %0.2f $", amountINR, INRtoUSD);
        }
        else if (currencySelect == 2)
        {
            printf("Enter amount in USD: ");
            scanf("%f", &amountUSD);
            USDtoINR = amountUSD * 76.52;
            printf("$ %0.2f is equal to RS. %0.2f", amountUSD, USDtoINR);
        }
        else if (currencySelect == 3)
        {
            printf("Enter amount in INR: ");
            scanf("%f", &amountINR);
            INRtoEURO = amountINR * 0.012;
            printf("RS. %0.2f is equal to %0.2f Euros", amountINR, INRtoEURO);
        }
        else if (currencySelect == 4)
        {
            printf("Enter amount in EURO: ");
            scanf("%f", &amountEURO);
            EUROtoINR = amountEURO * 82.54;
            printf("%0.2f Euros is equal to RS. %0.2f", amountEURO, EUROtoINR);
        }
        else
        {
            printf("Wrong Input! Please enter the correct input.\n");
        }
    }
    else if (category == 'M')
    {
        printf("\n** Mass Converter **\n");
        printf("Enter 1 for kg to pounds.\n");
        printf("Enter 2 for pounds to kg.\n");
        scanf("%d", &massSelect);

        if (massSelect == 1)
        {
            printf("Enter the mass in kg: ");
            scanf("%f", &massKg);
            KGtoPounds = massKg * 2.20;
            printf("%0.2f kg is equal to %0.2f pounds", massKg, KGtoPounds);
        }
        else if (massSelect == 2)
        {
            printf("Enter the mass in pounds: ");
            scanf("%f", &massPounds);
            PoundstoKG = massPounds * 0.45;
            printf("%0.2f pounds is equal to %0.2f kg", massPounds, PoundstoKG);
        }
        else
        {
            printf("Wrong Input! Please enter the correct input.\n");
        }
    }
    else if (category == 'L')
    {
        printf("\n** Length Converter **\n");
        printf("Enter 1 for km to miles.\n");
        printf("Enter 2 for miles to km.\n");
        printf("Enter 3 for cm to feet.\n");
        printf("Enter 4 for feet to cm.\n");
        scanf("%d", &lengthSelect);

        if (lengthSelect == 1)
        {
            printf("Enter the length in km: ");
            scanf("%f", &lengthKm);
            KMtoMiles = lengthKm * 0.62;
            printf("%0.2f km is equal to %0.2f Miles", lengthKm, KMtoMiles);
        }
        else if (lengthSelect == 2)
        {
            printf("Enter the length in miles: ");
            scanf("%f", &lengthMiles);
            MilestoKm = lengthMiles * 1.6;
            printf("%0.2f Miles is equal to %0.2f km", lengthMiles, MilestoKm);
        }
        else if (lengthSelect == 3)
        {
            printf("Enter the length in cm: ");
            scanf("%f", &lengthCm);
            CMtoFeet = lengthCm * 0.032;
            printf("%0.2f cm is equal to %0.2f feet", lengthCm, CMtoFeet);
        }
        else if (lengthSelect == 4)
        {
            printf("Enter the length in feet: ");
            scanf("%f", &lengthFeet);
            FeettoCM = lengthFeet * 30.48;
            printf("%0.2f feet is equal to %0.2f cm", lengthFeet, FeettoCM);
        }
        else
        {
            printf("Wrong Input! Please enter the correct inut.\n");
        }
    }
    else {
                    printf("Wrong Input! Please enter the correct input.\n");

    }
    
    return 0;
}

