from datetime import datetime
from decimal import *
from vultr import Vultr
from cfg.R import getconfig

vultr = Vultr(getconfig('vultr', 'apiKey'))
vultr.api_endpoint = '66.55.134.142'


def clean_server():
    jsondata: dict = vultr.server.list()
    subids: list = sorted(jsondata,
                          key=lambda d: datetime.strptime(jsondata.get(d)['date_created'], '%Y-%m-%d %H:%M:%S'),
                          reverse=True)
    subids.pop(0)
    for sub_id in subids:
        distroy_server(sub_id)


def distroy_server(subid):
    resp = vultr.server.destroy(subid)
    print(resp)


def create_server():
    param = {
        'SNAPSHOTID': getconfig('vultr', 'snapshotId'),
        'SSHKEYID': getconfig('vultr', 'sshKeyIds').split(','),
    }
    region_id = get_prefer_region_id()
    plan_id = get_cheap_plan_id(region_id)
    # odid=164 means create vm from snapshot
    vultr.server.create(dcid=int(region_id), vpsplanid=plan_id, osid=164, params=param)


def get_cheap_plan_id(regionid):
    plans_list: dict = vultr.plans.list({'type': 'vc2'})
    for plan in plans_list.values():
        if plan.get('available_locations') is not None and (int(regionid) in plan.get('available_locations')):
            price = plan.get('price_per_month', None)
            if (price is not None) and (Decimal(price) == 5 or Decimal(price) == 2.5):
                return plan['VPSPLANID']

    return next(iter(plans_list.items())).get('VPSPLANID')


def get_prefer_region_id():
    datastr: dict = vultr.regions.list()
    locations = getconfig('vultr', 'preferLocationIds').split(',')
    for location in locations:
        if datastr.get(location, None) is not None:
            return location
    return next(iter(datastr.items()))


print(vultr.server.list())
