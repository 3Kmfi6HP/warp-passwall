import csv
import hashlib
import random

# 读取 result.csv 文件
with open('result.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter='\t')
  # 跳过表头
  next(reader)
  # 读取前 10 行数据
  rows = [row for _, row in zip(range(100), reader)]

# 解析 IP 地址和端口号
ips_and_ports = [row[0].split(':') for row in rows]

# 生成随机 md5 哈希值
hashes = [
  hashlib.md5(str(random.random()).encode()).hexdigest() for _ in ips_and_ports
]

# 生成配置文件
config = ""
for i, (ip, port) in enumerate(ips_and_ports):
  print(i)
  port = port.split(",")[0]
  config += f"config nodes '{hashes[i]}'\n"
  config += "\toption protocol 'wireguard'\n"
  config += "\toption wireguard_mtu '1280'\n"
  config += "\toption wireguard_secret_key '2FjQ/hjZVg7pgG13QiTW7JebLJuntYCQ0poCehCQ9G4='\n"
  config += "\toption type 'Xray'\n"
  config += "\toption wireguard_public_key 'bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo='\n"
  config += "\toption wireguard_keepAlive '0'\n"
  config += "\tlist wireguard_local_address '172.16.0.2/32'\n"
  config += "\toption add_mode '1'\n"
  config += f"\toption address '{ip}'\n"
  config += f"\toption port '{port}'\n"
  config += f"\toption remarks 'WARP{i+5}'\n\n"

# 将配置文件写入文件
with open('out.txt', 'w') as f:
  f.write(config)

# 生成随机 md5 哈希值的配置文件

md5_config = f"config nodes '0fa449b6e27a4465a0259005ccc0548d'\n"
md5_config += "\toption remarks 'WARP 负载均衡'\n"
md5_config += "\toption type 'Xray'\n"
md5_config += "\toption protocol '_balancing'\n"
for i, (ip, port) in enumerate(ips_and_ports):
  print(i)
  md5_config += f"\tlist balancing_node '{hashes[i]}'\n"
md5_config += "\toption domainStrategy 'IPIfNonMatch'\n"
md5_config += "\toption domainMatcher 'hybrid'\n"

# 将随机 md5 哈希值的配置文件写入文件
with open('out2.txt', 'w') as f:
  f.write(md5_config)
