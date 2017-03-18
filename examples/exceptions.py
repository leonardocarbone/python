def division(value1, value2):
  try:
    value1 / value2
  except Exception, e:
    print 'On error - ' + str(e)
  else:
    print "On else!"
  finally:
    print 'On finally!'
    
division(2,2)
print ""
division(2,0)
