# Determine type to convert from.
typ = input("seconds or milliseconds? (s/[ms])  ")
if typ=="s":
  secs = int(input("Ok. Converting seconds to human readable format.\nPlease Enter the number of seconds.  "))
  miliseconds=0
else:
  ms=int(input("Ok. Converting miliseconds to human readable format.\nPlease Enter the number of miliseconds.  "))
  secs = ms%1000
  miliseconds= ms-secs*1000
mins=secs%60
seconds=secs-mins*60
hrs=mins%60
minutes=mins-hrs*60
days=hrs%24
hours=dys-days*24

print(f'There are {days} days, {hours} hours, {minutes} minutes, {seconds} seconds, and {milliseconds} seconds.')
