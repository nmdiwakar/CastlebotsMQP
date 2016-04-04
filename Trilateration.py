# wifi code here

from scipy.optimize import fsolve
import numpy


class Trilaterator:
	speed_sound = 343


float b_source = TS_b - TS_a
float c_source = TS_c - TS_a

float d_ab = speed_sound * b_source
float d_ac = speed_sound * c_source
#socket receives coordinates and mic readings - pass to this code

#a_x, a_y
#b_x, b_y
#c_x, c_y

#TS_a, TS_b, TS_c

#source_x = x[0]
#source_y = x[1]
#a_source = x[2]


def trilaterate(float a_x, float a_y, float b_x, float b_y, float c_x, float c_y, float ): 



def calculate(x):
	out = [((x[0]-a_x)**2) - ((x[1]-a_y)**2) - (speed_sound * x[2]]
	out.append = (((x[0] - b_x)**2) + ((x[1] - b_y)**2) - ((speed_sound*x[2]) + d_ab))
	out.append = (((x[0] - c_x)**2) + ((x[1] - b_y)**2) - ((speed_sound*x[2]) + d_ac))
	return out