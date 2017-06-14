import numpy as np
import copy

def squared(x):
    y = x**2
    return y


list = np.arange(5)

#print list

y_list = []
for i in list:
    print i
    y = squared(i)
    y_list.append(y)


#print y_list

y_list = np.array(y_list)

list_mean = np.mean(y_list)
list_sum = np.sum(y_list)
list_prod = np.prod(y_list)
list_min = np.min(y_list)
list_max = np.max(y_list)
list_argmin = np.argmin(y_list)


old_y_list = copy.copy(y_list)

np.random.shuffle(y_list)

list_argmin_new = np.argmin(y_list)

print 'old list', old_y_list
print 'new list', y_list
print list_mean, list_sum, list_prod, list_min, list_max

print 'old list argmin', list_argmin

print 'new list argmin',list_argmin_new
