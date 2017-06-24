[![Build Status](https://travis-ci.org/brianmpollack/WHM-LogStash-Grok-Patterns.svg?branch=master)](https://travis-ci.org/brianmpollack/WHM-LogStash-Grok-Patterns)

## Synopsis

Grok filters for my logstash setup. I am pulling logs from WHM/CPanel servers.

## Installation

Place the grok files in /etc/logstash/patterns.d. you may have to create this directory.

## Log Examples
Example log files to which I customized my grok filters and logstash rules. If your logs look different from mine, you will need to modify these rules.

## Testing
I use pytest to test the grok patterns. To run the tests, run the command ``python -m pytest`` from the root directory of this project.
[Grok Debugger](https://grokdebug.herokuapp.com/) is a great tool to use when building grok rules.

### Apache Examples
**Generic Apache 404:** Jun 24 00:50:00 web1 apache: domain.com:80 191.168.1.1 - - [24/Jun/2017:00:50:00 -0400] "GET /custom.css HTTP/1.1" 404 1148 "http://www.referrer-domain.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"'

### Dovecot Examples
**DOVECOT_LOGIN:** Jun 11 03:25:04 web1 dovecot: imap-login: Login: user=<user@domain.com>, method=PLAIN, rip=71.237.182.194, lip=192.168.78.10, mpid=25876, TLS, session=<euPpGapR8M9H7bbC>

**DOVECOT_DISCONNECT:** Jun 24 15:06:19 web1 dovecot: imap(john@example.com): Logged out in=93, out=1020, bytes=93/1020

**DOVECOT_LMTP:** Jun 11 03:25:07 web1 dovecot: lmtp(user@domain.com): msgid=<E1dJxFC-0006k0-Pw@domain.com>: saved mail to INBOX

**DOVECOT_GENERIC:** Jun 11 03:25:06 web1 dovecot: lmtp(25929): Connect from local

### Exim Examples
[The exim docs](http://www.exim.org/exim-html-current/doc/html/spec_html/ch-log_files.html) are a great reference with log examples. The exim logs span multiple lines and are very confusing at first to understand.

**EXIM_SMTP:** 2017-06-24 15:31:43 SMTP connection from mail.example.com [192.168.1.1]:46890 closed by QUIT

**EXIM_RECEIVED:** 2017-06-24 15:41:05 1dOqvZ-0002HB-Ob <= Brain_Power_101@pour.brainpowercompletely.us H=in3f.electric.net [72.35.12.46]:47218 P=esmtps X=TLSv1.2:ECDHE-RSA-AES256-GCM-SHA384:256 CV=no S=6297 T="Millionaires, CEOs, Entrepreneurs are using brain pills to boost intelligence." for user@localdomain.com

**EXIM_DELIVERY** 2017-06-24 15:41:05 1dOqvZ-0002HB-Ob => localuser <localuser@localdomain.com> R=virtual_user T=dovecot_virtual_delivery C="250 2.0.0 <localuser@localdomain.com> AVo8MlHATlm4HgAAhX93jg Saved"

**EXIM_FAILURE:** 2017-06-18 04:03:59 1dMVBf-0007Wx-F5 ** nobody@domain.com R=virtual_aliases: No Such User Here