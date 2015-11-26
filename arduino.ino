boolean led_status;
const int led_pin = 5;

void setup()
{
	Serial.begin(9600);
	pinMode(led_pin, OUTPUT);
	digitalWrite(led_pin, LOW);
	led_status = false;
}

void loop()
{
	digitalWrite(led_pin, led_status ? HIGH : LOW);
	if(Serial.available() > 0)
	{
		int n = Serial.parseInt();
		switch(n)
		{
			case 0:
				led_status = false;
				Serial.println("OFF");
				break;

			case 1:
				led_status = true;
				Serial.println("ON");
				break;

			case -1:
				Serial.println(led_status ? "ON" : "OFF");
				break;

			default:
				Serial.println("ERROR: Unknown command.");
				break;
		}
	}
}

