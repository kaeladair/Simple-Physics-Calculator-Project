train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# Function takes an input in degrees Farenheit and converts it to degrees Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9

# Converting 100 Farenheit into degrees Celsius
f100_in_celsius = f_to_c(100)
  
# Function takes an input in degrees Celsius and converts it to degrees Farenheit
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)

# Converting 0 degrees Celsius into degrees Farenheit
c0_in_farenheit = c_to_f(0)

# Function takes in mass and acceleration in order to compute force
def get_force(mass, acceleration):
  return mass * acceleration

# Storing the trains force into the variable train_force, then printing a string for output
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function takes in mass and c (default set as speed of light) and multiplies mass by c squared to get energy in Joules
def get_energy(mass, c = 3 * 10 ** 8):
  return mass * (c ** 2)

# Calls get_energy to find energy of a bomb with a certain mass. Stores it as a variable to print.
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function takes in mass, acceleration, and distance to get work in Joules by finding force and multiplying by distance
def get_work(mass, acceleration, distance):
  return get_force(train_mass, train_acceleration) * distance

# Stores the work in a variable to print
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")