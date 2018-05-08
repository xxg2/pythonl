Scrapy Project
====

Execute Steps
----
0. Setup Python 2.7.
1. Install scrapy.  
    ```
    pip install Scrapy
    ```
2. Run Scrips.
    * export QS data to items.csv
   ```
   scrapy crawl organizationQSSpider -o qsitems.csv
   ```
   * export SC data to items.csv
   ```
   scrapy crawl organizationSCSpider -o scitems.csv
   ```
References
---
#### How to install scrapy by different environment ?  
    You could follow this guide to install. https://docs.scrapy.org/en/latest/intro/install.html   
#### How to change user agent and proxy?  
    Open settings.py and find USER_AGENT_LIST and PROXIES to update items.
#### How to disable user agent and proxy?  
    Open settings.py and find DOWNLOADER_MIDDLEWARES to comment line. 