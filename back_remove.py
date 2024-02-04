from rembg import remove
from PIL import Image
input_path = '/home/dcl/Documents/python_problem_solves/loll.jpg'
output_path = '/home/dcl/Documents/python_problem_solves/output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)