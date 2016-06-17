# -*- coding: utf-8 -*-

class Singleton(type):
	def __call__(cls,*args,**kw):
		if not hasattr(cls,'_instance'):
			cls._instance = None
		if cls._instance is None:
			cls._instance = super(Singleton,cls).__call__(*args,**kw)
		return cls._instance
