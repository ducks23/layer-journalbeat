from charmhelpers.core.templating import render
from charmhelpers.core.host import service, service_running, service_available
from charmhelpers.core.hookenv import open_port, config
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.hookenv import application_name
from charmhelpers.core.hookenv import log
from charms.reactive import when, when_any, when_not, set_flag, set_state, endpoint_from_flag, when_file_changed
from charms.reactive.flags import register_trigger
from charmhelpers.core.hookenv import application_version_set
from charmhelpers.core.host import service_start, service_stop

@when_any('apt.installed.journalbeat',
          'deb.installed.journalbeat')
@when_not('journalbeat.elasticsearch.configured')
def set_available():
    log("inside the set available functon_________________________________________XxXXXXXXXX")
    set_flag('journalbeat.layer.installed') 
    status_set('active', 'layer installed')
