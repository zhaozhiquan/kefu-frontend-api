# coding=utf-8
import unittest
import os
from time import sleep
import requests as re
import random
import public.methods as t
import public.case_xls as xl
class API4(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''关闭问题'''
	def setUp(self):
		self.headers = {self.get_row(0, 11)[0]: self.get_row(0, 11)[1]}  # headers
		self.url = self.get_row(5,1)[1]
		self.key = self.get_row(5,2)        # key
	def tearDown(self):
		pass

	def test_01(self):
		u'''关闭问题,正确参数'''
		questions_id = self.get_questions_id()
		print questions_id
		if questions_id != None:
			value = self.get_row(5,3)
			data = {}
			data[self.key[2]] = self.get_token()
			data[self.key[3]] = questions_id
			data[self.key[4]] = value[4]
			data[self.key[5]] = value[5]
			request = self.apicall(value[1], self.url, data,self.headers)
			print request.status_code
			self.assertEqual(request.status_code,int(value[8]))
			print request.json()
			self.assertEqual(request.json()['error_code'],int(value[9]))
		else:
			print '没有已回复问题'
			self.assertIsNone(questions_id)

	def test_02(self):
		u'''关闭问题,错误(result)参数'''
		questions_id = self.get_questions_id()
		print questions_id
		if questions_id != None:
			value = self.get_row(5, 4)
			data = {}
			data[self.key[2]] = self.get_token()
			data[self.key[3]] = questions_id
			data[self.key[4]] = value[4]
			data[self.key[5]] = value[5]
			request = self.apicall(value[1], self.url, data,self.headers)
			print request.status_code
			self.assertEqual(request.status_code,int(value[8]))
			print request.json()
			self.assertEqual(request.json()['error_code'],int(value[9]))
		else:
			print '没有已回复问题'
			self.assertIsNone(questions_id)

	def test_03(self):
		u'''关闭问题,错误(appraise)参数'''
		questions_id = self.get_questions_id()
		print questions_id
		if questions_id != None:
			value = self.get_row(5, 5)
			data = {}
			data[self.key[2]] = self.get_token()
			data[self.key[3]] = questions_id
			data[self.key[4]] = value[4]
			data[self.key[5]] = None
			request = self.apicall(value[1], self.url, data,self.headers)
			print request.status_code
			self.assertEqual(request.status_code,int(value[8]))
			print request.json()
			self.assertEqual(request.json()['error_code'],int(value[9]))
		else:
			print '没有已回复问题'
			self.assertIsNone(questions_id)

	def test_04(self):
		u'''关闭问题,错误(id)参数'''
		questions_id = self.get_questions_id()
		print questions_id
		if questions_id != None:
			value = self.get_row(5, 6)
			data = {}
			data[self.key[2]] = self.get_token()
			data[self.key[3]] = questions_id+'1'
			data[self.key[4]] = value[4]
			data[self.key[5]] = value[5]
			request = self.apicall(value[1], self.url, data,self.headers)
			print request.status_code
			self.assertEqual(request.status_code,int(value[8]))
			print request.json()
			self.assertEqual(request.json()['error_code'],int(value[9]))
		else:
			print '没有已回复问题'
			self.assertIsNone(questions_id)