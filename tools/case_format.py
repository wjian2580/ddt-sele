# -*- coding: utf-8 -*-

import os 

def main():
	path = os.path.abspath('.')
	cases = [os.path.join(path,case) for case in os.listdir('.') if case != 'case_format.py']
	st = ''
	for case in cases:
		with open(case,encoding='utf-8') as f:
			lines = f.readlines()
		for line in lines:
			if 'clear()' in line:
				pass
			elif 'click()' in line:
				line = new_line(line,'click')
				st += (line+'\n')
			elif ').send' in line:
				line = new_line(line,f='send_keys')
				st += (line+'\n')
			else:
				st += line
		with open(case,'w',encoding='utf-8') as f:
			f.write(st)
		st = ''


def new_line(line,f):
	by = line.split('by_')[-1].split('(')[0]
	if by == 'css_selector':
		by = 'css'
	elif by == 'link_text':
		by = 'text'
	elif by == 'partial_link_text':
		by = 'text_part'
	elif by == 'class_name':
		by = 'class'
	value = line.split('(',1)[-1].split(')')[0].strip('"')
	if f == 'send_keys':
		keys = line.split('_keys')[-1].strip('"()')
		line = "self.send_keys('{}={}','{}')".format(by,value,keys)
	else:
		line = "self.click('{}={}')".format(by,value)
	return line

if __name__ == '__main__':
	main()