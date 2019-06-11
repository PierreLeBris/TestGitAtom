train_mass = 22680
train_acceleration = 10
train_distance = 100
train_force = 2000
bomb_mass = 1
c = 3*10**8

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_celsuis = f_to_c(100)
print(f100_celsuis)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_fahrenheit = c_to_f(0)
print(c0_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

def get_energy(mass):
  return mass * c
bomb_energy = get_energy(bomb_mass)

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train supplies "+str(train_force)+" Newtons of force.")
print("A "+str(bomb_mass)+"kg bomb supplies "+str(bomb_energy)+" Joules")
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")
