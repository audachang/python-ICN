#using_name.py
print __name__
if __name__ == '__main__':
	print('This program is being run by itself')
else:
	print __name__
	print('I am being imported from another module')