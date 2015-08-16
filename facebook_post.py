import mechanize
import cookielib
import sys
import getpass

br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = 'https://m.facebook.com/login.php'




def post_msg():
	br.select_form(nr=1)
	print "The message will get updated from your facebook profile, post carefully\n"
	message = raw_input("Enter the post: ")
	br.form['xc_message'] = message
	br.submit(name='view_post')
	print "[+] Post updated successfully.\n"
	r = raw_input("Do you want to post something again? (y/n): ")
	if r==y:
		post_msg()
	else:
		print "Exiting. . ."
		br.close()
		sys.exit(0)


def fb_login():
	
	email = raw_input("Enter your username: ")
	pwd = getpass.getpass()

	br.select_form(nr=0)
	br.form['email'] = email
	br.form['pass'] = pwd
	br.submit()

	login_url = br.geturl()
	error_login = 'https://m.facebook.com/login.php?'
	s = login_url.find(error_login)
	if(s==-1):
		print "\n[+] Login successful!\n"
		post_msg()

	elif(s!=-1):
		print "\n[+] Wrong credentials entered!"
		print "Try again. . .\n"
		fb_login()




br.open(url) 
fb_login()


