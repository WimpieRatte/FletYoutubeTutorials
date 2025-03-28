# Description
My coding of a received tutorial video.

Video URL: https://www.youtube.com/watch?v=5P8f5Tlim0M

# Breakdown
## 1. Create Fake API
- Use https://mockapi.io/
	- Create new project (FletApp Demo)
	- Create new resource/endpoint (users)
	- Set users to 20 and test the endpoint (by clicking on "users")
## 2. Flet app
- Create new folder in VS Code
- Create & activate a virtual environment
- Further, in terminal:
	- `pip list` to see which packages are already installed
	- `pip install flet` to install Flet to your project for creating Flutter apps with Python code.
	- `pip install requests` for HTTP requests.
	- Optional:
		- `pip install beautifulsoup4` to extract data from HTML code.
		- (Not needed, because we'll get data in the form of JSON)
- Create `main.py` in main folder. (See main.py)
	- Controls list: https://flet.dev/docs/controls
	- Test app with mock API endpoint