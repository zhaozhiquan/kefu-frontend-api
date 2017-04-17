#!/usr/bin/env python
#coding=utf-8
import os
from time import sleep, strftime
import case_xls as xl
import requests as re
import xlrd
from xlutils.copy import copy
class Methods(xl.Case_xls):

	def apicall(self, method, url, postparams=None,headers=None,getparams=None):
		if method == 'GET':
			if getparams != None:
				result = re.get(url, getparams)
			else:
				result = re.get(url,headers)
		if method == 'POST':
			if postparams != None:
				result = re.post(url, postparams,headers)
			else:
				result = re.post(url,headers)
		return result

	def save_token(self):
		headers = {self.get_row(0,11)[0]:self.get_row(0,11)[1]} #headers
		url = self.get_row(0,3)[1]
		data = {}
		data[self.get_row(0,5)[0]] = self.get_row(0,5)[1]    #grant_type
		data[self.get_row(0,6)[0]] = self.get_row(0,6)[1]    #client_id
		data[self.get_row(0,7)[0]] = self.get_row(0,7)[1]    #client_secret
		data[self.get_row(0,8)[0]] = self.get_row(0,8)[1]    #scope
		data[self.get_row(0,9)[0]] = self.get_row(0,9)[1]    #username
		data[self.get_row(0,10)[0]] = self.get_row(0,10)[1]  #password
		request = self.apicall(self.get_col(0,1)[4], url, data,headers)
		try:
			token = request.json()['access_token']
		except:
			token = None
		if token != None:
			rb = xlrd.open_workbook('/Users/zhaozhiquan/automation/kefu-frontend-api/public/TestData.xls')
			workbook = copy(rb)
			ws = workbook.get_sheet(0)
			ws.write(12, 1, token)
			workbook.save('/Users/zhaozhiquan/automation/kefu-frontend-api/public/TestData.xls')
			print '写入token成功'
		else:
			print '写入token失败,测试结束'
			exit()

	def get_questions_id(self):
		#获取 已回复的 问题
		url1 = 'http://kefu.4gvv.com/api/questions'
		token = self.get_token()
		data = {}
		data['access_token'] = token
		data['pagesize'] = 10
		questions = self.apicall('GET', url1, None, None, data)
		questions_list = questions.json()['data']
		for i in range(len(questions_list)):
			print questions_list[i]['status']
			if questions_list[i]['status'] == u'已回复':
				questions_id = questions_list[i]['id']
				break
			else:
				questions_id = None
		return questions_id

	def get_questions_id2(self):
		url1 = 'http://kefu.4gvv.com/api/questions'
		token = self.get_token()
		data = {}
		data['access_token'] = token
		questions = self.apicall('GET', url1, None, None, data)
		questions_id = questions.json()['data'][0]['id']
		return questions_id

	def get_token(self):
		token = self.get_row(0, 12)[1]
		return token