CloudFlareDNS
=============

I forked this code to mess with [vladc](https://github.com/vladc). It's never been tested. Heck, it has never been run. Don't make merge requests here, send them toward the original author. He might actually do something about it.

Configuration
=============
Before executing, you should update the following variables at the top of the script.

cloudflareEmail="EMAIL@EXAMPLE.COM" #CF Login Email Address
cloudflareAPIkey="cloudflareapikeylowercase" #API Key as shown on https://www.cloudflare.com/my-account
baseDomain='yourdomain.com' #Domain Name as shown on https://www.cloudflare.com/my-websites.html
recordType='A' #See "Type" Column on https://www.cloudflare.com/dns-settings?z=example.com
recordName='yoursubdomain' #See "Name" Column on https://www.cloudflare.com/dns-settings?z=example.com

Disclaimer
==========
Please note, I did absolutely nothing to fix existing defects and copied them as best I could. There are at least 3 I can spot by cursory inspection reading the [CloudFlare API documentation here](https://www.cloudflare.com/docs/client-api.html). Additionally, if it gets an error back from CF, or no-response from ip-api, it will still try to write updates back to CF. Use at your own risk.

License
=======
Original code is probably all-rights-reserved as it has no listed license. Updates by me are made under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
