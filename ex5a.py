name = 'Steve Silva'
age = 64 # not a lie
height = 70 # inches
weight = 220 # poundsy_eyes = 'Brown'
eyes = 'Brown'
teeth = 'White'
hair = "Grey"
cmc = 2.54
kilos = .4535924

print(f"Let's talk about {name}.")
print(f"He's {round(height*cmc)} centimeters tall.")
print(f"He's {round(weight*kilos)} kilos heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + round(height*cmc)+ round(weight*kilos)
print(f"If I add {age}, {round(height*cmc)}, and {round(weight*kilos)} I get {total}.")