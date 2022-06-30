import math
import re

def hex_to_color(code = 0xFFFFFF):
  '''
  Function makes tuple of RGB values from given hex-code
  '''
  if type(code) == str:
    if code[0] == '#':
      code = int(code[1:], 16)
    elif code[0:2] == '0x':
      code = int(code[2:], 16)
    else:
      code = int(code, 16)
  color = []
  for _ in range(3):
    color.append(code % 0x100)
    code //= 0x100
  color.reverse()
  return tuple(color)

def color_to_hex(color = (255, 255, 255)):
  '''
  Function makes hex-code from given tuple of RGB values
  '''
  return '#' + hex(color[0])[2:].zfill(2) + hex(color[1])[2:].zfill(2) + hex(color[2])[2:].zfill(2)

def gradient(color1 = (0, 0, 0), color2 = (255, 255, 255), steps = 100):
  '''
  Function takes two colors and returns a tuple of the colors that make up their gradient
  '''
  if type(color1) == str or type(color1) == int:
    color1 = hex_to_color(color1)
  if type(color2) == str or type(color2) == int:
    color2 = hex_to_color(color2)
  diff = [(color2[i] - color1[i]) / steps for i in range(3)]
  color_list = list((color_to_hex(color1),))
  color_temp = color1
  for _ in range(steps):
    color_temp = [min(255, color_temp[i] + diff[i]) for i in range(3)]
    new_color = tuple([math.ceil(color) for color in color_temp])
    color_list.append(color_to_hex(new_color))
  return tuple(color_list)

is_correct_color = lambda x: re.match(r'^(#\b|\b0x)?[a-fA-F0-9]{1,6}\b',x)
