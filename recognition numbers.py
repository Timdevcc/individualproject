from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import test
import random
Window.size = (500, 480)
tema = 0
n = 0
n_sensor = 15
img = [0 for i in range(15)]
weights = [0 for i in range(15)]

def decrease(number):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[i] -= 1

def increase(number):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[i] += 1

def perceptron(Sensor):
    b = 7
    s = 0
    for i in range(n_sensor):
        s += int(Sensor[i]) * weights[i]
    if s >= b:
        return True
    else:
        return False


class Container(GridLayout):
    def Pressed(self, num, obj):
        if obj.background_color == [1, 1, 1, 1]:
            obj.background_color = [.74, .33, .33, 1]
            img[num] = 1
        else:
            obj.background_color == [.74, .33, .33, 1]
            obj.background_color = [1, 1, 1, 1]
            img[num] = 0

    def topic_change(self):
        global tema
        tema = int(self.txt.text)

    def train(self):
        global n
        n = int(self.ntxt.text)
    
    def go_train(self):
        for i in range(n):
            j = random.randint(0, 9)
            r = perceptron(test.nums[j])
            
            if j != tema:
                if r:
                    decrease(test.nums[j])
            else:
                if not  r:
                    increase(test.nums[tema])
    
    def recog(self):
        res = perceptron(img)
        if res:
            self.result.text = f"это число {tema}"
        else:
            self.result.text = f'это не число {tema}'
        

            
class Myapp(App):
    def build(self):
        return Container()

if __name__ == "__main__":
    Myapp().run()
print(weights)