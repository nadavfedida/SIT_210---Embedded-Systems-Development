#include <MQTT.h>
#include <SparkJson.h>
// create a JSON object
int Gate1 = D5; 
int Gate2 = D6; 
int Gate3 = D7; 

StaticJsonBuffer<200> jsonBuffer;
JsonObject& root = jsonBuffer.createObject();

// MQTT callback
void callback(char* topic, byte* payload, unsigned int length);
// MQTT client
MQTT client("test.mosquitto.org", 1883, callback);


void setup() {
	pinMode(Gate1, OUTPUT);
	pinMode(Gate2, OUTPUT);
	pinMode(Gate3, OUTPUT);
	
	// connect to MQTT server
	client.connect("particle_dust");
	
	// MQTT subscribe
	if(client.isConnected()) {
		client.subscribe("SIT210_nadav");
	}
	
}

void loop() {
	// generate the JSON string
	char output[200];
	root.printTo(output, sizeof(output));
	delay(1000);
	client.loop();
	
}

// MQTT call back function
void callback(char* topic, byte* payload, unsigned int length) {
	char p[length + 1];
	memcpy(p, payload, length);
	p[length] = NULL;
	if (strcmp(p, "nadav") == 0)
	{
		Particle.publish("Particle Publish", 
		"Gate 1 opened", 60, PRIVATE);
		digitalWrite(Gate1, HIGH);
		delay(1000); // 1 second
		digitalWrite(Gate1, LOW);
	}
	if (strcmp(p, "tom") == 0)
	{
		Particle.publish("Particle Publish", 
		"Gate 2 opened", 60, PRIVATE);
		digitalWrite(Gate2, HIGH);
		delay(1000); // 1 second
		digitalWrite(Gate2, LOW);
	}
	if (strcmp(p, "will") == 0)
	{
		Particle.publish("Particle Publish", 
		"Gate 3 opened", 60, PRIVATE);
		digitalWrite(Gate3, HIGH);
		delay(1000); // 1 second
		digitalWrite(Gate3, LOW);
	}
}