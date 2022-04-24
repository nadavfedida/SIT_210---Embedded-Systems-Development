//Defining D7 to Led2 - which is the built in LED 
int led2 = D7; 

//A few local functions to perform different tasks with the built in LED
void High() {
    digitalWrite(led2, HIGH);
    delay(1000);
    digitalWrite(led2, LOW);
}

void Low() {
    digitalWrite(led2, HIGH);
    delay(500);
    digitalWrite(led2, LOW);
}

void Delay() {
    delay(500);
}

void Gap() {
    delay(1000);
}
    
//A function to take in any string and convert it to Morse code
void blinkName(String STRING){
    
    //S = tolower(STRING);
    for (int i=0; i < sizeof(STRING -1 ); i++)
    {
        Gap();
        if (STRING[i] == 'a') // A * -
        {
            High();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'b') // B - * * *
        {
            Low();
            Delay();
            High();
            Delay();
            High();  
            Delay();
            High();
        }
        
        if (STRING[i] == 'c') // C - * - *
        {
            Low();
            Delay();
            High();  
            Delay();
            Low();
            Delay();
            High();  
        }
        
        if (STRING[i] == 'd') // D - * *
        {
            Low();
            Delay();
            High();  
            Delay();
            High();  
        }
        
        if (STRING[i] == 'e') // E *
        {
            High();
        }
        
        if (STRING[i] == 'f') // F * * - *
        {
            High();  
            Delay();
            High();
            Delay();
            Low();
            Delay();
            High();

        }
        
        if (STRING[i] == 'g') // G - - *
        {
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'h') // H * * * *
        {
            High();
            Delay();
            High();
            Delay();
            High();
            Delay();
            High();
        }
        
        
        if (STRING[i] == 'i') // I * *
        {
            High();
            Delay();
            High();
        }
        
        if (STRING[i] == 'j') // J * - - - 
        {
            High();
            Delay();
            Low();
            Delay();
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'k') // K - * - 
        {
            Low();
            Delay();
            High();
            Delay();
            Low();

        }
        
        if (STRING[i] == 'l') // L * * - * 
        {
            High();
            Delay();
            High();
            Delay();
            Low();
            Delay();
            High();
        }
        
        if (STRING[i] == 'm') // M - -  
        {
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'n') // N - *  
        {
            Low();
            Delay(); 
            High();
        }
        
        if (STRING[i] == 'o') // O - - - 
        {
            Low();
            Delay();
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'p') // P * - - *  
        {
            High();
            Delay();
            Low();
            Delay();
            Low();
            Delay();
            High();
        }
        
        if (STRING[i] == 'q') // Q - - * -  
        {
            Low();
            Delay();
            Low();
            Delay();
            High();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'r') // R * - *  
        {
            High();
            Delay();
            Low();
            Delay();
            High();
        }
        
        if (STRING[i] == 's') // S * * *  
        {
            Low();
            Delay();
            High();
        }
        
        if (STRING[i] == 't') // T -   
        {
            Low();
        }
        
        if (STRING[i] == 'u') // U * * -  
        {
            High();
            Delay();
            High();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'v') // V * * * -  
        {
            High();
            Delay();
            High();
            Delay();
            High();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'w') // W * - -  
        {
            High();
            Delay();
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'x') // X - * * - 
        {
            Low();
            Delay();
            High();
            Delay();
            High();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'y') // Y - * - - 
        {
            Low();
            Delay();
            High();
            Delay();
            Low();
            Delay();
            Low();
        }
        
        if (STRING[i] == 'z') // Z - - * *  
        {
            Low();
            Delay();
            Low();
            Delay();
            High();
            Delay();
            High();
        }
        Delay();
    }
}

// Enables the LED to start blinking before cloud connection is established 
SYSTEM_THREAD(ENABLED);


void setup() {
  pinMode(led2, OUTPUT);
  
}

void loop() {
    blinkName("nadav"); // calling my fucntion with my first name as the input
    
    delay(1000);

    //blinkName("FEDIDA"); // comment out to enable the last name to be converted 
    
    // flashing lights to indicate word is over
    delay(50);
    digitalWrite(led2, HIGH);
    delay(50);
    digitalWrite(led2, LOW);
    delay(50);
    digitalWrite(led2, HIGH);
    delay(50);
    digitalWrite(led2, LOW);
    delay(50);
    digitalWrite(led2, HIGH);
    delay(50);
    digitalWrite(led2, LOW);

}
