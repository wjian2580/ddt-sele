import os 

path = os.path.abspath('.')

cases = [os.path.join(path,case) for case in os.listdir('.') if case != 'case_format.py']


st = ''

for case in cases:
	try:
		f = open(case,encoding='utf-8')
		lines = f.readlines()
	finally:
		if f:
			f.close()
	for line in lines:
		if 'clear()' in line:
			pass
		elif 'click()' in line:
			by = line.split('by_')[-1].split('(')[0]
			value = line.split('(',1)[-1].split(')')[0].strip('"')
			if by == 'css_selector':
				by = 'css'
			elif by == 'link_text':
				by = 'text'
			elif by == 'partial_link_text':
				by = 'text_part'
			elif by == 'class_name':
				by = 'class'
			line = "self.click('{}={}')".format(by,value)
			st += (line+'\n')
		elif 'send_keys(' in line:
			by = line.split('by_')[-1].split('(')[0]
			value = line.split('(',1)[-1].split(')')[0].strip('"')
			keys = line.split('send_keys(')[-1].split(')')[0].strip('"')
			if by == 'css_selector':
				by = 'css'
			elif by == 'link_text':
				by = 'text'
			elif by == 'partial_link_text':
				by = 'text_part'
			elif by == 'class_name':
				by = 'class'
			line = "self.send_keys('{}={}','{}')".format(by,value,keys)
			st += (line+'\n')
		else:
			st += (line)
	try:
		f = open(case,'w',encoding='utf-8')
		f.write(st)
	finally:
		if f:
			f.close()
