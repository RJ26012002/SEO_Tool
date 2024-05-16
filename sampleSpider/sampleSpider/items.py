# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SamplespiderItem(scrapy.Item):
    meta_title = scrapy.Field()
    meta_description = scrapy.Field()
    img_alt_tags = scrapy.Field()
    facebook = scrapy.Field()
    youtube=scrapy.Field()
    twitter = scrapy.Field()
    instagram=scrapy.Field()
    linkedin = scrapy.Field()
    robots=scrapy.Field()
    sitexml=scrapy.Field()
    sitehtml=scrapy.Field()
    canonical_url = scrapy.Field()
    utf=scrapy.Field()
    gtm_tag=scrapy.Field()
    h1count=scrapy.Field()
    h2count=scrapy.Field()
    h3count=scrapy.Field()
    h4count=scrapy.Field()
    h5count=scrapy.Field()
    h6count=scrapy.Field()
    total_words=scrapy.Field()
    web_loadspeed = scrapy.Field()
    mob_loadspeed = scrapy.Field()
    website_url = scrapy.Field()
    icc = scrapy.Field()
    favicon_count=scrapy.Field()
    all_links = scrapy.Field() 
    links_count = scrapy.Field()
    fcp = scrapy.Field()
    fid = scrapy.Field()
    lcp = scrapy.Field()
    cls = scrapy.Field()
    SI = scrapy.Field()
    total_blockingT = scrapy.Field()