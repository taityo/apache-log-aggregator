# Apache Log Aggregator

これはApacheのアクセスログを集計するCLIです。

## Installation
### pipenv 
```
$ git clone https://github.com/taityo/apache-log-aggregator.git
$ cd ~/apache-log-aggregator/
$ pipenv install
```

### pip
```
$ git clone https://github.com/taityo/apache-log-aggregator.git
$ cd ~/apache-log-aggregator/
$ pip install -r requirements.txt
```

## Usage
```
$ python agg.py -h
usage: agg.py [-h] [-f FILE] [-t TERM] [time/host]

Webサーバのアクセスログを集計するCLI

positional arguments:
  [time/host]           集計方法を指定する。timeかhostを指定する事ができる

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  集計するファイルを指定する
  -t TERM, --term TERM  集計した期間を指定する
```

## Example
時間ごとにアクセス件数を集計する
```
$ python agg.py time -f log/access_log
Time            AccessCount
2005/04/18 00:10:47     9
2007/04/18 00:10:47     9
2005/04/18 00:10:30     6
2005/04/18 00:10:50     5
2006/04/18 00:10:30     5
2005/04/18 00:10:49     4
...
```

リモートホストごとにアクセス件数を集計する
```
$ python agg.py host -f log/access_log
RemoteHost      AccessCount
10.2.3.7        30
10.2.3.6        10
10.2.3.4        9
10.2.3.5        8
10.2.3.8        3
...
```

複数ファイルを集計する場合は、コンマ(,)で区切る  
ファイルは2つ以上指定する事も可能  
```
$ python agg.py time -f log/access_log,log/access_log2
```

期間を指定する場合は、コロン(:)で区切る  
始まりの日付と終わりの日付のみを指定できる  
```
$ python agg.py time -f log/access_log -t 2020/03/03:2020/05/02
```
