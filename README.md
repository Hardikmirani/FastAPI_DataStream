# FastAPI_DataStream
Using Kafka services APIs will provide live streaming data.

## Description 
Using the Kafka services . I made APIs to consume the data and helps to visualize the data in a good manner.


## Authors

- [@Hardikmirani](https://github.com/Hardikmirani)


## Run Locally

Clone the project

```bash
    git clone https://github.com/Hardikmirani/FastAPI_DataStream.git
```

Go to the project directory

```bash
    cd FastAPI_DataStream
```



Visit This Site to download Kafka & ZooKeeper SetUp

```bash
    https://kafka.apache.org/downloads
```


Make Virtual environment and Activate

```bash
    Virtualenv envfapi
``` 

```bash
    Source activate
```

Install Required Modules by using this command

```bash
    pip install -r requirements.txt
```

Start Server of ZooKeeper and Kafka from Setup file location

```bash
    bin/zookeeper-server-start.sh config/zookeeper.properties
```
```bash
    bin/kafka-server-start.sh config/server.properties
```
First run your Producer and after that use this code to run Main file 
```bash
    uvicorn main:app --reload 
```

## 🚀 About Me
I'm a Python Developer and enthusiastic for Data Science


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hardik-mirani)
[![kaggle](https://img.shields.io/badge/Kaggle-1DA1F1?style=for-the-badge&logo=kaggle&logoColor=white)](https://twitter.com/)