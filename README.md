#密码
导入请求
进口CSV
导入时间
从日期时间导入日期时间

类：
定义文件__初始化__（自我，市场名称，间隔=5）
市场名称=市场名称
自间隔=间隔

    定义取序簿（自身）：
    url = f“https://api.upbit.com/v1/orderbook?markets={self.market_name}”
    响应=requests.get（网址）
    Json表示的是:[0]
    退货订单_预订_数据

    自身，订单书数据，文件名：
    打开（文件名，‘w’，换行符=“）作为csvfile：
    字段名=【价格、数量、类型、时间戳】
    writer=csvDictWriter（csvfile，字段名=字段名）
            
    写头文件（）
    以order_book_data【'order_book_units'】形式投标者：
    价格：出价，数量：出价，类型：出价，时间戳：时间（））
    对于order_book_data【'orderbook_units'】中的查询:
    价格：要价，数量：要价，类型：要价，时间戳：time.time（）}

    def运行（自身）：
    而真实：
    order_book_data=自取order_book
    文件名=f"book-{datetime.now().strftime('%Y-%m-%d')}-upbit-{self.market_name}.csv"
    save_order_book（order_book_data，文件名）
    打印“订单簿数据保存到{文件名}”）
    睡眠时间（自我间隔）

#用法示例：
如果__姓名__ == “主要":
收集器=UpbitOrderBookCollector（市场名称=KRW-BTC，间隔=5）
收集器.运行

