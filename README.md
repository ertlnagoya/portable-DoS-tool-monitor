# portable-DoS-tool-monitor

## kibana導入   
https版 https://github.com/ertlnagoya/kibana.git   
----
```git clone git@github.com:ertlnagoya/kibana.git # ssh版推奨   
git checkout dev # 開発はdevブランチでしている   
nvm install $(cat .node-version) # nodejs のバージョンを開発者の間で合わせるため   
npm install # nodeモジュールの依存関係を解決   ```

----
```npm start # development mode での起動   ```

## elasticsearch導入   
----
```docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0   
docker run --rm -it -p 9200:9200 --name elasticsearch -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.3.0   ```

起動   
----
```docker ps -a   
docker start 4aa6da0ada4f # Process ID  
docker stop 4aa6da0ada4f  ``` 
