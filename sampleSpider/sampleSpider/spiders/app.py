# Flask application
import scrapy
from flask import Flask, render_template, request
import mysql.connector
import subprocess
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import json

app = Flask(__name__)
# MySQL configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'samplespider'
}

@app.route('/')
def index():
    print("hoiiiiiojjjjlkokkm")
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    print("hoiiiiiojjjjj")
    if request.method == 'POST':
        url = request.form['url']
        # Pass the URL to the Scrapy spider using subprocess
        print("the url is " + url)
        try:
            subprocess.run(['scrapy', 'crawl', 'sampleSpiderr', '-a', f'start_urls={url}'])
            

            print("the url isssssssss " + url)
        except Exception as e:
            return f"An error occurreddddddd: {e}"

        try:
            conn = mysql.connector.connect(**mysql_config)
            cursor = conn.cursor()

            query = "SELECT meta_title, meta_description,img_alt_tags,facebook_link,instagram_link,linkedin_link,twitter_link,youtube_link,robots,sitexml,sitehtml,canonical_url,utf,gtm_tag,h1count,h2count,h3count,h4count,h5count,h6count , total_words , web_loadspeed ,mob_loadspeed ,website_url ,icc,favicon_count ,all_links ,fcp,fid,lcp,cls,SI,total_blockingT FROM temp_data"
            cursor.execute(query)
            
            results = cursor.fetchall()
            app.logger.info(results)  # Log the results for debugging
            # results = cursor.fetchall()

            cursor.close()
            conn.close()
            print("the datatyoe of result is : ")
            print(len(results))
            t = ()
            t=results[0]
            items_to_show=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
            items_to_show[0]=t[0] # title 
            title_length= len(t[0])
            items_to_show[1]=len(t[0]) # title length
            description_length=len(t[1])
            items_to_show[2]=t[1]  # descrition
            items_to_show[3]=len(t[1]) # description length
            if title_length<75:
                items_to_show[4]="Short Title"
            elif 75<title_length<90:
                items_to_show[4]="Overlength Title"
            else:
                items_to_show[4]="High Risk Title"
            
            if description_length<75:
                items_to_show[5]="Short Description"
            elif 75<description_length<90:
                items_to_show[5]="Overlength Description"
            else:
                items_to_show[5]="High Risk Description"
            items_to_show[6]=t[2]   #alt tags
            items_to_show[7]=t[3]   #face
            items_to_show[8]=t[4]   #ints
            items_to_show[9]=t[5]   #linked
            items_to_show[10]=t[6]  #twit
            items_to_show[11]=t[7]  #yout
            social_linkC =0
            if items_to_show[7]=='facebook link not found' or items_to_show[8]=='Instagram link not found' or items_to_show[9]=='linkedin link not found' or items_to_show[10]=='twitter link not found' or items_to_show[11]=='youtube link not found':
                social_linkC = 1
            
            items_to_show[12]=t[8]  #robots.txt
            items_to_show[13]=t[9]  #sitemap.xml
            items_to_show[14]=t[10] #sitemap.html
            items_to_show[15]=t[11] # canonical
            items_to_show[16]=t[12] # utf
            items_to_show[17]=t[13] #gtm tag
            items_to_show[18]=t[14] #h1
            items_to_show[19]=t[15]
            items_to_show[20]=t[16]
            items_to_show[21]=t[17]
            items_to_show[22]=t[18]
            items_to_show[23]=t[19] #h6
            items_to_show[24]=t[20] # total word count
            items_to_show[25]=t[21] #website load speed
            items_to_show[26]=t[22] #mobile load speed
            items_to_show[27]=t[23] # website url
            items_to_show[28]=t[24] # inline css count
            items_to_show[29]=t[25] # favicon count
            json_data = t[26]
            
            items_to_show[30]=json.loads(json_data)# all the links 
            length = items_to_show[30]
            items_to_show[31]=len(length) # total links
            items_to_show[32]=t[27] #fcp
            items_to_show[33]=t[28] #fid
            items_to_show[34]=t[29] #lcp
            items_to_show[35]=t[30] #cls
            items_to_show[36]=t[31] #SI
            items_to_show[37]=t[32] #total_blockingT
            items_to_show[38]=social_linkC # social media count 
            print("the values of socila is ",social_linkC);

            

            

            # print("the size of new is ")
            # print(len(items_to_show))
            print(results)
            print(items_to_show)



            return render_template('New.html', results=items_to_show)
        except Exception as e:
            return f"An error occurred: {e}"

        # return "Spider started for search query: " + url 

        # return render_template('success.html', url=url)
    
    

if __name__ == '__main__':
    app.run(debug=True)


# code ends here 
