import os
import sys
import time

class App(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    @property
    def get_name(self):
        return self.name

    @property
    def get_age(self):
        return self.age
    
    @property
    def get_height(self):
        return self.height

    @property
    def get_weight(self):
        return self.weight

    def get_summary(self):
        print(f"This person is {self.name}. This person is {self.age} years of age.")
        print(f"{self.name} stands at {self.height} inches tall.")
        print(f"{self.name} weighs {self.weight} pounds.")