<h2> Reading Data From Websites </h2>
<p> Web scraping refers to the art of programmatically getting data from the internet. One of the coolest features of Python is that it makes it easy to scrape websites. 
In Python 3, the most popular library for web scraping is <b>BeautifulSoup</b>. To use <b>BeautifulSoup</b>, we will also need the <b>requests</b> module, which basically connects to a given URL and fetches data from it (in HTML format). A web page is basically HTML code, and the main use of <b>BeautifulSoup</b> is that it helps you parse HTML easily.</p>

<h3> Use Case - Fetching Mobile App Reviews from Google Playstore </h2>
Let's say you want to understand why people install and uninstall mobile apps, and why they like or dislike certain apps. A very rich source of app-reviews data is the Google Play Store, where people write their feedback about the app.

The reviews of the Facebook Messenger app can be found
here: <href><https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en>

Scrape reviews of the Messenger app, i.e. get them into Python,
