import os.path
from pygrok import Grok
import pytest

class Test:
    def test_apache(self):
        """Test simple Apache 404 log."""
        log_entry = 'Jun 24 00:50:00 web1 apache: domain.com:80 191.168.1.1 - - '\
                '[24/Jun/2017:00:50:00 -0400] "GET /custom.css HTTP/1.1" 404 1148 '\
                '"http://www.referrer-domain.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 '\
                'Edge/14.14393"'
        patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
        grok_output = Grok('%{APACHE_SYSLOG}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
        assert grok_output['program'] == 'apache'
        assert grok_output['verb'] == 'GET'
        assert grok_output['timestamp'] == '24/Jun/2017:00:50:00 -0400'
        assert grok_output['request'] == '/custom.css'
        assert grok_output['apache_port'] == '80'
        assert grok_output['clientip'] == '191.168.1.1'
        assert grok_output['apache_domain'] == 'domain.com'
        assert grok_output['response'] == '404'
        assert grok_output['referrer'] == '"http://www.referrer-domain.com/"'
        assert grok_output['agent'] == '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '\
                                    'Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"'

