__author__ = 'adm'

import xml.etree.ElementTree as ET

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<findItemsAdvancedResponse>
	<ack>Success</ack>
	<version>1.12.0</version>
	<timestamp>2014-04-06T15:51:41.551Z</timestamp>
	<searchResult count="2">
		<item>
			<itemId>321366006702</itemId>
			<title>Nexus 7 8GB, Wi-Fi, 7in - Black (1 Gen)</title>
			<globalId>EBAY-US</globalId>
			<primaryCategory>
				<categoryId>171485</categoryId>
				<categoryName>iPads, Tablets &amp; eBook Readers</categoryName>
			</primaryCategory>
			<galleryURL>http://thumbs3.ebaystatic.com/m/malh52tRWH-JZP8CVvJBUFw/140.jpg</galleryURL>
			<viewItemURL>http://www.ebay.com/itm/Nexus-7-8GB-Wi-Fi-7in-Black-1-Gen-/321366006702?pt=US_Tablets</viewItemURL>
			<productId type="ReferenceID">115431290</productId>
			<paymentMethod>PayPal</paymentMethod>
			<autoPay>false</autoPay>
			<postalCode>06484</postalCode>
			<location>Shelton,CT,USA</location>
			<country>US</country>
			<sellerInfo>
				<sellerUserName>erickrdch</sellerUserName>
				<feedbackScore>5</feedbackScore>
				<positiveFeedbackPercent>0.0</positiveFeedbackPercent>
				<feedbackRatingStar>None</feedbackRatingStar>
				<topRatedSeller>false</topRatedSeller>
			</sellerInfo>
			<shippingInfo>
				<shippingServiceCost currencyId="USD">0.0</shippingServiceCost>
				<shippingType>Free</shippingType>
				<shipToLocations>US</shipToLocations>
				<expeditedShipping>false</expeditedShipping>
				<oneDayShippingAvailable>false</oneDayShippingAvailable>
				<handlingTime>2</handlingTime>
			</shippingInfo>
			<sellingStatus>
				<currentPrice currencyId="USD">75.0</currentPrice>
				<convertedCurrentPrice currencyId="USD">75.0</convertedCurrentPrice>
				<bidCount>35</bidCount>
				<sellingState>Active</sellingState>
				<timeLeft>P0DT0H14M10S</timeLeft>
			</sellingStatus>
			<listingInfo>
				<bestOfferEnabled>false</bestOfferEnabled>
				<buyItNowAvailable>false</buyItNowAvailable>
				<startTime>2014-03-30T16:05:51.000Z</startTime>
				<endTime>2014-04-06T16:05:51.000Z</endTime>
				<listingType>Auction</listingType>
				<gift>false</gift>
			</listingInfo>
			<returnsAccepted>false</returnsAccepted>
			<condition>
				<conditionId>3000</conditionId>
				<conditionDisplayName>Used</conditionDisplayName>
			</condition>
			<isMultiVariationListing>false</isMultiVariationListing>
			<topRatedListing>false</topRatedListing>
		</item>
		<item>
			<itemId>123456789001</itemId>
			<title>Nexus My try </title>
			<globalId>EBAY-US</globalId>
			<primaryCategory>
				<categoryId>171485</categoryId>
				<categoryName>iPads, Tablets &amp; eBook Readers</categoryName>
			</primaryCategory>
			<galleryURL>http://thumbs3.ebaystatic.com/m/malh52tRWH-JZP8CVvJBUFw/140.jpg</galleryURL>
			<viewItemURL>http://www.ebay.com/itm/Nexus-7-8GB-Wi-Fi-7in-Black-1-Gen-/321366006702?pt=US_Tablets</viewItemURL>
			<productId type="ReferenceID">115431290</productId>
			<paymentMethod>PayPal</paymentMethod>
			<autoPay>false</autoPay>
			<postalCode>06484</postalCode>
			<location>Shelton,CT,USA</location>
			<country>US</country>
			<sellerInfo>
				<sellerUserName>erickrdch</sellerUserName>
				<feedbackScore>5</feedbackScore>
				<positiveFeedbackPercent>0.0</positiveFeedbackPercent>
				<feedbackRatingStar>None</feedbackRatingStar>
				<topRatedSeller>false</topRatedSeller>
			</sellerInfo>
			<shippingInfo>
				<shippingServiceCost currencyId="USD">9.99</shippingServiceCost>
				<shippingType>Free</shippingType>
				<shipToLocations>US</shipToLocations>
				<expeditedShipping>false</expeditedShipping>
				<oneDayShippingAvailable>false</oneDayShippingAvailable>
				<handlingTime>2</handlingTime>
			</shippingInfo>
			<sellingStatus>
				<currentPrice currencyId="USD">99.9</currentPrice>
				<convertedCurrentPrice currencyId="USD">99.9</convertedCurrentPrice>
				<bidCount>35</bidCount>
				<sellingState>Active</sellingState>
				<timeLeft>P0DT0H14M10S</timeLeft>
			</sellingStatus>
			<listingInfo>
				<bestOfferEnabled>false</bestOfferEnabled>
				<buyItNowAvailable>false</buyItNowAvailable>
				<startTime>2014-03-30T16:05:51.000Z</startTime>
				<endTime>2014-04-06T16:05:51.000Z</endTime>
				<listingType>Auction</listingType>
				<gift>false</gift>
			</listingInfo>
			<returnsAccepted>false</returnsAccepted>
			<condition>
				<conditionId>3000</conditionId>
				<conditionDisplayName>Used</conditionDisplayName>
			</condition>
			<isMultiVariationListing>false</isMultiVariationListing>
			<topRatedListing>false</topRatedListing>
		</item>
	</searchResult>
	<paginationOutput>
		<pageNumber>1</pageNumber>
		<entriesPerPage>2</entriesPerPage>
		<totalPages>247</totalPages>
		<totalEntries>494</totalEntries>
	</paginationOutput>
	<itemSearchURL>http://www.ebay.com/sch/171485/i.html?LH_ItemCondition=2&amp;_nkw=Nexus+7&amp;_ddo=1&amp;_ipg=2&amp;_mPrRngCbx=1&amp;_os=S%7CD&amp;_pgn=1&amp;_udhi=140</itemSearchURL>
</findItemsAdvancedResponse>'''

def parser(data):
    cont = ET.fromstring(data) #returns document
    #print 'itemId:', cont.findall('.//itemId'), len(cont.findall('.//itemId'))
    count = len(cont.findall('.//itemId'))
    for i in xrange(0,count):
        print cont.findall('.//itemId')[i].text, cont.findall('.//title')[i].text, cont.findall('.//shippingServiceCost')[i].text, cont.findall('.//currentPrice')[i].text, cont.findall('.//endTime')[i].text, cont.findall('.//conditionDisplayName')[i].text

    #print 'title:', cont.find('.//title').text
    #print 'Price:', cont.find('.//currentPrice').text
    #print 'Shipping:', cont.find('.//shippingServiceCost').text
    #print 'End time:', cont.find('.//endTime').text
    #print 'condition:', cont.find('.//conditionDisplayName').text

    #print content.getchildren()[3].getchildren()[0].getchildren()[0].text
    #print content.getiterator()
    #all = content.findall('country')
    #s = all[2].getchildren()
    #print s[0].getchildren()[0]
    return

if __name__ == "__main__":
    parser(xml)