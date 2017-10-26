Open-source Software-based Portable DoS Test Tool for IoT Devices -Monitor-    
====
This DoS tool consists of the _monitor_ and _the attacker_.     
The portable DoS tool monitor is instructs the attack and visualizes the load.   
The attacker tool is available [here](https://github.com/ertlnagoya/portable-DoS-tool-attacker).    
    
<img width="350" alt="2017-09-25 10 22 39" src="https://user-images.githubusercontent.com/26764885/30840032-02bdea00-a2b0-11e7-82ee-2e580704a730.png">    

## Description
 ### What is "Open-source Software-based Portable DoS Test Tool for IoT Device?"
 We implemented a portable denial of service (DoS) test tool based on the *Mirai* malware and conducted a DoS test on several IoT devices. 
 The tool visualizes the load, and adjusts the volume of the attack packet manually. 
 These functionalities enable visual checks of the state of a DoS attack. 
 We can also change the attack method and its performance in different target devices. 
 By applying the tool, we can check the vulnerability of an IoT device and understand the state of the actual DoS attack.
 
 
 
## Demo
![image](https://user-images.githubusercontent.com/26764885/30792330-5ac7b3a0-a1f4-11e7-85fa-6db92e2ff4c1.png)
## VS. 
The embedded board offers the following three advantages:     
1. the resources of the monitor PC need not be devoted to stress testing,     
2. the compact size saves power and is suitable for carrying,    
3. the embedded board can be inexpensively scaled.     
<img width="659" alt="2017-09-25 10 22 39" src="https://user-images.githubusercontent.com/26764885/30792602-a87c3b32-a1f6-11e7-8560-b4e1e6c65385.png">     

## Requirement
- macOS Sierra v.10.12.6
     - python 2.7
     - docker 17.06.2-ce-mac27
     - nvm
     - npm    
## Usage
### To start Elasticsearch
```
docker ps -a   
docker start [Process ID]  
``` 
### To stop Elasticsearch    
```    
docker stop [Process ID]    
``` 
### To start Kibana
```   
cd kibana
npm start # development mode  
```
### To start Monitor program    
```
### Terminal 1    
python correct_time_server.py   
### Terminal 2    
python recieve_packet_stats.py    
### Terminal 3    
python webcam_server.py 
### Terminal 4    
python ping_server.py
```
### To instruct attack     
```
telnet [attacker IP address]
```
```
[+] This is the Portable DoS Test Tool.
[+] Command is here.
[+] attack:[type target(s) time flags]
[+] (If you use ? in attack command, you can check help.
     Ex:[?],[udp ?],[udp 1.1.1.1 ?])
[+] exit:[exit],[quit]
[+] botcount:[botcount]
root@botnet# ?
Available attack list
ack: ACK flood
greip: GRE IP flood
greeth: GRE Ethernet flood
udpplain: UDP flood with less options. optimized for higher PPS
http: HTTP flood
udp: UDP flood
vse: Valve source engine specific flood
syn: SYN flood

root@botnet# udp ?
Comma delimited list of target prefixes
Ex: 192.168.0.1
Ex: 10.0.0.0/8
Ex: 8.8.8.8,127.0.0.0/29

root@botnet# udp 192.168.0.1 ?
Duration of the attack, in seconds
```
Up to three duplicate attacks are possible    

## Installation    
### Elasticsearch Install
[Elasticsearch](https://www.elastic.co/jp/products/elasticsearch)     
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
docker run --rm -it -p 9200:9200 --name elasticsearch -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e    "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
```

### Kibana Install 
[kibana](https://www.elastic.co/jp/products/kibana)    
     
[https download](https://github.com/ertlnagoya/kibana.git)            
```
git clone git@github.com:ertlnagoya/kibana.git    
git checkout dev    
nvm install $(cat .node-version) # for nodejs version  
npm install # for node module 
```
### Monitor program Install
```
git clone git@github.com:ertlnagoya/portable-DoS-tool-monitor.git
```
## Licence
[Apache License 2.0](https://github.com/ertlnagoya/portable-DoS-tool-monitor/blob/master/LICENSE)
## Author
* [K-atc](https://github.com/K-atc)    
* [NGR](https://github.com/KeigoNagara)    
* [Yutaka Matsubara](https://github.com/YutakaMatsubara)    

