# -*- coding: utf-8 -*-
import math

root = math.sqrt(math.pi)
print root
print '%.3f' % root
print str(root)[:7] + ' or ' + '%1.5f' % root  # to løsninger

val = -1
while val <= 1:
    print 'cos: ' + ('%1.4f' % math.cos(val)) + ', sin: ' + ('%1.4f' % math.sin(val))
    val += 0.05
