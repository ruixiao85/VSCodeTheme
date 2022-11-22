import colorsys

def hl2ratio(h, b=0.14, r=0.5, o=0.4):
  return b+r*min((h+1.0-o)%1.0,(h-o)%1.0)

prfs=['{ \"settings\": { \"foreground\": \"#']

# topaz
b=0.14; r=0.5; o=0.4; s=0.9
print(b,r,o,s)
sufs=[
(0.00, '\" }, \"scope\": [\"entity\"] },'),
(0.04, '\" }, \"scope\": [\"variable.language.special\", \"variable.parameter.function.language.special\"] },'),
(0.10, '\" }, \"scope\": [\"variable\", \"meta.function-call.arguments\"] },'),
(0.28, '\" }, \"scope\": [\"string\"] },'),
(0.39, '\" }, \"scope\": [\"constant\"] },'),
(0.51, '\" }, \"scope\": [\"meta\"] },'),
(0.62, '\" }, \"scope\": [\"support\"] },'),
(0.73, '\" }, \"scope\": [\"support.function\", \"meta.function-call\"] },'),
(0.80, '\" }, \"scope\": [\"keyword\"] },'),
(0.90, '\" }, \"scope\": [\"storage\"] },')
]
for (h, sur) in sufs:
  l=hl2ratio(h,b,r,o)
  rgb=[round(255*e) for e in colorsys.hls_to_rgb(h,l,s)]
  # print(f"{rgb}")
  rgbhex="".join("%02x" % c for c in rgb)
  # print(f"#{rgbhex}")
  print(prfs[0]+rgbhex+sur)


# cobalt rgb_ref=[25, 53, 73] # cobalt
b=0.6; r=-0.1; o=0.75; s=0.8
print(b,r,o,s)
for i in range(10):
  print(f"h {0.1*i:.2f} l {hl2ratio(0.1*i, b,r,o):.2f}")

sufs=[
(0.00, '\" }, \"scope\": [\"constant\"] },'),
(0.10, '\" }, \"scope\": [\"storage\"] },'),
(0.20, '\" }, \"scope\": [\"keyword\"] },'),
(0.30, '\" }, \"scope\": [\"entity\"] },'),
(0.40, '\" }, \"scope\": [\"variable.language.special\", \"variable.parameter.function.language.special\"] },'),
(0.50, '\" }, \"scope\": [\"variable\", \"meta.function-call.arguments\"] },'),
(0.60, '\" }, \"scope\": [\"string\"] },'),
(0.71, '\" }, \"scope\": [\"meta\"] },'),
(0.82, '\" }, \"scope\": [\"support\"] },'),
(0.90, '\" }, \"scope\": [\"support.function\", \"meta.function-call\"] },'),
]
for (h, sur) in sufs:
  l=hl2ratio(h,b,r,o)
  rgb=[round(255*e) for e in colorsys.hls_to_rgb(h,l,s)]
  # print(f"{rgb}")
  rgb=[max(0,min(255,a+b)) for a,b, in zip(rgb,rgb_dlt)]
  rgbhex="".join("%02x" % c for c in rgb)
  # print(f"#{rgbhex}")
  print(prfs[0]+rgbhex+sur)




# rgb_ref=[245,236,200] # topaz
# rgb_dlt=[(255-c)//3 for c in rgb_ref]

# rgb_dlt=[round(c/2) for c in rgb_ref]
# rgb_ref=[25, 53, 73] # cobalt
# rgb_ref=[11, 51, 41] # emerald
for b in [0.13]:
  for r in [0.5]: # 0.4, 0.6, 0.8
    for o in [0.4]:
      for s in [0.9]:




