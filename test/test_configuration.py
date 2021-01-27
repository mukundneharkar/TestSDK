import sys
from pprint import pprint

sys.path.append("..")
import lmingest

conf = lmingest.Configuration(company="",
                              authentication={'id': 'asd', 'key': 'asdd'})
print(conf._authentication)
conf.authentication = {'id': 'asdsd', 'key': 'asdad'}
pprint(conf.__dict__)
