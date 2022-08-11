#Python> Date and Time > Calendar Module
#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

MM, DD, YY = map(int, input().split(" "));

print(calendar.day_name[calendar.weekday(YY,MM,DD)].upper());

#NOTAS:
'''
- Importante siempre leer el orden de los parámetros antes de usar el método, para no tener que adivinar en que orden ponerlos valores.

- Calendar podría no ser el módulo adecuado para el cálculo de fechas y tiempo, una mejor opción según otro usuario de HackeRank es datetime.date
'''