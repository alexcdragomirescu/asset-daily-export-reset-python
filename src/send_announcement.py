import os
import sys
import jinja2

from sftp import SFTP
from datetime import datetime, timedelta

dt = datetime.now()

wd = os.path.dirname(os.path.abspath(sys.argv[0]))

execution_dt = dt + timedelta(days=1)
execution_hts = execution_dt.strftime('%A, %B %d %Y')
templates = os.path.join(wd, 'templates')
templateLoader = jinja2.FileSystemLoader(searchpath=templates)
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = 'announcement.html'
template = templateEnv.get_template(TEMPLATE_FILE)
context = {'event_time': str(event_time)}
message_filename = 'reset_' + TEMPLATE_FILE
with open(os.path.join(wd, message_filename), 'wb') as f:
    f.write(template.render(**context).encode('utf-8'))

ssh = SFTP('172.31.240.82', 'taskexec', os.path.join(wd, 'freetown', 'id_rsa'))
ssh.sftp_obj.put(os.path.join(wd, message_filename), '/export/home/taskexec/send_mail/outbox/' + message_filename)
ssh.command('''python /export/home/taskexec/send_mail/mail.py \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --to 'EDITED' \
        --subject 'DAILY_EXPORT Flag Reset on {execution_hts}' \
        --inline_attachment '/export/home/taskexec/send_mail/outbox/{message_filename}\''''.format(
        execution_hts = str(execution_hts), 
        message_filename = message_filename
    )
)
