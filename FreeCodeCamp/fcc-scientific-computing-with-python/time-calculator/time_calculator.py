def add_time(start, duration, day=None):
  dminute = int(duration[-2:])
  dhour = int(duration[0:-3])
  realstart = start.replace(":", " ").split()
  realhour = int(realstart[0]) + dhour
  realminute = int(realstart[1]) + dminute

  if start[-2:].lower() == "pm":
    realhour += 12

  while realminute >= 60:
    realminute -= 60
    realhour += 1

  dayvalue = 0
  while realhour >= 24:
    dayvalue += 1
    realhour -= 24
  
  realampm = ""
  if realhour >= 12:
    realhour -= 12
    realampm = "PM"

  else:
    realampm = "AM"

  if realhour == 0:
    realhour = 12

  if day == None and dayvalue < 1:
    return f"{realhour}:{realminute:02d} {realampm}"

  elif day == None and dayvalue == 1:
    return f"{realhour}:{realminute:02d} {realampm} (next day)"

  elif day == None and dayvalue > 1:
    return f"{realhour}:{realminute:02d} {realampm} ({dayvalue} days later)"
  
  else:

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    daydict = dict(zip(days,range(int(len(days))+1)))
    dayss = dayvalue
    dayvalue += daydict.get(day.lower())

    while dayvalue >= 7:
      dayvalue -= 7

    realday = (list(daydict.keys())[list(daydict.values()).index(dayvalue)])

  if dayss == 1:
    return f"{realhour}:{realminute:02d} {realampm}, {realday.capitalize()} (next day)"

  elif dayss == 0:
    return f"{realhour}:{realminute:02d} {realampm}, {realday.capitalize()}"

  elif dayss > 1:
    return f"{realhour}:{realminute:02d} {realampm}, {realday.capitalize()} ({dayss} days later)"

