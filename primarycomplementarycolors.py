# -*- coding: UTF8 -*-

def complementary_color(primary_color):
  if primary_color == 'red':
    print("The complimentary color of",primary_color,'is green!')
  elif primary_color == 'blue':
    print("The complimentary color of",primary_color,'is orange!')
  elif primary_color == 'yellow':
    print("The complimentary color of",primary_color,'is purple!')
  else:
    print(primary_color,"is not a primary color.")

def main():
  
  primary_color = input("Insert primary color (red / blue / yellow): ")

  primary_color = primary_color.lower()

  complementary_color(primary_color)

if __name__ == "__main__":
      main()