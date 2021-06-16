t =int(input())
while(t>0):
  x = list(input().split())
  h = int(x[0])
  m = int(x[1])
  hour_angle = ((h*60) + m)//2
  minute_angle = (6 * m)
  angle = abs(hour_angle - minute_angle)
  angle = min(360-angle,angle)
  print(angle)
  t=t-1