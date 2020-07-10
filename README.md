# Apache Log Aggregator

これはApacheのアクセスログを集計するCLIです。

## Installation
### pipenv 
```
git clone https://github.com/taityo/fixpoint-coding-test.git

pipenv install
```

### pip
```
git clone https://github.com/taityo/fixpoint-coding-test.git

pip install -r requirements.txt
```

## Usage
```
python agg.py [time/host] [-f FILE] [-t TERM]
```

## Example
時間ごとにアクセス件数を集計する
```
python agg.py time -f log/access_log
```

リモートホストごとにアクセス件数を集計する
```
python agg.py host -f log/access_log
```

複数ファイルを集計する場合は、コンマ(,)で区切る
```
python agg.py time -f log/access_log,log/access_log2
```

期間を指定して集計する
```
python agg.py time -f log/access_log -t 2020/03/03:2020/05/02
```
