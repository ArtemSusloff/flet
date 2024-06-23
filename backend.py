import paho.mqtt.client as mqttclient
# from fletTest import test_call


class Backend:
    def __init__(self):
        self.client = client = mqttclient.Client(mqttclient.CallbackAPIVersion.VERSION1)
        self.connect_state = False
        self.address = ""
        self.port = 1883
        self.topic = ""

    def get_signal(self):
        return True


    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("client connect")
            client.loop_start()
            client.subscribe(self.topic)
            self.connect_state = True
        else:
            self.connect_state = True
            print("client is not connected")

    def __on_disconnect(self, client, userdata, rc):
        if rc != 0:
            self.connect_state = False
            # self.client.connect(self.address, port=self.port)
            # self.client.subscribe(self.topic)
            # self.client.loop_start()
            print("MQTT reconnect")

    def __on_messages(self, client, userdata, message):
        m_str = str(message.payload.decode("utf-8"))
        self.get_signal()
        try:
            my_dict = eval(m_str)
            # self.smab_db.add_record(my_dict)
            # self.upload.convert_excel(my_dict)
            # self.upload.convert_excel_form(my_dict)
        except:
            pass

    def connect_client(self, address, topic):
        self.address = address
        self.topic = topic
        self.client.connect(address, port=1883)
        self.client.subscribe(topic)
        self.client.on_connect = self.__on_connect
        self.client.on_disconnect = self.__on_disconnect
        self.client.on_message = self.__on_messages
        self.client.loop_start()
