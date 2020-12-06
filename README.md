# sys_collector

___
{
    "memory_mb": {
        "avail_percent": 87.27896542623384, 
        "total": 3789.0, 
        "use_percent": 12.721034573766165, 
        "free": 3307.0, 
        "used": 482.0
    }, 
    "sys": {
        "kernel": "3.10.0-1160.el7.x86_64", 
        "app_jmx": [
            {
                "test.ymfly.com": "no_java_pid"
            }
        ], 
        "dist": "centos7.9.2009", 
        "uptime_seconds": 27656, 
        "python": "2.7.5", 
        "arch": "x86_64", 
        "glibc": "2.2.5", 
        "hostname": "localhost.localdomain", 
        "datetime": "2020-12-06 22:47:22", 
        "dns": "192.168.1.1", 
        "ipaddress": "192.168.1.248", 
        "app": [
            "test.ymfly.com"
        ]
    }, 
    "services": {
        "filebeat": "no", 
        "chronyd": "no", 
        "autodeploy": "no", 
        "nginx": "no", 
        "rsyslog": "ok", 
        "falcon": "no"
    }, 
    "env": {
        "LANG": "zh_CN.UTF-8", 
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin", 
        "HISTSIZE": "1000"
    }, 
    "mounts": {
        "/boot": {
            "use_percent": 14.792899408284024, 
            "avail_percent": 85.20710059171599, 
            "size_total": 1014.0, 
            "size_available": 864.0, 
            "device": "/dev/sda1", 
            "mount": "/boot", 
            "options": "rw,seclabel,relatime,attr2,inode64,noquota", 
            "fstype": "xfs"
        }, 
        "/": {
            "use_percent": 11.274346132442961, 
            "avail_percent": 88.72565386755704, 
            "size_total": 17970.0, 
            "size_available": 15944.0, 
            "device": "/dev/mapper/centos-root", 
            "mount": "/", 
            "options": "rw,seclabel,relatime,attr2,inode64,noquota", 
            "fstype": "xfs"
        }
    }, 
    "sysctl": {
        "net_ipv4_tcp_rmem": "False", 
        "vm_swappiness": "False", 
        "net_ipv4_tcp_fin_timeout": "False", 
        "net_core_rmem_default": "False", 
        "net_ipv4_tcp_wmem": "False", 
        "net_ipv4_tcp_syncookies": "True", 
        "fs_inotify_max_user_instances": "False", 
        "net_ipv4_tcp_ecn": "False", 
        "net_ipv4_conf_all_arp_ignore": "False", 
        "net_ipv4_tcp_mem": "False", 
        "vm_drop_caches": "False", 
        "net_core_wmem_max": "False", 
        "net_ipv4_tcp_max_tw_buckets": "False", 
        "net_core_rmem_max": "False", 
        "net_ipv4_tcp_tw_reuse": "False", 
        "net_ipv4_tcp_retries2": "False", 
        "net_ipv4_tcp_keepalive_time": "False", 
        "net_ipv4_ip_local_port_range": "False", 
        "net_ipv4_tcp_timestamps": "False", 
        "net_ipv4_tcp_max_orphans": "False", 
        "net_core_somaxconn": "False", 
        "net_ipv4_tcp_tw_recycle": "False", 
        "net_ipv4_ip_nonlocal_bind": "False", 
        "net_ipv4_tcp_max_syn_backlog": "False", 
        "net_ipv4_tcp_synack_retries": "False", 
        "net_ipv4_ip_forward": "True", 
        "net_core_wmem_default": "False", 
        "net_ipv4_conf_all_arp_announce": "False", 
        "net_ipv4_conf_default_rp_filter": "False", 
        "net_core_netdev_max_backlog": "False"
    }, 
    "interfaces": {
        "docker0": {
            "macaddress": "02:42:7f:55:09:f7", 
            "interfaces": [], 
            "mtu": 1500, 
            "active": false, 
            "promisc": false, 
            "stp": false, 
            "device": "docker0", 
            "type": "bridge", 
            "id": "8000.02427f5509f7"
        }, 
        "enp0s3": {
            "macaddress": "08:00:27:c0:39:58", 
            "speed": 1000, 
            "pciid": "0000:00:03.0", 
            "mtu": 1500, 
            "active": true, 
            "promisc": false, 
            "device": "enp0s3", 
            "type": "ether"
        }, 
        "enp0s8": {
            "macaddress": "08:00:27:fa:32:32", 
            "speed": 1000, 
            "pciid": "0000:00:08.0", 
            "mtu": 1500, 
            "active": true, 
            "promisc": false, 
            "device": "enp0s8", 
            "type": "ether"
        }
    }, 
    "init_soft": [], 
    "cpu": {
        "idel": 273, 
        "cpu_load_1": 0.0, 
        "cpu_load_15": 0.05, 
        "cpu_load_5": 0.01, 
        "iowait": 0, 
        "cpu_count": 1
    }
}

