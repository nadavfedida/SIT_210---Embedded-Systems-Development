const int LED_PIN = D5;
SYSTEM_THREAD(ENABLED);

void setup() {
    pinMode(LED_PIN, OUTPUT);
	Particle.subscribe("Deakin_RIOT_SIT210_Photon_Buddy", myHandler);
}

void loop() {
    int state = 0;
    if (state == 0)
    {
        Particle.publish("Deakin_RIOT_SIT210_Photon_Buddy", "wave", PUBLIC);
        state = 1;
        delay(10000);
    }
    if (state == 1)
    {
        Particle.publish("Deakin_RIOT_SIT210_Photon_Buddy", "pat", PUBLIC);
        state = 0;
        delay(10000);
    }
}

void myHandler(const char *event, const char *data) {
    //String comparer - looking for "wave"
	if (strcmp(data, "wave") == 0) 
    {
        for (int i = 0; i < 3; i++) {
            digitalWrite(LED_PIN, HIGH);
            delay(500);
            digitalWrite(LED_PIN, LOW);
            delay(500);
        }
        // Particle.publish("WAVE", String("WAVE_RECIEVED_NADAV"), PRIVATE);
    }
    //String comparer - looking for "pat"
	else if (strcmp(data, "pat") == 0) 
	{
        for (int i = 0; i < 12; i++) {
            digitalWrite(LED_PIN, HIGH);
            delay(80);
            digitalWrite(LED_PIN, LOW);
            delay(80);
        }  
        // Particle.publish("WAVE", String("PAT_RECIEVED_NADAV"), PRIVATE);

    }
}

