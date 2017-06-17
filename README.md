## Synopsis

Grok filters for my logstash setup. I am pulling logs from WHM/CPanel.

## Log Examples

### Dovecot Examples
**DOVECOT_LOGIN:** Jun 11 03:25:04 web1 dovecot: imap-login: Login: user=<user@domain.com>, method=PLAIN, rip=71.237.182.194, lip=192.168.78.10, mpid=25876, TLS, session=<euPpGapR8M9H7bbC>

**DOVECOT_DISCONNECT:** Jun 11 03:25:07 web1 dovecot: imap(user@domain.com): Connection closed (STATUS finished 1.521 secs ago) in=636, out=7911, bytes=636/7911

**DOVECOT_LMTP:** Jun 11 03:25:07 web1 dovecot: lmtp(user@domain.com): msgid=<E1dJxFC-0006k0-Pw@domain.com>: saved mail to INBOX

**DOVECOT_GENERIC:** Jun 11 03:25:06 web1 dovecot: lmtp(25929): Connect from local


## Installation

Place the grok files in /etc/logstash/patterns.d. you may have to create this directory.