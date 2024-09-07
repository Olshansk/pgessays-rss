Paul Graham's website links to an old RSS feed at this link: http://www.aaronsw.com/2002/feeds/pgessays.rss

It looks like so

````xml
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel>
  <title>Paul Graham: Essays</title>
  <link>http://www.paulgraham.com/</link>
  <description>Scraped feed provided by aaronsw.com</description>
  <item>
    <link>http://www.paulgraham.com/superlinear.html</link>
    <title>Superlinear Returns</title>
  </item>
  <item>
    <link>http://www.paulgraham.com/greatwork.html</link>
    <title>How to Do Great Work</title>
  </item>
  <item>
    <link>http://www.paulgraham.com/getideas.html</link>
    <title>How to Get New Ideas</title>
  </item>
  <item>
    <link>http://www.paulgraham.com/read.html</link>
    <title>The Need to Read</title>
  </item>
  <item>
    <link>http://www.paulgraham.com/want.html</link>
    <title>What You (Want to)* Want</title>
  </item>
  <item>
    <link>http://www.paulgraham.com/alien.html</link>
    <title>Alien Truth</title>
...

He links to it the RSS feed from the following link for reference: https://www.paulgraham.com/rss.html

However, this is outdated and there are my new essays available at here: https://www.paulgraham.com/articles.html

In particular, here is the tbody on the webiste above:

```html
<tbody><tr><td><img src="https://sep.turbifycdn.com/ca/Img/trans_1x1.gif" height="5" width="1" border="0"></td></tr><tr valign="top"><td width="435"><img src="https://s.turbifycdn.com/aah/paulgraham/the-reddits-2.gif" width="12" height="14" align="left" border="0" hspace="0" vspace="0"><font size="2" face="verdana"><a href="foundermode.html">Founder Mode</a><img src="https://sep.turbifycdn.com/ca/Img/trans_1x1.gif" height="2" width="1" border="0"><br></font></td></tr><tr><td><img src="https://sep.turbifycdn.com/ca/Img/trans_1x1.gif" height="5" width="1" border="0"></td></tr><tr valign="top"><td width="435"><img src="https://s.turbifycdn.com/aah/paulgraham/the-reddits-2.gif" width="12" height="14" align="left" border="0" hspace="0" vspace="0"><font size="2" face="verdana"><a href="persistence.html">The Right Kind of Stubborn</a><img src="https://sep.turbifycdn.com/ca/Img/trans_1x1.gif" ...
````

I want to have an updated RSS feed myself and others could use and am thinking of doing this:

1. Write a A python script that:

   - Scrapes https://www.paulgraham.com/articles.html
   - Generates an XML feed similar to http://www.aaronsw.com/2002/feeds/pgessays.rss

2. Use GitHub actions to run this daily or weekly
3. Host the feed on GitHub pages

I have two questions:

1. Can you think of a better approach?
2. If so, what is it?
3. If not, please provide all the code I need for this.
