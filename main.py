import math


class StraightLine:
    def __init__(self, y, x, name):
        self.y = y
        self.x = x
        self.name = name

    def input_attributes(self):
        self.y = float(input("Faka isilungelelanisi sika Y"))
        self.x = float(input("Faka isilungelelanisi sika X"))
        self.name = input("Faka igama lendawo")

    def distance(self):
        x_origin = 0
        y_origin = 0
        dist = math.sqrt((self.x - x_origin) ** 2 + (self.y - y_origin) ** 2)
        return dist

    def x_ref_x_axis(self):
        x_ref = self.x * -1
        return x_ref

    def y_ref_y_axis(self):
        y_ref = self.y * -1
        return y_ref

    def determine_quad(self):
        if self.y > 0 and self.x > 0:
            quad = "EMntla Mpuma"
        elif self.y > 0 and self.x < 0:
            quad = "EMntla Ntshona"
        elif self.y < 0 and self.x < 0:
            quad = "EMzantsi Ntshona"
        elif self.y < 0 and self.x > 0:
            quad = "Emzantsi Mpuma"
        elif self.y > 0 and self.x == 0:
            quad = "Emntla"
        elif self.y == 0 and self.x < 0:
            quad = "Ntshona"
        elif self.y < 0 and self.x == 0:
            quad = "Mzantsi"
        elif self.y == 0 and self.x > 0:
            quad = "Mpuma"
        elif self.y == 0 and self.x == 0:
            quad = "Orijini"
        return quad

    def equation_str(self):
        # equation of a straight line...y = mx + c
        x_ori = 0
        y_ori = 0
        m = (self.y - y_ori) / (self.x - x_ori)
        c = self.y - m * self.x
        y = m * self.x + c
        return f'y = {m}x + {c}'

    def output(self,dis, ref_x_x_axis, ref_y_y_axis, quad, equa_straight):
        print("Umgama ophakathi kweOrijini nendawo efakwe ngumntu ngu", dis)
        print("Uguqulelo lwendawo efakwe ngumntu kwiiAsi zika Y ngu ",self.name, "(", ref_x_x_axis, ",", self.y, ")")
        print("Uguqulelo lwendawo efakwe ngumntu kwiiAsi zikaX ngu ",self.name, "(", self.x, ",", ref_y_y_axis, ")")
        print("Lendawo ifakwe ngumntu ise " + quad)
        print("IEquation yomgca ongqalileyo ngu  " + equa_straight)


class TestClass:
    if __name__ == '__main__':
        obj2_sl = StraightLine(0.0,0.0,"")
        obj2_sl.input_attributes()
        dis = obj2_sl.distance()
        ref_x_x_axis = obj2_sl.x_ref_x_axis()
        ref_y_y_axis = obj2_sl.y_ref_y_axis()
        quad = obj2_sl.determine_quad()
        equa_straight = obj2_sl.equation_str()
        obj2_sl.output(dis, ref_x_x_axis, ref_y_y_axis, quad, equa_straight)



