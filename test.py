import cv2
import re

constr = "('IAAB01_Step_1_1','==',5) and ('IAAB01_Step_1_1','==',6)"

pattern = "\([^()]*\)"

a = re.findall(pattern, constr)
for aa in a:
    aa = aa.lstrip("(")
    aa = aa.rstrip(")")
    vals = aa.split(",")
    print(vals)



