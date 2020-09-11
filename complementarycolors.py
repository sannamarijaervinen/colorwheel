# -*- coding: UTF8 -*-

def secondary_color(primary_color):

  if primary_color == 'red':
    print("The complementary color of",primary_color,'is green!')
  elif primary_color == 'blue':
    print("The complementary color of",primary_color,'is orange!')
  elif primary_color == 'yellow':
    print("The complementary color of",primary_color,'is purple!')
  else:
    print(primary_color,"is not a primary color.")

def main():
  
  primary_color = input("Insert primary color (red / blue / yellow): ")

  primary_color = primary_color.lower() # The color wheel is based on the traditional RYB color model.

  secondary_color(primary_color)  # This subfunction prints the secondary color of the primary color.

if __name__ == "__main__":
      main()