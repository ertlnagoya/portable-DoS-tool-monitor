Open-source Software-based Portable DoS Test Tool for IoT Devices
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

## Requirement

## Usage

## Install

### Elasticsearch Install 
Elasticsearch https://www.elastic.co/jp/products/elasticsearch
```docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
docker run --rm -it -p 9200:9200 --name elasticsearch -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e    "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
```

### Elasticsearch Start
```
docker ps -a   
docker start 4aa6da0ada4f # Process ID  
docker stop 4aa6da0ada4f  
``` 

### kibana Install 
kibana https://www.elastic.co/jp/products/kibana    
     
https: https://github.com/ertlnagoya/kibana.git   
```
git clone git@github.com:ertlnagoya/kibana.git # ssh  
git checkout dev    
nvm install $(cat .node-version) # for nodejs version  
npm install # for node module 
```

### kibana Start
```   
npm start # development mode  
```



## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[tcnksm](https://github.com/tcnksm)

# portable-DoS-tool-monitor
