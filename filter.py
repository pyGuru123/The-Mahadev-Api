import os

count = 1
for file in os.listdir():
	name, ext = os.path.splitext(file)
	if ext != '.py':
		new = f'shivlinga{count}.jpg'
		os.rename(file, new)
		count += 1