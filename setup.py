from distutils.core import setup

setup(
	name = 'protojamblang',
	version = '0.0.0',
	packages = [
		'jamb'
	],
	scripts = [
		'scripts/jamb'
	],
	requires = [
		'sympy'
	]
)
