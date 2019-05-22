# -*- coding:utf-8 -*-

college = {
'science':['chemistry', 'physics', 'mathematics'],
'engineering':['electric engineering','mechanics','chemical engineering'],
'Social Science':['History', 'Sociology', 'Psychology']}


def has_college(colstr):
	if colstr in college.keys():
		print 'yes, NCU has school of %s ' % colstr
		return True
	else:
		print 'No, NCU does not have %s school' % colstr
		return False
