# Clipping links with Bitley

The script shortens a long link or displays the number of clicks on a short one

### How to install

After cloning the project, create an .env file in the root with the following content:

```
TOKEN=Here is your GENERIC ACCESS TOKEN to work with Bit.ly
```

### How to get GENERIC ACCESS TOKEN

* Go to https://bitly.com
* If you don't have an account, create one https://bitly.com/a/sign_up.
* If you have an account, log in https://bitly.com/a/sign_in.
* Go to the settings page https://bitly.com/a/settings
* Select "Generic Access Token" tab
* Enter your bit.ly password and click "Generate Token"
* Copy your "Generic Access Token" and paste it into the .env file

Python3 should already be installed.
Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

### Launch example
```
python main.py https://google.com
```

### Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).
