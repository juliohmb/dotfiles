#include <IRremote.h>
#include <Adafruit_NeoPixel.h>
#define PIN 13
#define NUMPIXELS 10

int leds[5] = {4, 5, 6, 7, 9};

byte Transmissor = 3;
byte Receptor = 2;

float tempo = 0;
float presenca = 0;

int contador = 0;
int contador2;
int EN;

int redColor = 0;
int greenColor = 255;
int blueColor =0;

  void setup()
  {
    pinMode(Receptor,INPUT);
    pinMode(12,OUTPUT);
    pinMode(Transmissor, OUTPUT);
    pinMode(8, INPUT);
    
    digitalWrite(12, LOW);
    digitalWrite(Transmissor, LOW);
    
    Serial.begin(9600);
  	Serial.println("O Arduino foi iniciado!");
  }
  void loop()
  {
    EN = digitalRead(8);
    digitalWrite(Transmissor,HIGH);
    delayMicroseconds(10);
    digitalWrite(Transmissor, LOW);

    tempo = pulseIn(Receptor, HIGH);

    presenca = tempo/20 * 0.343;
    Serial.println(presenca);

    if(presenca<=310)
      {
        if(EN==0)
        {
          while(contador <10)
          {
            for(contador2=0 ; contador2<=9 ; contador2 ++)
            {
                pixels.setPixelColor(contador2 , pixels.Color(redColor, greenColor, blueColor));
            }
            pixels.setPixelColor(contador, pixels.Color(255, 255, 0));
            pixels.show();

            digitalWrite(12,HIGH);
            delay(500);
            digitalWrite(12,LOW);
            delay(500);
            contador=contador+1;
          }
          contador =0;
          for(contador2=0; contador2<=9; contador2++)
          {
            pixels.setPixelColor(contador2, pixels.Color(0, 0, 0));
          }
          pixels.show();
        }
        else
        {
          while(contador<10)
          {
            for(contador2=0; contador2<=9; contador2++)
            {
               pixels.setPixelColor(contador2, pixels.Color(255, 255, 0));
            }
            pixels.show();
            digitalWrite(12,HIGH);
            delay(500);
            digitalWrite(12,LOW);
            delay(500);
            contador=contador+1;
          }
          contador=0;
          for(contador2=0; contador2<=9; contador2++)
          {
            pixels.setPixelColor(contador2, pixels.Color(0, 0, 0));
          }
          pixels.show();
        }
        delay(100);
      }
    
  }