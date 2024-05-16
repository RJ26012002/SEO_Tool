# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class SamplespiderPipeline:

    def __init__(self):
        self.connecting()
        self.create_table()

    
    def connecting(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '1234',
            database = 'samplespider'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS temp_data""")
        self.curr.execute("""create table temp_data(
                          meta_title text,
                          meta_description text,
                          img_alt_tags text,
                          facebook_link text,
                          instagram_link text,
                          linkedin_link text,
                          twitter_link text,
                          youtube_link text,
                          robots text,
                          sitexml text,
                          sitehtml text,
                          canonical_url text,
                          utf text,
                          gtm_tag text,
                          h1count text,
                          h2count text,
                          h3count text,
                          h4count text,
                          h5count text,
                          h6count text,
                          total_words text,
                          web_loadspeed text,
                          mob_loadspeed text,
                          website_url text,
                          icc text,
                          favicon_count text,
                          all_links text,
                          fcp text,
                          fid text,
                          lcp text,
                          cls text,
                          SI text,
                          total_blockingT text


                          
                          
                          
                         
                          
        )""")
    
    
    def insert_intodb(self,item):
        self.curr.execute("""INSERT INTO temp_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(
            item['meta_title'],
            item['meta_description'],
            item['img_alt_tags'],
            item['facebook'] ,
            item['instagram'],
            item['linkedin'],
            item['twitter'],
            item['youtube'],
            item['robots'],
            item['sitexml'],
            item['sitehtml'],
            item['canonical_url'],
            item['utf'],
            item['gtm_tag'],
            item['h1count'],
            item['h2count'],
            item['h3count'],
            item['h4count'],
            item['h5count'],
            item['h6count'],
            item['total_words'],
            item['web_loadspeed'],
            item['mob_loadspeed'],
            item['website_url'],
            item['icc'],
            item['favicon_count'],
            item['all_links'],
            item['fcp'],
            item['fid'],
            item['lcp'],
            item['cls'],
            item['SI'],
            item['total_blockingT']

         
        ))
        self.conn.commit()
    
    def process_item(self, item, spider):
        self.insert_intodb(item)
    
        return item
