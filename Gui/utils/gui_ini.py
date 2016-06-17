# -*- coding: utf-8 -*-

import re
from Singleton import Singleton

class gui_ini(metaclass = Singleton):
	_guipath = 'E:/Python_src/python/Gui'
	_dictgui = {}
	def __init__(self):
		pass

	def Init(self):
		'''
			初始化配置类，保存为一个dict
		'''
		try:
			with open(self._guipath + '/gui.ini','r') as gui_file:
				dictCtrl = {} #控件map
				lastCtrlComment = '' #最近的一条控件的注释
				lastDlgID = ''
				lastcomment = '' #最近的一条注释
				pattern = re.compile(r'^\[(\d*)-(\d*)\]$')
				AttrPattern = re.compile(r'^(.*)=(.*)$')
				bLegal = False
				for line in gui_file:

					line = line.strip()
					if line.find('//') == 0: #找到一条注释
						lastcomment = line
						'''
						lastcomment = line[2:]
						lst_comment = lastcomment.split('-',1)
						ctrl_name = lst_comment[0]
						if lst_comment[1] != "":
							ctrl_comment = lst_comment[1]
						'''
					elif pattern.search(line):
						parent_id = pattern.search(line).groups()[0]
						ctrlID = pattern.search(line).groups()[1]
						dictCtrl = {}
						dictCtrl['parentid']= parent_id
						dictCtrl['id'] = ctrlID
						dictCtrl['comment'] = lastcomment
						bLegal = True
						if parent_id == '0': #是Dlg
							dictCtrl['children'] = []
							self._dictgui[ctrlID] = dictCtrl
							lastDlgID = ctrlID
						else: #是控件
							parent = self._dictgui.get(str(lastDlgID))
							if parent:
								parent['children'].append(dictCtrl)
					elif AttrPattern.search(line): #找到属性
						if bLegal == True:
							dictCtrl[ AttrPattern.search(line).groups()[0] ] = AttrPattern.search(line).groups()[1]
					else: #非法的配置
						bLegal = False
			return True
		except IOError as e:
			print(e)
			return False

	def get(self,id):
		return self._dictgui.get(str(id))

	def getChildren(self,id):
		if self.get(str(id)):
			return self.get(id)['children']
		return None










