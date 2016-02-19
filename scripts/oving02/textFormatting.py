# -*- coding: utf-8 -*-
import math

root = math.sqrt(math.pi)
print root
print '%.3f' % root
print str(root)[:7] + ' or ' + '%1.5f' % root  # to løsninger

print 'x\t\tsin(x)\tcos(x)'
val = -1
while val < 1:
    print '%.2f\t%.4f\t%.4f' % (val, math.sin(val), math.cos(val))
    val += 0.05
