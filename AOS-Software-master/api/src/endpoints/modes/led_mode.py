from flask import Blueprint, jsonify, request
from src.endpoints.modes.utils import MODES
from threading import Thread
from src.connections.arduino import ArduinoConn, SLAVE_ADDRESS


LED_ON = False

TURNING_LED_ON = "Turning The LED ON.."
LED_ALREADY_ON = "The LED is already ON"
TURNING_LED_OFF = "Turung The LED OFF.."
LED_ALREADY_OFF = "The LED is already OFF"

def led_on():
  global LED_ON
  if not LED_ON :
      print("turning the LED ON..")
      # here the code to send the request for the arduino to turn on the LED
      ArduinoConn.write_byte(SLAVE_ADDRESS, MODES.get("LED_ON_MODE"))
      LED_ON = True
  else:
      print("the LED is already ON!")

def led_off():
  global LED_ON
  if LED_ON :
      print("turning the LED OFF..")
      # here the code to send the request for the arduino to turn on the LED
      ArduinoConn.write_byte(SLAVE_ADDRESS, MODES.get("LED_OFF_MODE"))
      LED_ON = False
  else:
      print("the LED is already OFF!")

led_on_mode = Blueprint(name="led_on_mode", import_name=__name__)
led_off_mode = Blueprint(name="led_off_mode", import_name=__name__)

@led_on_mode.route('/run', methods=['GET'])
def led_on_run():
    """
    ---
    get:
      description: This is what turns on the LED
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing
    """
    output = {
      "msg": "",
      "led_on":""
    }
    # this should start the video 
    led_process = Thread(target=led_on, args=())
    led_process.start()

    if(not LED_ON):
        output["msg"] = TURNING_LED_ON
    else:
        output["msg"] = LED_ALREADY_ON
    output["led_on"] = LED_ON
    return jsonify(output)


@led_off_mode.route('/run', methods=['GET'])
def led_off_run():
    """
    ---
    get:
      description: This is what turns off the LED
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing
    """
    output = {
      "msg": "",
      "led_on":""
    }
    
    led_process = Thread(target=led_off, args=())
    led_process.start()

    if(LED_ON):
        output["msg"] = TURNING_LED_OFF
    else:
        output["msg"] = LED_ALREADY_OFF
    output["led_on"] = LED_ON
    return jsonify(output)
