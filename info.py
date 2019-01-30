import os
import time
import string
import json

from app import App

class Info(object):
    def __init__(self):
        pass 

    def write_to_json(self, inputs):
        if (os.path.exists("exports.json") == True):
            pass
        else:
            os.mknod("exports.json")

        with open("exports.json", "w") as data:
            json.dump(inputs, data)
            
    def retrieve_info(self):
        input_name = input("Enter name: ")
        input_age = input("Enter age: ")
        input_height = input("Enter height in inches: ")
        input_weight = input("Enter weight in pounds: ")

        print("\nProcessing information...")
        self.write_to_json((input_name, input_age, input_height, input_weight))
        time.sleep(1)
        print("Done!\n")

        app = App(input_name, input_age, input_height, input_weight)
        app.get_summary()