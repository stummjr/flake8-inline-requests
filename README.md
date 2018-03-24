# flake8-inline-requests

An experimental flake8 plugin to find possibly problematic usage of inline
requests in Scrapy spiders.


## What does it detect?

This plugin will raise a Flake8 issue when it finds inline requests such as:

```
resp = yield Request(url)
```

Instead of:

```
resp = yield Request(url, meta={'handle_httpstatus_all': True})
```


## Why

Because an inline request without `meta={'handle_httpstatus_all': True}` that
gets a 404 response (for example) will silently fail and the current callback
will stop.

With that meta param, you'll get the 404 (or whatever) response back and you can
decide what to do with that response.

## Warning

This is a highly experimental plugin and it may miss many cases.
