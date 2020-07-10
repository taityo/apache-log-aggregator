import argparse as ap
import pandas as pd

from src.aggregate import TimeAccessAggregator, RemoteHostAccessAggregator
from src.log import ApatchLogDataFormatter

if __name__ == "__main__":
    
    # コマンドを定義
    parser = ap.ArgumentParser(description="Webサーバのアクセスログを集計するCLI")
    parser.add_argument("agg", help="集計方法をしている。timeかhostを指定する事ができる")
    parser.add_argument("-f", "--file", type=lambda x:x.split(","), help="集計するファイルを指定する")
    parser.add_argument("-t", "--term", type=lambda x:x.split(":"), help="集計した期間を指定する")
    
    # 引数の解析と読み込み
    args = parser.parse_args()
    agg = args.agg
    filenames = args.file
    term = args.term
    
    # 集計オブジェクトを作成
    if agg == "time":
        aggregator = TimeAccessAggregator()
    elif agg == "host":
        aggregator = RemoteHostAccessAggregator()
    else:
        exit()

    # ファイルを読み込み、集計
    for fn in filenames:
        # ファイルリーダーを作成
        reader = pd.read_table(fn, chunksize=50)

        for lines in reader:
            # pandasのDataFrameを文字列のlistに変換
            lines = [str(s[0]).strip() for s in lines.values]
            
            # ログデータをLogData型に変換
            data_formatter = ApatchLogDataFormatter()
            logs = data_formatter.get_log_data(lines)
          
            # 集計したい期間を指定 
            if term is not None:
                aggregator.set_term(term[0], term[1])
                
            # ログデータから集計
            aggregator.aggregate(logs)
    
    # 集計結果を出力
    result = aggregator.get_result()
    if args.agg == "time":
        print("Time      \tAccessCount")
    elif args.agg == "host":
        print("RemoteHost\tAccessCount")
    for key in result.keys():
        print(f"{key}\t{result[key]}")