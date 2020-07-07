import os
from db import db

ipv4_list = os.popen('ip addr show').read().split("inet ")[1:]
ipv4_list = [ipv4.split("/")[0] for ipv4 in ipv4_list]
ipv4_list = [ipv4 for ipv4 in ipv4_list if ipv4 != "127.0.0.1"]

LOCAL_IP_ADDR = ipv4_list[0]

def select_table(table):
    table = table or "__default__"
    return db.table(table)

def get_db():
    return db

def get_at(l, index, default):
    print(l, index, l[index:])
    return (l[index:]+[default])[0]