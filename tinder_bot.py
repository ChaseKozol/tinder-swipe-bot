from selenium import webdriver
from time import sleep

from secrets import phonenumber, blacklist

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome()

	def login(self):
		self.driver.get('https://tinder.com')

		sleep(2)

		pn_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
		pn_btn.click()

		sleep(2)

		pn_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
		pn_in.send_keys(phonenumber)

		continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
		continue_btn.click()

		# you will need to manually enter the code that was texted
		sleep(15)
        
		self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
		self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

	def like(self):
		like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/button[3]')
		like_btn.click()

	def dislike(self):
		dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/button[1]')
		dislike_btn.click()

	def find_bio_button(self):
		# open up bio
			try:
				self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button').click()
			# sometimes the button moves ?
			except Exception:
				try:
					self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[7]/button').click()
					# who the fuck made this website ???
				except Exception:
					self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/button').click()

	def swipe(self):
		while True:
			sleep(1)
			liked = True
			try:
				self.find_bio_button()

				try:
					bio = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/span').text
				except Exception:
					bio = ""
				
				#search bio for blacklisted term	
				for term in blacklist:
					if term in bio:
						print(term + " found in Blacklist")
						liked = False

				# check if profile only has one photo
				try:
					self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[2]/div/div[1]/div/div[2]')
				except Exception:
					print("Could not find second photo")
					liked = False

				if liked:
					self.like()
				else:
					self.dislike()

			except Exception:
				try:
					self.close_popup()
				except Exception:
					self.close_match()

	def close_popup(self):
		popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
		popup_3.click()

	def close_match(self):
		match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
		match_popup.click()

bot = TinderBot()
bot.login()
sleep(5)
bot.swipe()