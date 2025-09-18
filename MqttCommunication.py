import sys
import time as time
import time
import threading
import paho.mqtt.client as mqtt

class MqttCommunication:
    def __init__(self):
        self.message = None
        self.message_event = threading.Event()
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        client.subscribe("connection")

    def on_message(self, client, userdata, msg):
        self.message = str(msg.payload.decode())
        self.message_event.set()
        print(self.message)

        def start_communication(self):
            import threading
            thread = threading.Thread(target=self.communication_thread)
            thread.daemon = True
            thread.start()

    def communication_thread(self):
        self.mqttc.connect("localhost", 1883, 60)
        self.mqttc.loop_forever()
        
    def send_message(self, topic, payload):
        self.mqttc.publish(topic, payload)

    def reset_message(self):
        self.message = None
        self.message_event.clear()
        
    def wait_for_message(self):
        self.message_event.wait()
    def wait_for_message(self):
        while self.message is None:
            time.sleep(0.5)


if __name__ == "__main__":
    client = MqttCommunication()
    client.start_communication()
