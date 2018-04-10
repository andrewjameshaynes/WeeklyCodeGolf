def f(s):
	q=[x[0].upper()+x[1:] for x in ' '.join(' '.join(s.split('_')).split('.')).split(' ')]
	print(' '.join(q))

f("I have_some_cool.friends")