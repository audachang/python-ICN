# -*- coding:utf-8 -*-

class university(object):

	college = {
	'science':['chemistry', 'physics', 'mathematics'], 
	'engineering':['electric engineering','mechanics','chemical engineering'],
	'Social Science':['History', 'Socioloyg', 'Psychology']}


	def has_college(self, colstr):
		if colstr in self.college.keys():
			print 'yes, NCU has school of %s ' % colstr
			return True 
		else:
			print 'You wish!! NCU does not have %s school' % colstr
			return False
			
