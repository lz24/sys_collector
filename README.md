# sys_collector

___
{
    "memory_mb": {
        "avail_percent": 88.41382950646609, 
        "total": 3789.0, 
        "use_percent": 11.586170493533913, 
        "free": 3350.0, 
        "used": 439.0
    }, 
    "sys": {
        "kernel": "3.10.0-1160.el7.x86_64", 
        "app_jmx": [
            {
                "test.ymfly.com": "no_java_pid"
            }
        ], 
        "dist": "centos7.9.2009", 
        "uptime_seconds": 14120, 
        "python": "2.7.5", 
        "arch": "x86_64", 
        "glibc": "2.2.5", 
        "hostname": "localhost.localdomain", 
        "datetime": "2020-12-07 15:26:24", 
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
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/go/bin:/root/bin", 
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
            "use_percent": 14.752365052865887, 
            "avail_percent": 85.24763494713412, 
            "size_total": 17970.0, 
            "size_available": 15319.0, 
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
            "macaddress": "02:42:1d:c6:3e:68", 
            "net_flow": [
                {
                    "docker0:": {
                        "ReceiveFrames": 0, 
                        "TransmitErrs": 0, 
                        "ReceiveDrop": 0, 
                        "ReceiveBytes": 0, 
                        "TransmitCompressed": 0, 
                        "TransmitFrames": 0, 
                        "ReceiveMulticast": 0, 
                        "ReceivePackets": 0, 
                        "ReceiveCompressed": 0, 
                        "TransmitFifo": 0, 
                        "TransmitPackets": 0, 
                        "device": "docker0:", 
                        "TransmitBytes": 0, 
                        "TransmitMulticast": 0, 
                        "ReceiveErrs": 0, 
                        "TransmitDrop": 0, 
                        "ReceiveFifo": 0
                    }
                }
            ], 
            "interfaces": [], 
            "mtu": 1500, 
            "active": false, 
            "promisc": false, 
            "stp": false, 
            "device": "docker0", 
            "type": "bridge", 
            "id": "8000.02421dc63e68"
        }, 
        "enp0s3": {
            "macaddress": "08:00:27:c0:39:58", 
            "net_flow": [
                {
                    "enp0s3:": {
                        "ReceiveFrames": 0, 
                        "TransmitErrs": 0, 
                        "ReceiveDrop": 0, 
                        "ReceiveBytes": 231756561, 
                        "TransmitCompressed": 0, 
                        "TransmitFrames": 0, 
                        "ReceiveMulticast": 462, 
                        "ReceivePackets": 196997, 
                        "ReceiveCompressed": 0, 
                        "TransmitFifo": 0, 
                        "TransmitPackets": 62521, 
                        "device": "enp0s3:", 
                        "TransmitBytes": 5997484, 
                        "TransmitMulticast": 0, 
                        "ReceiveErrs": 0, 
                        "TransmitDrop": 0, 
                        "ReceiveFifo": 0
                    }
                }
            ], 
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
            "net_flow": [
                {
                    "enp0s8:": {
                        "ReceiveFrames": 0, 
                        "TransmitErrs": 0, 
                        "ReceiveDrop": 0, 
                        "ReceiveBytes": 43853, 
                        "TransmitCompressed": 0, 
                        "TransmitFrames": 0, 
                        "ReceiveMulticast": 0, 
                        "ReceivePackets": 145, 
                        "ReceiveCompressed": 0, 
                        "TransmitFifo": 0, 
                        "TransmitPackets": 119, 
                        "device": "enp0s8:", 
                        "TransmitBytes": 22610, 
                        "TransmitMulticast": 0, 
                        "ReceiveErrs": 0, 
                        "TransmitDrop": 0, 
                        "ReceiveFifo": 0
                    }
                }
            ], 
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
        "idel": 139, 
        "cpu_load_1": 0.0, 
        "cpu_load_15": 0.05, 
        "cpu_load_5": 0.01, 
        "iowait": 0, 
        "cpu_count": 1
    }
}

