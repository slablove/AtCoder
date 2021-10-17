x = int(input())

if x%100 == 0:
	if x >= 100 and x <= 1000:
  		print('Yes')
 
	elif x < 100:
  		print('No')
  
	elif x > 1000:
  		print('No')
else:
  print('No')
