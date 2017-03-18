try:
  2/0
except Exception, e:
  print 'Error - ' + str(e)
finally:
  print 'Done!'
