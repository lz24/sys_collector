#!/usr/bin/env python
# coding=utf-8

#Author: ymc023
#Mail:
#Platform:python2.x.x && python3.x.x
#Date:Mon 12 Jun 2017 12:24:51 PM CST
#Update: Wed 16 Aug 2017

import os
import sys
import datetime
import platform
import glob
import re
import socket
import subprocess
import time
import urllib2
import re

# Useful for very coarse version differentiation.
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

YMFLY = re.compile(r'\w*\.ymfly\.(com|lo)$')
APP_INSTANCE_P = re.compile(r'\w+\.ymfly\.\w+/server\d+')
APP_INSTANCE = re.compile(r'\w+\.ymfly\.\w+')
SPRING_APP = re.compile(r'\w+\.ymfly\.\w+/release/')
APP_PATH='/home/App'

JMX_PORT = re.compile(r'jmxremote.port=\d+')
NTP_CRON = re.compile(r'ntpdate ntp.ymfly.com')

CLEAN_RETURN=re.compile(r'\n$')
CLOCK_TICKS = os.sysconf("SC_CLK_TCK")

sys.path.append(os.getcwd()+'/../bin/')



if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
    MAXSIZE = sys.maxsize
    _meth_func = "__func__"
    _meth_self = "__self__"
    _func_closure = "__closure__"
    _func_code = "__code__"
    _func_defaults = "__defaults__"
    _func_globals = "__globals__"
    _iterkeys = "keys"
    _itervalues = "values"
    _iteritems = "items"
    _iterlists = "lists"

if PY2:
    _meth_func = "im_func"
    _meth_self = "im_self"
    _func_closure = "func_closure"
    _func_code = "func_code"
    _func_defaults = "func_defaults"
    _func_globals = "func_globals"
    _iterkeys = "iterkeys"
    _itervalues = "itervalues"
    _iteritems = "iteritems"
    _iterlists = "iterlists"

try:
    import json
    # Detect python-json which is incompatible and fallback to simplejson in
except ImportError:
    import simplejson as json


def get_file_content(path, default=None, strip=True):
    """ return file content """
    data = default
    if os.path.exists(path) and os.access(path, os.R_OK):
        try:
            try:
                datafile = open(path)
                data = datafile.read()
                if strip:
                    data = data.strip()
                if len(data) == 0:
                    data = default
            finally:
                datafile.close()
        except:
            # done in 2 blocks for 2.4 compat
            pass
    return data

def usage_percent(used, total,mark=None):
    """Calculate percentage usage of 'used'."""
    try:
        ret = float(used) / float(total) * 100
    except ZeroDivisionError:
        ret = 0.0 if isinstance(used, float) or isinstance(total, float) else 0
    return float(ret)

def available_percent(available, total,mark=None):
    """Calculate percentage of  available"""
    try:
        ret = float(available) / float(total) * 100
    except ZeroDivisionError:
        ret = 0.0 if isinstance(available, float) or isinstance(total, float) else 0
    return float(ret)

def get_file_lines(path):
    ''' get list of lines from file '''
    data = get_file_content(path)
    if data:
        ret = data.splitlines()
    else:
        ret = []
    return ret

def iteritems(d, **kw):
    return iter(getattr(d, _iteritems)(**kw))

def imsh(cmd):
    ''' return cmd result '''
    args = cmd
    pro = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std = pro.stdout.readlines()
    err = pro.stderr.readlines()
    return std

''' define /etc/sysctl.conf '''
sysctlt = {'net_core_wmem_default':'8388608',
                  'net_core_rmem_default':'8388608',
                  'net_core_rmem_max':'16777216',
                  'net_core_wmem_max':'16777216',
                  'net_ipv4_tcp_timestamps':'0',
                  'net_ipv4_tcp_synack_retries':'1',
                  'net_ipv4_tcp_tw_recycle':'1',
                  'net_ipv4_tcp_tw_reuse':'1',
                  'net_ipv4_tcp_mem':'94500000\t915000000\t927000000',
                  'net_ipv4_tcp_max_orphans':'3276800',
                  'net_ipv4_ip_local_port_range':'1024\t65535',
                  'net_ipv4_tcp_fin_timeout':'10',
                  'net_ipv4_tcp_keepalive_time':'100',
                  'net_ipv4_tcp_syncookies':'1',
                  'net_ipv4_tcp_max_syn_backlog':'819200',
                  'net_ipv4_tcp_max_tw_buckets':'20000',
                  'net_ipv4_tcp_rmem':'4096\t87380\t16777216',
                  'net_ipv4_tcp_wmem':'4096\t65536\t16777216',
                  'net_core_netdev_max_backlog':'300000',
                  'net_ipv4_ip_forward':'1',
                  'net_ipv4_tcp_ecn':'0',
                  'net_ipv4_ip_nonlocal_bind':'1',
                  'net_ipv4_conf_all_arp_announce':'2',
                  'net_ipv4_conf_all_arp_ignore':'1',
                  'net_ipv4_conf_default_rp_filter':'0',
                  'fs_inotify_max_user_instances':'1280',
                  #'fs_inotify_max_queued_events':'163840',
                  #'fs_inotify_max_user_watches':'8192000',
                  'vm_swappiness':'10',
                  'vm_drop_caches':'2',
                  'net_ipv4_tcp_retries2':'5',
                  'net_core_somaxconn':'300000'
                  }
sysctlpath = {
        'net_core_wmem_default':'/proc/sys/net/core/wmem_default',
        'net_core_rmem_default':'/proc/sys/net/core/rmem_default',
        'net_core_rmem_max':'/proc/sys/net/core/rmem_max',
        'net_core_wmem_max':'/proc/sys/net/core/wmem_max',
        'net_ipv4_tcp_timestamps':'/proc/sys/net/ipv4/tcp_timestamps',
        'net_ipv4_tcp_synack_retries':'/proc/sys/net/ipv4/tcp_synack_retries',
        'net_ipv4_tcp_tw_recycle':'/proc/sys/net/ipv4/tcp_tw_recycle',
        'net_ipv4_tcp_tw_reuse':'/proc/sys/net/ipv4/tcp_tw_reuse',
        'net_ipv4_tcp_mem':'/proc/sys/net/ipv4/tcp_mem',
        'net_ipv4_tcp_max_orphans':'/proc/sys/net/ipv4/tcp_max_orphans',
        'net_ipv4_ip_local_port_range':'/proc/sys/net/ipv4/ip_local_port_range',
        'net_ipv4_tcp_fin_timeout':'/proc/sys/net/ipv4/tcp_fin_timeout',
        'net_ipv4_tcp_keepalive_time':'/proc/sys/net/ipv4/tcp_keepalive_time',
        'net_ipv4_tcp_syncookies':'/proc/sys/net/ipv4/tcp_syncookies',
        'net_ipv4_tcp_max_syn_backlog':'/proc/sys/net/ipv4/tcp_max_syn_backlog',
        'net_ipv4_tcp_max_tw_buckets':'/proc/sys/net/ipv4/tcp_max_tw_buckets',
        'net_ipv4_tcp_rmem':'/proc/sys/net/ipv4/tcp_rmem',
        'net_ipv4_tcp_wmem':'/proc/sys/net/ipv4/tcp_wmem',
        'net_core_netdev_max_backlog':'/proc/sys/net/core/netdev_max_backlog',
        'net_ipv4_ip_forward':'/proc/sys/net/ipv4/ip_forward',
        'net_ipv4_tcp_ecn':'/proc/sys/net/ipv4/tcp_ecn',
        'net_ipv4_ip_nonlocal_bind':'/proc/sys/net/ipv4/ip_nonlocal_bind',
        'net_ipv4_conf_all_arp_announce':'/proc/sys/net/ipv4/conf/all/arp_announce',
        'net_ipv4_conf_all_arp_ignore':'/proc/sys/net/ipv4/conf/all/arp_ignore',
        'net_ipv4_conf_default_rp_filter':'/proc/sys/net/ipv4/conf/default/rp_filter',
        'fs_inotify_max_user_instances':'/proc/sys/fs/inotify/max_user_instances',
        #'fs_inotify_max_queued_events':'/proc/sys/fs/inotify/max_queued_events',
        #'fs_inotify_max_user_watches':'/proc/sys/fs/inotify/max_user_watches',
        'vm_swappiness':'/proc/sys/vm/swappiness',
        'vm_drop_caches':'/proc/sys/vm/drop_caches',
        'net_ipv4_tcp_retries2':'/proc/sys/net/ipv4/tcp_retries2',
        'net_core_somaxconn':'/proc/sys/net/core/somaxconn'
}
def get_ip():
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   try:
       s.connect(('10.255.255.255', 0))
       IP = s.getsockname()[0]
   except:
       IP = '127.0.0.1'
   finally:
       s.close()
   return IP


class CollectorBase(object):
    ''' collecotr server info '''
    def __init__(self,write_file=None):
        self.info = {}
        self.get_platform_info()
        self.get_env_info()
        self.get_mem_info()
        self.get_mount_info()
        self.get_interfaces_info()
        self.get_cpu_info()
        self.get_network_flow()

    ''' platform '''
    def get_platform_info(self):
        self.info['sys'] = {}
        self.info['sys']['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.info['sys']['ipaddress'] = get_ip()
        self.info['sys']['kernel'] = platform.release()
        self.info['sys']['arch'] = platform.machine()
        self.info['sys']['python'] = platform.python_version()
        self.info['sys']['hostname'] = platform.node()
        self.info['sys']['glibc'] = platform.libc_ver()[1]
        self.info['sys']['dist'] = platform.dist()[0]+platform.dist()[1]
        self.info['sys']['uptime_seconds'] = self.get_uptime_info()
        self.info['sys']['app'] = self.get_app_info()
        self.info['sys']['app_jmx'] = self.get_app_jmx()
        self.info['sys']['dns'] = self.get_dns_info()

    def _network_stat(self,device=None):
        net = []
        lines = get_file_lines("/proc/net/dev")
        for line in lines[2:]:
            con = line.split()
            if device in line and device == str((con[0].lstrip(":")).strip(":")):
                intf = {}
                net.append(int(con[1]))
                net.append(int(con[9]))

                intf[con[0].lstrip(":")] = {"device": con[0].lstrip(":")}
                intf[con[0].lstrip(":")]['ReceiveBytes'] = int(con[1])
                intf[con[0].lstrip(":")]['ReceivePackets'] = int(con[2])
                intf[con[0].lstrip(":")]['ReceiveErrs'] = int(con[3])
                intf[con[0].lstrip(":")]['ReceiveDrop'] = int(con[4])
                intf[con[0].lstrip(":")]['ReceiveFifo'] = int(con[5])
                intf[con[0].lstrip(":")]['ReceiveFrames'] = int(con[6])
                intf[con[0].lstrip(":")]['ReceiveCompressed'] = int(con[7])
                intf[con[0].lstrip(":")]['ReceiveMulticast'] = int(con[8])

                intf[con[0].lstrip(":")]['TransmitBytes'] = int(con[9])
                intf[con[0].lstrip(":")]['TransmitPackets'] = int(con[10])
                intf[con[0].lstrip(":")]['TransmitErrs'] = int(con[11])
                intf[con[0].lstrip(":")]['TransmitDrop'] = int(con[12])
                intf[con[0].lstrip(":")]['TransmitFifo'] = int(con[13])
                intf[con[0].lstrip(":")]['TransmitFrames'] = int(con[14])
                intf[con[0].lstrip(":")]['TransmitCompressed'] = int(con[15])
                intf[con[0].lstrip(":")]['TransmitMulticast'] = int(con[16])
                net.append(intf)
        return net

    def get_network_flow(self,device="bond0"):
        net_flow = self._network_stat(device)
        time.sleep(1)
        net1_flow = self._network_stat(device)

        n_f = [round(float(net1_flow[i] - net_flow[i])/1024/1024,2) for i in range(len(net_flow))]

        return n_f

        #try:
        #    for i in range(len(net_flow)):
        #        for k,v in net_flow[i].items():
        #            for p,ve in v.items():
        #                if net1_flow[i][k].get(p) and str(ve).isalnum():
        #                    net_flow[i][k][p] = net1_flow[i][k][p] - net_flow[i][k][p]
        #
        #except Exception :
        #    self.info["net_flow"] = None

    def get_app_jmx(self):
        app_info = self.get_app_info()
        app_jmx = []
        if isinstance(app_info,list):
            for app_name in app_info:
                pids = imsh(cmd="ps -ef |grep java |grep '%s' |grep -v grep |awk '{print $2}'"%app_name)
                if pids and isinstance(pids,list):
                    for pid in pids:
                        jmx_remote_port = self.cmdline(re.sub('\n','',pid))
                        app_jmx.append(jmx_remote_port)
                else:
                    app_jmx.append({"%s"%app_name:"no_java_pid"})
        else:
            app_jmx.append('no app')
        return app_jmx

    def get_app_info(self):
        raw = imsh(cmd='ls %s'%APP_PATH)
        normal_app_info = self._cleandata(raw)
        if normal_app_info:
            return normal_app_info
        else:
            return "no app"

    ''' return process id cmdline (/proc/processid/cmdline)'''
    def cmdline(self,pid):
        with open ("/proc/%s/cmdline" % (pid)) as f:
            data = f.read()
            try:
                _type = re.search(SPRING_APP,data).group(0)
                if _type:
                    app_type = 'SpringCloud'
            except:
                app_type = 'Tomcat'
            try:
                jmx_port = re.search(JMX_PORT,data).group(0)
            except:
                jmx_port = 'no_jmx_port'
            try:
                app_instance = re.sub('/','-',re.search(APP_INSTANCE_P,data).group(0))
            except:
                try:
                    app_instance = re.search(APP_INSTANCE,data).group(0)
                except:
                    app_instance = 'no_app'
            try:
                app_jmx_dict = {"%s"%app_instance:["%s"%jmx_port,"%s"%app_type]}
            except:
                app_jmx_dict = {}

            #print ('jmx port:',jmx_port)
            #if data.endswith('\x00'):
            #    data = data[:-1]
            #    print ('end \x00',[x for x in data.split('\x00')])

        return app_jmx_dict if app_jmx_dict else 'no_data'

    def _cleandata(self,data):
        normal = []
        abnormal = []
        c_data = [CLEAN_RETURN.sub('',i) for i in data]
        try:
            for i in c_data:
                normal.append(i) if re.match(YMFLY,CLEAN_RETURN.sub('',i)) else abnormal.append(i)
        except Exception ,e:
            print ("ERROR %s"%e)
        return normal

    def get_env_info(self):
        self.info['env'] = {}
        for k,v in iteritems(os.environ):
            if k in ['PATH','LANG','NVM_DIR','JAVA_HOME','HISTSIZE','TMOUT']:
                self.info['env'][k] = v

    def get_dns_info(self):
        for line in get_file_content('/etc/resolv.conf', '').splitlines():
            if line.startswith('#') or line.startswith(';') or line.strip() == '':
                continue
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] == 'nameserver':
                return tokens[1]
            else:
                return 'no dns'

    def _get_cpu_load(self):
        cpu_load_1, cpu_load_5, cpu_load_15 =  os.getloadavg()
        return (cpu_load_1, cpu_load_5, cpu_load_15)

    def _get_cpu_count(self):
        try:
            cpu_count = os.sysconf('SC_NPROCESSORS_ONLN')
        except:
            cpu_count = 0
        return cpu_count

    def _get_cpu_times(self):
        f = open("/proc/stat","r")
        for f_line in f:
            break
        f.close()
        f_line = f_line.split(" ")
        values=[]
        for i in f_line:
            if i.isdigit():
                i=float(i)
                values.append(float(i)/CLOCK_TICKS)
        vlen = len(values)
        if vlen >= 8:
            # Linux >= 2.6.11
            user = float(values[0])/CLOCK_TICKS
            nice = float(values[1])/CLOCK_TICKS
            system = float(values[2])/CLOCK_TICKS
            idel = float(values[3])/CLOCK_TICKS
            iowait = float(values[4])/CLOCK_TICKS
            irq = float(values[5])/CLOCK_TICKS
            softirq = float(values[6])/CLOCK_TICKS
            steal = float(values[7])/CLOCK_TICKS
            alltime = sum(values)
            return (user,nice,system,idel,iowait,irq,softirq,steal,alltime)
        if vlen >= 9:
            # Linux >= 2.6.24
            user = float(values[0])/CLOCK_TICKS
            nice = float(values[1])/CLOCK_TICKS
            system = float(values[2])/CLOCK_TICKS
            idel = float(values[3])/CLOCK_TICKS
            iowait = float(values[4])/CLOCK_TICKS
            irq = float(values[5])/CLOCK_TICKS
            softirq = float(values[6])/CLOCK_TICKS
            steal = float(values[7])/CLOCK_TICKS
            guest = float(values[8])/CLOCK_TICKS
            alltime = sum(values)
            return (user,nice,system,idel,iowait,irq,softirq,steal,guest,alltime)
        if vlen >= 10:
            # 3.2.0
            user = float(values[0])/CLOCK_TICKS
            nice = float(values[1])/CLOCK_TICKS
            system = float(values[2])/CLOCK_TICKS
            idel = float(values[3])/CLOCK_TICKS
            iowait = float(values[4])/CLOCK_TICKS
            irq = float(values[5])/CLOCK_TICKS
            softirq = float(values[6])/CLOCK_TICKS
            steal = float(values[7])/CLOCK_TICKS
            guest = float(values[8])/CLOCK_TICKS
            guest_nice = float(values[9])/CLOCK_TICKS
            alltime = sum(values)
            return (user,nice,system,idel,iowait,irq,softirq,steal,guest,guest_nice,alltime)

    def get_cpu_info(self):
        self.info['cpu'] = {}
        self.info['cpu']['cpu_load_1'] = self._get_cpu_load()[0]
        self.info['cpu']['cpu_load_5'] = self._get_cpu_load()[1]
        self.info['cpu']['cpu_load_15'] = self._get_cpu_load()[2]
        self.info['cpu']['cpu_count'] = self._get_cpu_count()
        self.info['cpu']['iowait'] = int(self._get_cpu_times()[4])
        self.info['cpu']['idel'] = int(self._get_cpu_times()[3])

    def get_mem_info(self):
        ORIGINAL_MEMORY = frozenset(('MemTotal', 'SwapTotal', 'MemFree', 'SwapFree'))
        MEMORY = ORIGINAL_MEMORY.union(('Buffers', 'Cached', 'SwapCached'))
        if not os.access("/proc/meminfo", os.R_OK):
            return
        memstats = {}
        for line in get_file_lines("/proc/meminfo"):
            data = line.split(":", 1)
            key = data[0]
            #
            #if key in ORIGINAL_MEMORY:
            #    val = data[1].strip().split(' ')[0]
            #    self.info["%s_mb" % key.lower()] = float(val) // 1024
            if key in MEMORY:
                 val = data[1].strip().split(' ')[0]
                 memstats[key.lower()] = float(val) // 1024


        if None not in (memstats.get('memfree'),memstats.get('buffers'),memstats.get('cached')):
            memstats['real:available'] = memstats['memfree'] + memstats['buffers'] + memstats['cached']

            if None not in (memstats.get('memtotal'),memstats.get('memfree'),memstats.get('buffers'),memstats.get('cached')):
                memstats['real:used'] = memstats.get('memtotal') - memstats['real:available']
            else:
                memstats['real:used'] = 'None'
        else:
            memstats['real:available'] = 'None'

        if None not in (memstats.get('swaptotal'), memstats.get('swapfree')):
            memstats['swap:used'] = memstats['swaptotal'] - memstats['swapfree']

        #if None not in (memstats.get('memtotal'), memstats.get('memfree')):
            #memstats['real:used'] = memstats['memtotal'] - memstats['memfree']
        #if None not in (memstats.get('cached'), memstats.get('memfree'), memstats.get('buffers')):
            #memstats['nocache:free'] = memstats['cached'] + memstats['memfree'] + memstats['buffers']
        #if None not in (memstats.get('memtotal'), memstats.get('nocache:free')):
            #memstats['nocache:used'] = memstats['memtotal'] - memstats['nocache:free']
        #if None not in (memstats.get('swaptotal'), memstats.get('swapfree')):
            #memstats['swap:used'] = memstats['swaptotal'] - memstats['swapfree']

        self.info['memory_mb'] = {
                     #'real' : {
                         'total': memstats.get('memtotal') if (memstats.get('memtotal')) else 0,
                         'used': memstats.get('real:used') if (memstats.get('real:used')) else 0,
                         'free': memstats.get('real:available') if (memstats.get('real:available')) else 0,
                         'use_percent':usage_percent(memstats.get('real:used'),memstats.get('memtotal')),
                         'avail_percent':available_percent(memstats.get('real:available'),memstats.get('memtotal'))
                     }
                     #'nocache' : {
                     #    'free': memstats.get('nocache:free'),
                     #    'used': memstats.get('nocache:used'),
                     #},
                     #'swap' : {
                     #    'total': memstats.get('swaptotal'),
                     #    'free': memstats.get('swapfree'),
                     #    'used': memstats.get('swap:used'),
                     #    'cached': memstats.get('swapcached'),
                     #    'use_percent':usage_percent(memstats.get('swap:used'),memstats.get('swaptotal')),
                     #    'avail_percent':available_percent(memstats.get('swapfree'),memstats.get('swaptotal')),
                     #},
                 #}

    def _get_mount_size(self, mountpoint):
        size_total = None
        size_available = None
        try:
            statvfs_result = os.statvfs(mountpoint)
            size_total = float(statvfs_result.f_frsize *\
statvfs_result.f_blocks)//1024//1024
            size_available =\
float(statvfs_result.f_frsize*(statvfs_result.f_bavail))//1024//1024
        except OSError:
            pass
        return size_total, size_available


    def _mtab_entries(self):
        mtabfile = '/etc/mtab'
        if not os.path.exists(mtabfile):
            mtabfile = '/proc/mounts'
        mtab = get_file_content(mtabfile, '')
        mtab_entries = []
        for line in mtab.splitlines():
            fields = line.split()
            if len(fields) < 4:
                continue
            mtab_entries.append(fields)
        return mtab_entries

    def get_mount_info(self):
        mounts_info = {}
        mtab_entries = self._mtab_entries()

        for fields in mtab_entries:
            device, mount, fstype, options = fields[0], fields[1], fields[2], fields[3]
            if not device.startswith('/') and ':/' not in device:
                continue
            if fstype not in ['ext2','ext3','ext4','xfs']:
                continue
            size_total, size_available = self._get_mount_size(mount)

            mounts_info[mount] = {'mount_point':mount}
            mounts_info[mount] =  {'mount': mount,
                          'device': device,
                          'fstype': fstype,
                          'options': options,
                          'size_total': size_total,
                          'size_available': size_available,
                          'use_percent':usage_percent((size_total-size_available),size_total),
                          'avail_percent':available_percent(size_available,size_total)
                          }
        self.info['mounts'] = mounts_info
        #self.info['mounts']['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #self.info['mounts']['ipaddress'] = get_ip()

    def get_uptime_info(self):
        uptime_file_content = get_file_content('/proc/uptime')
        if uptime_file_content:
            uptime_seconds_string = uptime_file_content.split(' ')[0]
            return int(float(uptime_seconds_string))

    def get_interfaces_info(self):
        interfaces = {}
        for path in glob.glob('/sys/class/net/*'):
            if not os.path.isdir(path) or 'lo' in path:
                continue
            device = os.path.basename(path)
            interfaces[device] = { 'device': device }

            if os.path.exists(os.path.join(path, 'address')):
                macaddress = get_file_content(os.path.join(path, 'address'), default='')
                if macaddress and macaddress != '00:00:00:00:00:00':
                    interfaces[device]['macaddress'] = macaddress

            if os.path.exists(os.path.join(path, 'mtu')):
                interfaces[device]['mtu'] = int(get_file_content(os.path.join(path, 'mtu')))
            if os.path.exists(os.path.join(path, 'operstate')):
                interfaces[device]['active'] = get_file_content(os.path.join(path, 'operstate')) != 'down'
            if os.path.exists(os.path.join(path, 'type')):
                _type = get_file_content(os.path.join(path, 'type'))
                if _type == '1':
                    interfaces[device]['type'] = 'ether'
                elif _type == '512':
                    interfaces[device]['type'] = 'ppp'
                elif _type == '772':
                    interfaces[device]['type'] = 'loopback'
            if os.path.exists(os.path.join(path, 'bridge')):
                interfaces[device]['type'] = 'bridge'
                interfaces[device]['interfaces'] = [ os.path.basename(b) for b in glob.glob(os.path.join(path, 'brif', '*')) ]
                if os.path.exists(os.path.join(path, 'bridge', 'bridge_id')):
                    interfaces[device]['id'] = get_file_content(os.path.join(path, 'bridge', 'bridge_id'), default='')
                if os.path.exists(os.path.join(path, 'bridge', 'stp_state')):
                    interfaces[device]['stp'] = get_file_content(os.path.join(path, 'bridge', 'stp_state')) == '1'
            if os.path.exists(os.path.join(path, 'bonding')):
                interfaces[device]['type'] = 'bonding'
                interfaces[device]['slaves'] = get_file_content(os.path.join(path, 'bonding', 'slaves'), default='').split()
                interfaces[device]['mode'] = get_file_content(os.path.join(path, 'bonding', 'mode'), default='').split()[0]
                interfaces[device]['miimon'] = get_file_content(os.path.join(path, 'bonding', 'miimon'), default='').split()[0]
                interfaces[device]['lacp_rate'] = get_file_content(os.path.join(path, 'bonding', 'lacp_rate'), default='').split()[0]
                primary = get_file_content(os.path.join(path, 'bonding', 'primary'))
                if primary:
                    interfaces[device]['primary'] = primary
                    path = os.path.join(path, 'bonding', 'all_slaves_active')
                    if os.path.exists(path):
                        interfaces[device]['all_slaves_active'] = get_file_content(path) == '1'
            if os.path.exists(os.path.join(path,'device')):
                interfaces[device]['pciid'] = os.path.basename(os.readlink(os.path.join(path,'device')))
            if os.path.exists(os.path.join(path, 'speed')):
                speed = get_file_content(os.path.join(path, 'speed'))
                if speed is not None:
                    interfaces[device]['speed'] = int(speed)

            # Check whether an interface is in promiscuous mode
            if os.path.exists(os.path.join(path,'flags')):
                promisc_mode = False
                # The second byte indicates whether the interface is in promiscuous mode.
                # 1 = promisc
                # 0 = no promisc
                data = int(get_file_content(os.path.join(path, 'flags')),16)
                promisc_mode = (data & 0x0100 > 0)
                interfaces[device]['promisc'] = promisc_mode
            if "bond" in device:
                interfaces[device]['receivembytes'] = self.get_network_flow(device)[0]
                interfaces[device]['transmitmbytes'] = self.get_network_flow(device)[1]
            self.info['interfaces'] = interfaces

class CollectorServices(CollectorBase):
    def __init__(self):
        self.info = {}
        self.get_service_info()
        self._get_check_sysctl()
        self.info['init_soft'] = self._init_install()

    def _compare(self,name):
        return "True" if sysctlt['%s'%name] in get_file_lines(sysctlpath[name]) else  "False"


    def _init_install(self):
        install_list = []
        opt_dir = imsh(cmd='ls /opt')
        ymfly_app_dir = imsh(cmd='ls %s'%APP_PATH)
        try:
            for name in opt_dir:
                if  re.sub('\n','',name) in ['jdk1.8.0_112','nginx','pinpoint-agent','tomcat8.0.21','zabbix-agent']:
                    install_list.append(re.sub('\n','',name))
            for name in ymfly_app_dir:
                if re.sub('\n','',name) in ['autodeploy_agent','ymfly-falcon-agent']:
                    install_list.append(re.sub('\n','',name))
        except:
             pass
        return install_list

    def _chk_service(self,service_list):
        _tmp_dict = {}
        for i in service_list:
            raw = imsh(cmd='ps -ef |grep %s|grep -v grep'%i)
            if raw:
                _tmp_dict['%s'%i] = 'ok'
            else:
                _tmp_dict['%s'%i] = 'no'
        return _tmp_dict


    def get_service_info(self):
        service_list=['chronyd','autodeploy','rsyslog','filebeat','nginx','falcon']
        self.info['services'] = self._chk_service(service_list) 


    def _get_check_sysctl(self):
        self.info['sysctl']={}
        for k in sysctlt.keys():
            self.info['sysctl'][k] = self._compare(k)
        if platform.dist()[1].split('.')[0] > '6':
            self.info['sysctl']['net_core_somaxconn'] = "True" if '65535' in get_file_lines(sysctlpath['net_core_somaxconn']) else 'False'
        if 'False' in self.info['sysctl'].values():
            return 'no'
        else:
            return 'ok'


def _post(url,data):
    url = str(url)
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(req)
    return response.read()

if  __name__ == '__main__':
    a = CollectorBase()
    b = CollectorServices()
    c = dict(a.info,**b.info)
    print json.dumps(c,indent=4)
    
