Open-source Software-based Portable DoS Test Tool for IoT Devices    
Monitor
====
The portable DoS tool monitor is instructs the attack and visualizes the load.    
## Description
We constructed a portable denial of service (DoS) test tool based on the malware *Mirai* and conducted a DoS test on several IoT devices. 
The tool can visualize the load and adjust the volume of the attack packet. 
These functionalities enable visual checks of the state of a DoS attack. 
We can also change the attack method and performance in different target devices. 
By applying the tool, we can check the vulnerability of an IoT device and understand the state of the actual DoS attack. 
## Demo
![image](https://user-images.githubusercontent.com/26764885/30792330-5ac7b3a0-a1f4-11e7-85fa-6db92e2ff4c1.png)
TODO
## VS. 
TODO    
<img width="659" alt="2017-09-25 10 22 39" src="https://user-images.githubusercontent.com/26764885/30792602-a87c3b32-a1f6-11e7-8560-b4e1e6c65385.png">
## Requirement
- macOS Sierra v.10.12.6
     - python 2.7
     - docker 17.06.2-ce-mac27
     - nvm
     - npm    
## Usage
### Elasticsearch Start
```
docker ps -a   
docker start [Process ID]  
``` 
### Elasticsearch Stop    
```    
docker stop [Process ID]    
``` 
### Kibana Start
```   
cd kibana
npm start # development mode  
```
### Monitor program Start    
```
python correct_time_server.py    
python recieve_packet_stats.py    
python webcam_server.py 
python ping_server.py
```
## Install    
### Elasticsearch Install 
Elasticsearch https://www.elastic.co/jp/products/elasticsearch
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
docker run --rm -it -p 9200:9200 --name elasticsearch -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e    "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
```

### Kibana Install 
kibana https://www.elastic.co/jp/products/kibana    
     
https: https://github.com/ertlnagoya/kibana.git   
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
## Contribution
TODO
## Licence
[MIT](https://github.com/ertlnagoya/portable-DoS-tool-monitor/blob/master/LICENSE）
## Author
TODO
[tcnksm](https://github.com/tcnksm)
