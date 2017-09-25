Open-source Software-based Portable DoS Test Tool for IoT Devices
====

With the growing interest in devices based on internet-of-things (IoT), the vulnerability of IoT has been clarified. 
In this study, we constructed a portable denial of service (DoS) test tool based on the malware *Mirai* and conducted a DoS test on several IoT devices. 
The tool can visualize the load and adjust the volume of the attack packet. 
These functionalities enable visual checks of the state of a DoS attack. 
We can also change the attack method and performance in different target devices. 
By applying the tool, we can check the vulnerability of an IoT device and understand the state of the actual DoS attack. 

## Description
It is the portable DoS tool monitor.

## Demo

## VS. 

## Requirement

## Usage

## Install

### elasticsearchInstall 
```docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
docker run --rm -it -p 9200:9200 --name elasticsearch -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e    "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
```

起動   
```docker ps -a   
docker start 4aa6da0ada4f # Process ID  
docker stop 4aa6da0ada4f  
``` 

### kibana Install 
https版 https://github.com/ertlnagoya/kibana.git   
```git clone git@github.com:ertlnagoya/kibana.git # ssh  
git checkout dev    
nvm install $(cat .node-version) # for nodejs version  
npm install # for node module 
```

```   
npm start # development mode  
```



## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[tcnksm](https://github.com/tcnksm)

# portable-DoS-tool-monitor
