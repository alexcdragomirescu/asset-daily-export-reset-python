import os
import sys
import logging
import socket
import codecs
import lxml.etree as et 

from dbcmd import DbCmd
from datetime import datetime, timedelta
from remove import remove_files, remove_old_files, remove_tree
from names import breakdown
from copy_file import copy_file
from zip import zip_dir
import jinja2


dt = datetime.now()
ts = dt.strftime('%Y%m%d%H%M%S')

wd = os.path.dirname(os.path.abspath(sys.argv[0]))
logs = os.path.join(wd, 'logs')

log = os.path.join(logs, 'python_' + str(ts) + '.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(log),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Logging enabled.")
hostname = socket.gethostname()
logging.info("The script is located in \"" + wd + "\" on the machine \"" 
    + hostname + "\".")

remove_old_files(logs, 7)

log_dir = os.path.join(logs, 'reset_' + str(ts))
os.mkdir(log_dir)
dbcmd91 = DbCmd('EDITED', 'EDITED', 'EDITED', 'EDITED', 'EDITED', log_dir)



def count_mu_nodes(path_prefix):
    tree = et.parse(os.path.join(path_prefix, 'MU-NODE-LIST001.xml'))
    return int(tree.xpath('count(//MU-NODE-LIST/MU-NODE)'))
    
def count_property(path_prefix):
    tree = et.parse(os.path.join(path_prefix, 'PROPERTY-LIST001.xml'))
    return int(
        tree.xpath(
            'count(//PROPERTY-LIST/PROPERTY/STATUS-LIST/FIELD[@GROUP=\'DAILY_EXPORT\' and @VALUE = \'YES\'])'
        )
    )
    
def change_to_no(source, destination):
    input = et.parse(source)
    xslt = et.parse(os.path.join(wd, 'reset.xsl'))
    transform = et.XSLT(xslt)
    output = transform(input)
    xml = et.tostring(output, xml_declaration = True, encoding = 'utf-8', 
        standalone=False).decode()
    
    with codecs.open(destination, "w", encoding = 'utf8') as f:
        f.write(xml)

export = os.path.join(wd, 'export')
import_path_prefix = os.path.join(wd, 'import')

val_count = {
    'a': {
        'export': {},
        'reset': {}
    },
    'bfw': {
        'export': {},
        'reset': {}
    },
    'c': {
        'export': {},
        'reset': {}
    },
    'g': {
        'export': {},
        'reset': {}
    },
    'h': {
        'export': {},
        'reset': {}
    },
    'l': {
        'export': {},
        'reset': {}
    },
    'nr': {
        'export': {},
        'reset': {}
    },
    'o': {
        'export': {},
        'reset': {}
    }
}

logging.info("Processing reginal project \"Region A\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'a')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '4',
    'EDITED',
    'EDITED',
    os.path.join(export, 'a.txt')
)

logging.info("Counting pre-reset elements...")
val_count['a']['export'] = count_property(
    os.path.join(export, 'a')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'a')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'a', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'a', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '4',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'a.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'a')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '4',
    'EDITED',
    'EDITED',
    os.path.join(export, 'a.txt')
)

logging.info("Counting post-reset elements...")
val_count['a']['reset'] = count_property(
    os.path.join(export, 'a')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region A\".")



logging.info("Processing reginal project \"Region BFW\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'bfw')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '8',
    'EDITED',
    'EDITED',
    os.path.join(export, 'bfw.txt')
)

logging.info("Counting pre-reset elements...")
val_count['bfw']['export'] = count_property(
    os.path.join(export, 'bfw')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'bfw')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'bfw', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'bfw', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '8',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'bfw.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'bfw')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '8',
    'EDITED',
    'EDITED',
    os.path.join(export, 'bfw.txt')
)

logging.info("Counting post-reset elements...")
val_count['bfw']['reset'] = count_property(
    os.path.join(export, 'bfw')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region BFW\".")



logging.info("Processing reginal project \"Region C\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'c')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '14',
    'EDITED',
    'EDITED',
    os.path.join(export, 'c.txt')
)

logging.info("Counting pre-reset elements...")
val_count['c']['export'] = count_property(
    os.path.join(export, 'c')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'c')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'c', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'c', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '14',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'c.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'c')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '14',
    'EDITED',
    'EDITED',
    os.path.join(export, 'c.txt')
)

logging.info("Counting post-reset elements...")
val_count['c']['reset'] = count_property(
    os.path.join(export, 'c')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region C\".")



logging.info("Processing reginal project \"Region G\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'g')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '15',
    'EDITED',
    'EDITED',
    os.path.join(export, 'g.txt')
)

logging.info("Counting pre-reset elements...")
val_count['g']['export'] = count_property(
    os.path.join(export, 'g')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'g')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'g', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'g', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '15',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'g.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'g')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '15',
    'EDITED',
    'EDITED',
    os.path.join(export, 'g.txt')
)

logging.info("Counting post-reset elements...")
val_count['g']['reset'] = count_property(
    os.path.join(export, 'g')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region G\".")



logging.info("Processing reginal project \"Region H\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'h')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '18',
    'EDITED',
    'EDITED',
    os.path.join(export, 'h.txt')
)

logging.info("Counting pre-reset elements...")
val_count['h']['export'] = count_property(
    os.path.join(export, 'h')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'h')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'h', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'h', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '18',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'h.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'h')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '18',
    'EDITED',
    'EDITED',
    os.path.join(export, 'h.txt')
)

logging.info("Counting post-reset elements...")
val_count['h']['reset'] = count_property(
    os.path.join(export, 'h')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region H\".")



logging.info("Processing reginal project \"Region L\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'l')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '19',
    'EDITED',
    'EDITED',
    os.path.join(export, 'l.txt')
)

logging.info("Counting pre-reset elements...")
val_count['l']['export'] = count_property(
    os.path.join(export, 'l')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'l')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'l', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'l', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '19',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'l.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'l')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '19',
    'EDITED',
    'EDITED',
    os.path.join(export, 'l.txt')
)

logging.info("Counting post-reset elements...")
val_count['l']['reset'] = count_property(
    os.path.join(export, 'l')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region L\".")



logging.info("Processing reginal project \"Region NR\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'nr')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '10',
    'EDITED',
    'EDITED',
    os.path.join(export, 'nr.txt')
)

logging.info("Counting pre-reset elements...")
val_count['nr']['export'] = count_property(
    os.path.join(export, 'nr')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'nr')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'nr', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'nr', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '10',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'nr.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'nr')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '10',
    'EDITED',
    'EDITED',
    os.path.join(export, 'nr.txt')
)

logging.info("Counting post-reset elements...")
val_count['nr']['reset'] = count_property(
    os.path.join(export, 'nr')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region NR\".")



logging.info("Processing reginal project \"Region O\".")

logging.info("Removing previously exported data...")
remove_files(
    os.path.join(export, 'o')
)
logging.info("Done.")

logging.info("Exporting pre-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '13',
    'EDITED',
    'EDITED',
    os.path.join(export, 'o.txt')
)

logging.info("Counting pre-reset elements...")
val_count['o']['export'] = count_property(
    os.path.join(export, 'o')
)
logging.info("Done.")

logging.info("Removing previously edited data...")
remove_files(
    os.path.join(import_path_prefix, 'o')
)
logging.info("Done.")

logging.info("Changing \"DAILY_EXPORT\" flag to \"NO\"...")
change_to_no(
    os.path.join(export, 'o', 'PROPERTY-LIST001.xml'),
    os.path.join(import_path_prefix, 'o', 'PROPERTY-LIST001.xml')
)
logging.info("Done.")

logging.info("Importing edited data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '13',
    'EDITED',
    'EDITED',
    os.path.join(import_path_prefix, 'o.txt')
)

logging.info("Removing pre-reset exported data...")
remove_files(
    os.path.join(export, 'o')
)
logging.info("Done.")

logging.info("Exporting post-reset data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '99_NEW_PROD_ASSET_91',
    '13',
    'EDITED',
    'EDITED',
    os.path.join(export, 'o.txt')
)

logging.info("Counting post-reset elements...")
val_count['o']['reset'] = count_property(
    os.path.join(export, 'o')
)
logging.info("Done.")

logging.info("Completed reginal project \"Region O\".")



global_count = {
    'export': sum(val_count[i]['export'] for i in val_count), 
    'reset': sum(val_count[i]['reset'] for i in val_count)
}

log_basename = breakdown(log)[1]
logging.info("Copying the log at this point...")
copy_file(log, os.path.join(log_dir, log_basename))

archive_filename = 'reset_' + str(ts) + '.zip'
archive_pathname = os.path.join(logs, archive_filename)
logging.info("Archiving and compressing logs...")
zip_dir(log_dir, archive_pathname)
remove_tree(log_dir)

dt_end = datetime.now()
diff = dt_end - dt
days, seconds = diff.days, diff.seconds
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

hts = dt.strftime('%A, %B %d %Y, %H:%M:%S %p')
event_end_hts = dt_end.strftime('%A, %B %d %Y, %H:%M:%S %p')

templates = os.path.join(wd, 'templates')
logging.info("Authoring mail body...")
templateLoader = jinja2.FileSystemLoader(searchpath=templates)
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = 'admin.html'
template = templateEnv.get_template(TEMPLATE_FILE)
context = {
    'hostname': hostname,
    'wd': wd,
    'ts': str(ts),
    'hts': str(hts),
    'event_end_hts': str(event_end_hts),
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds,
    'val_count': val_count,
    'global_count': global_count
}
message_filename = 'reset_' + TEMPLATE_FILE
with open(os.path.join(wd, message_filename), 'wb') as f:
    f.write(template.render(**context).encode('utf-8'))

from sftp import SFTP
logging.info("Seding files to freetown...")
ssh = SFTP('172.31.240.82', 'taskexec', os.path.join(wd, 'freetown', 'id_rsa'))
ssh.sftp_obj.put(os.path.join(wd, message_filename), '/export/home/taskexec/send_mail/outbox/' + message_filename)
ssh.sftp_obj.put(archive_pathname, '/export/home/taskexec/send_mail/outbox/' + archive_filename)
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
        --subject 'reset_{ts}' \
        --inline_attachment '/export/home/taskexec/send_mail/outbox/{message_filename}' \
        --attachment '/export/home/taskexec/send_mail/outbox/{archive_filename}\''''.format(
        ts = str(ts), 
        message_filename = message_filename,
        archive_filename = archive_filename
    )
)
logging.info("Done.")
