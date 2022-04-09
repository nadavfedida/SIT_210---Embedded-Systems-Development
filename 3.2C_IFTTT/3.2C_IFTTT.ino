#define LUX_LEVEL A0
#define LED D6


// int temperature;


int SUN_SHINING;
int LuxLevelReading;

void setup() {
    pinMode(LUX_LEVEL, INPUT);
    pinMode(LED, OUTPUT);
}

void loop() {
    int ave_lux;
    int lux_total;
    String NO_SUN;
    String SUN;


    //gathering an average over 5 seconds for the LUX level
    for (int i = 0; i < 10; i++){
        LuxLevelReading = analogRead(LUX_LEVEL);
        lux_total += LuxLevelReading;
        delay(500);
    }
    ave_lux = (lux_total / 10); 
     if (ave_lux > 2900 & SUN_SHINING == 0){
        SUN_SHINING = 1;
        digitalWrite(LED, HIGH);
        Particle.publish("Light_level", String("SUN"), PRIVATE);
        
    }
    
    if (ave_lux < 2900 & SUN_SHINING == 1){
        SUN_SHINING = 0;
        digitalWrite(LED, LOW);
        Particle.publish("Light_level", String("NO_SUN"), PRIVATE);
    }
    ave_lux = 0;
}




 
