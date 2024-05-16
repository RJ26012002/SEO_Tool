import scrapy
# from ..items import SamplespiderItem
from ..items import SamplespiderItem
import sys
import requests
import time 
import json




class Crawling_Test(scrapy.Spider):
    name ="sampleSpiderr"
    start_urls = []
    global website_url
    website_url="https://apollosage.in/"
    # start_urls = ["https://www.geeksforgeeks.org/introduction-deep-learning/"]

    def __init__(self, start_urls='', *args, **kwargs):
        super(Crawling_Test, self).__init__(*args, **kwargs)
        
        # self.start_urls = ["https://www.geeksforgeeks.org/introduction-deep-learning/"]
        self.start_urls = [start_urls]
    
    # print("the value of website url outside anything is ss" + website_url)
    def parse(self,response):
        items = SamplespiderItem()

        # Meta Title and Description
        meta_title = response.css("title").extract()[0].replace("<title>","").replace("</title>","")
        meta_description = response.xpath('//meta[@name="description"]/@content').extract()[0]

        #calculating the alt tags 
        tags = response.css('img::attr(alt)').getall()
        c=0
        for i in tags:
            if i=='':
                c=c+1
        img_alt_tags = str(c)

        # extracting the social links
        fb = response.xpath('//a[contains(@href, "facebook.com")]/@href').extract()
        twt =  response.xpath('//a[contains(@href, "twitter.com")]/@href').extract()
        inst = response.xpath('//a[contains(@href, "instagram.com")]/@href').extract()
        yout =  response.xpath('//a[contains(@href, "youtube.com")]/@href').extract()
        linkd =  response.xpath('//a[contains(@href, "linkedin.com")]/@href').extract()

        if len(fb)>1:
            items['facebook'] = fb[0]
        else:
            if len(fb)==0:
                items['facebook']="facebook link not found"
            else:
                items['facebook'] = fb[0]
        if len(twt)>1:
            items['twitter']= twt[0]
        else:
            if len(twt)==0:
                items['twitter']="twitter link not found"
            else:
                items['twitter'] =twt[0]
        if len(inst)>1:
            items['instagram']= inst[0]
        else:
            if len(inst)==0:
                items['instagram']="Instagram link not found"
            else:
                items['instagram'] = inst[0]
        if len(linkd)>1:
            items['linkedin']= linkd[0]
        else:
            if len(linkd)==0:
                items['linkedin']="linkedin link not found"
            else:
                items['linkedin'] = linkd[0]
        if len(yout)>1:
            items['youtube']= yout[0]
        else:
            if len(yout)==0:
                items['youtube']="youtube link not found"
            else:
                items['youtube'] = yout[0]
        
        
        # Cheking the utf
        websit_url=self.start_urls[0]
        print("kya url yaha tak aai ??? " + websit_url + " dekho dekho ")
        # Checking robots.txt,sitemap.xml,sitemap.html
        def check_robots_txt(url):
            try:
                # print("the website_urls issssssss "+url)
                response = requests.get(url)
                return response.status_code == 200
            except requests.RequestException:
                return False

        r=""
        # print("the website url before anythins is "+websit_url)
        if check_robots_txt(f'{websit_url}/robots.txt'):
            r = "It contain robots.txt"
        else:
            r="It does not contain robots.txt"
        
        sx =""
        if check_robots_txt(f'{websit_url}/sitemap.xml'):
            sx = "It contain sitemap.xml"
        else:
            sx="It does not contain sitemap.xml"

        sh=""
        if check_robots_txt(f'{websit_url}/sitemap.html'):
            sh = "It contain sitemap.html"
        else:
            sh="It does not contain sitemap.html"

        # cannonical
        canonical_url = response.xpath('//link[@rel="canonical"]/@href').get()

        # utf 8
        utf = response.xpath('//meta[@charset]/@charset').extract()[0]

        # gtm tag
        script_tag = response.xpath('//script[@src]')
        gtm_tag = script_tag.xpath('@src').get()

        # count h1 to h6 tags 
        h1 = response.css("h1::text").getall()
        h1count=len(h1)
        h2 = response.css("h2::text").getall()
        h2count=len(h2)
        h3=response.css("h3::text").getall()
        h3count=len(h3)
        h4  = response.css("h4::text").getall()
        h4count=len(h4)
        h5 = response.css("h5::text").getall()
        h5count=len(h5)
        h6=response.css("h6::text").getall()
        h6count=len(h6)

        # counting the number of words present 

        text_content =response.css('body *::text').getall()
        text = ' '.join(text_content)
        words = text.split()
        total_words = str(len(words))

        # calculating the speed of thw website loading speed

        def calculate_loading_time(url):
            try:
                start_time = time.time()
                response = requests.get(url)
                end_time = time.time()
                loading_time = end_time - start_time
                return loading_time
            except Exception as e:
                print(f"Error: {e}")
                return None
        
        
        loadin_time = calculate_loading_time(website_url)
        web_loadspeed = "{:.3f}".format(loadin_time)

        # calculating the mobile load speed

        def measure_mobile_responsive_speed(url):
            try:
                start_time = time.time()
                # Make a GET request to the website
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'})
                # Measure the time it takes to receive the response
                loading_time = time.time() - start_time
                return loading_time
            except Exception as e:
                print(f"Error: {e}")
                return None

        mob_loadspee = measure_mobile_responsive_speed(website_url)
        mob_loadspeed = "{:.3f}".format(mob_loadspee)


        # inline css check 
        inline_css = response.css('[style]').getall()
        icc = str(len(inline_css))

        # favicon count
        favicon_link = response.xpath('//link[@rel="icon"]/@href').getall()
        favicon_count = str(len(favicon_link))

        # all links sections
        data = {}
        c = 0
        links_count = 0
        links = response.css('a')
        for link in links:
            if c==1:
                break
            url = link.css('a::attr(href)').get()
            # print(type(url))
            if url!='' and url!=None :
                
                if url[0]=='h':
                    links_count=links_count+1
                    response = requests.get(url)
                    status_code = response.status_code
                    # print("character is " , char )
                    anchor_text = link.css('::text').get()
                    # print("for link :",url,"Anchor Text:", anchor_text)
                    data[url]=[anchor_text,str(status_code)]
                    c=c+1
        all_links = json.dumps(data)


        # Google Page Speed Index Section 

        def get_page_speed_insights(url, api_key):
            endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}"
            response = requests.get(endpoint)
    
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Error:", response.status_code)
            return None
        
        url = websit_url
        api_key = "AIzaSyAENmXarKSkKOzXfncCeleSmLVh6VYSfEQ"
        page_speed_data = get_page_speed_insights(url, api_key)

        data = page_speed_data

        fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        # fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]/1000
        fid = 0.01
        lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100
        speed_index = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
        blocking_time_duration = data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]


        items['meta_title'] = meta_title
        items['meta_description']=meta_description

        items['img_alt_tags']=img_alt_tags

        items['robots']=r
        items['sitexml']=sx
        items['sitehtml']=sh

        items['canonical_url']=canonical_url

        items['utf']=utf

        items['gtm_tag']=gtm_tag

        items['h1count']=h1count
        items['h2count']=h2count
        items['h3count']=h3count
        items['h4count']=h4count
        items['h5count']=h5count
        items['h6count']=h6count

        items['total_words']= total_words

        items['web_loadspeed'] = web_loadspeed

        items['mob_loadspeed']= mob_loadspeed

        items['website_url']=websit_url

        items['icc']=icc

        items['favicon_count']=favicon_count

        items['all_links']=all_links

        items['links_count']=links_count

        items['fcp']= str(fcp)
        items['fid']= str(fid)
        items['lcp']= str(lcp)
        items['cls']= str(cls)
        items['SI']= str(speed_index)
        items['total_blockingT']= str(blocking_time_duration)
        yield items 


