import os.path
import pytest
from pygrok import Grok

def test_dovecot_login():
    """Test POP or IMAP login (user checking his or her email from a mail client)"""
    log_entry = 'Jun 24 15:06:14 web1 dovecot: imap-login: Login: user=<info@domain.com>, '\
                'method=PLAIN, rip=192.168.1.1, lip=192.168.1.2, mpid=22445, '\
                'TLS, session=<sessionid>'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOGBASE} %{DOVECOT_LOGIN}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    print grok_output
    assert grok_output['program'] == 'dovecot'
    assert grok_output['dovecot_protocol'] == 'imap'
    assert grok_output['timestamp'] == 'Jun 24 15:06:14'
    assert grok_output['dovecot_login_result'] == 'Login'
    assert grok_output['dovecot_user'] == 'info@domain.com'
    assert grok_output['dovecot_auth_method'] == 'PLAIN'
    assert grok_output['dovecot_client_ip'] == '192.168.1.1'
    assert grok_output['dovecot_server_ip'] == '192.168.1.2'
    assert grok_output['dovecot_session'] == 'sessionid'
