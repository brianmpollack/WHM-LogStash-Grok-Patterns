import os.path
import pytest
from pygrok import Grok

def test_exim_smtp():
    """Test exim incoming smtp delivery."""
    log_entry = '2017-06-24 15:31:43 SMTP connection from mail.example.com '\
                '[192.168.1.1]:46890 closed by QUIT'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOG_EXIM}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    assert grok_output['exim_port'] == '46890'
    assert grok_output['exim_url'] == 'mail.example.com'
    assert grok_output['exim_ip_address'] == '192.168.1.1'
    assert grok_output['exim_smtp_message'] == 'closed by QUIT'
    assert grok_output['exim_timestamp'] == '2017-06-24 15:31:43'

def test_exim_received():
    """Test exim incoming email"""
    log_entry = '2017-06-24 15:41:05 1dOqvZ-0002HB-Ob <= '\
                'Brain_Power_101@pour.brainpowercompletely.us H=in3f.electric.net '\
                '[72.35.12.46]:47218 P=esmtps X=TLSv1.2:ECDHE-RSA-AES256-GCM-SHA384:256 '\
                'CV=no S=6297 T="Millionaires, CEOs, Entrepreneurs are using brain pills '\
                'to boost intelligence." for user@localdomain.com'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOG_EXIM}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    assert grok_output['exim_timestamp'] == '2017-06-24 15:41:05'
    assert grok_output['exim_log_id'] == '1dOqvZ-0002HB-Ob'
    assert grok_output['exim_remote_host'] == 'in3f.electric.net'
    assert grok_output['exim_remote_ip'] == '72.35.12.46'
    assert grok_output['exim_tls_cipher'] == 'TLSv1.2:ECDHE-RSA-AES256-GCM-SHA384:256'
    assert grok_output['exim_tls_certificate_verified'] == 'no'
    assert grok_output['exim_sender_address'] == 'Brain_Power_101@pour.brainpowercompletely.us'
    assert grok_output['exim_port'] == '47218'
    assert grok_output['exim_protocol'] == 'esmtps'
    assert grok_output['exim_message_size'] == '6297'
    assert grok_output['exim_subject'] == 'Millionaires, CEOs, Entrepreneurs '\
                                        'are using brain pills to boost intelligence.'

def test_exim_delivery():
    """Test exim message delivery"""
    log_entry = '2017-06-24 15:41:05 1dOqvZ-0002HB-Ob => localuser '\
                '<localuser@localdomain.com> R=virtual_user '\
                'T=dovecot_virtual_delivery C="250 2.0.0 '\
                '<localuser@localdomain.com> AVo8MlHATlm4HgAAhX93jg Saved"'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOG_EXIM}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    assert grok_output['exim_timestamp'] == '2017-06-24 15:41:05'
    assert grok_output['exim_log_id'] == '1dOqvZ-0002HB-Ob'
    assert grok_output['exim_final_delivery_address'] == 'localuser'
    assert grok_output['exim_original_delivery_address'] == 'localuser@localdomain.com'
    assert grok_output['exim_router'] == 'virtual_user'
    assert grok_output['exim_transport'] == 'dovecot_virtual_delivery'
    assert grok_output['exim_smtp_confirmation'] == '250 2.0.0 '\
            '<localuser@localdomain.com> AVo8MlHATlm4HgAAhX93jg Saved'

def test_exim_failure():
    """Test exim message failure"""
    log_entry = '2017-06-18 04:03:59 1dMVBf-0007Wx-F5 ** '\
                'nobody@domain.com R=virtual_aliases: No Such User Here'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOG_EXIM}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    assert grok_output['exim_timestamp'] == '2017-06-18 04:03:59'
    assert grok_output['exim_log_id'] == '1dMVBf-0007Wx-F5'
    assert grok_output['exim_final_delivery_address'] == 'nobody@domain.com'
    assert grok_output['exim_router'] == 'virtual_aliases'
    assert grok_output['exim_failure_message'] == 'No Such User Here'

def test_exim_smtp_outgoing():
    """Test exim outgoing smtp"""
    log_entry = '2017-06-24 23:36:21 1dOyLV-000359-20 SMTP connection outbound '\
                '1498361781 1dOyLV-000359-20 domain.com user@externaldomain.com'
    patterns_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
                            '../patterns.d')
    grok_output = Grok('%{SYSLOG_EXIM}', \
                    custom_patterns_dir=patterns_directory).match(log_entry)
    assert grok_output['exim_log_id'] == '1dOyLV-000359-20'
    assert grok_output['exim_sender'] == 'domain.com'
    assert grok_output['exim_external_recipient'] == 'user@externaldomain.com'
    assert grok_output['exim_timestamp'] == '2017-06-24 23:36:21'
