# Selenium-Scripts

## Basic Setup
* Make sure you have the latest version of python installed
* Install Selenium
>`pip install -U selenium`
* Download [Chrome Webdriver](https://chromedriver.chromium.org/downloads) compatible to your Google Chrome browser version. (**Unzip the file to the directory where script is located**)

1.  ### Whatsapp Broadcast Script
A dead simple script to broadcast messages to many people (Even to people not saved in your contacts!)
#### Usage
* Enter your message and all numbers.
>     msg = 'Hello!' #Enter your message here
>     number = ['+91964744235', '+91583853853'] #Enter all numbers here
* Now run the script
    `python WhatsappBroadcast.py`
* Scan the QR code when whatsapp web opens.
* Thats it! Watch the script sending messages!

2.  ### Instagram like all posts Script
A dead simple script to like all posts of a person on Instagram
#### Usage
* Enter the username and password of your account.
>     user = 'YOUR USER NAME HERE'
>     passwd = 'YOUR PASSWORD HERE'

* Enter the username of the person

    `favPerson = 'vaishnavi_ganesh_nayaka'`

* Now run the script
    `python InstaLike.py`
* Thats it! Watch the script liking all posts

More scripts will be added...