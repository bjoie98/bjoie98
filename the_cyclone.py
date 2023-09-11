# Write code below 💖
# the_cyclone.py
height = int(input('height (cm)? '))
credits = int(input('credits? '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >=10:
  print("You are not tall enough to ride")
elif height >=137 and credits < 10:
  print("You don't have enough credits")
elif height < 137 or credits < 10:
  print("Either requirement not met")
else:
  print('error')
