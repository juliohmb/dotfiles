int leds[5] = {4, 5, 6, 7, 9};

byte Transmissor = 3;
byte Receptor = 2;

float tempo = 0;
float presenca = 0;

int contador = 0;
int contador2;
int EN;

  void setup()
  {
    pinMode(Receptor,INPUT);
    pinMode(12,OUTPUT);
    pinMode(Transmissor, OUTPUT);
    pinMode(8, INPUT);

    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(9, OUTPUT);
    
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

    Serial.println(EN);
    if(presenca<=310)
      {
        if(EN==0)   // Liga quando não tem energia
        {
          while(contador <10)
          {
            for(contador2=0 ; contador2<5 ; contador2 ++)
            {
                digitalWrite(leds[contador2], LOW);
            }
            
            digitalWrite(leds[contador], HIGH);

            digitalWrite(12,HIGH);
            delay(500);
            digitalWrite(12,LOW);
            delay(500);
            contador=contador+1;
          }
          contador =0;
          for(contador2=0; contador2<5; contador2++)
          {
            digitalWrite(leds[contador2], LOW);
          }
        }
        else    // Comportamento padrão
        {
          while(contador<10)
          {
            for(contador2=0; contador2<5; contador2++)
            {
               digitalWrite(leds[contador2], HIGH);
            }
            digitalWrite(12,HIGH);
            delay(500);
            digitalWrite(12,LOW);
            delay(500);
            contador=contador+1;
          }
          contador=0;
          for(contador2=0; contador2<5; contador2++)
          {
            digitalWrite(leds[contador2], LOW);
          }
        }
        delay(100);
      }
    
  }