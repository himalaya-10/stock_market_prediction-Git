# template_file='template/stocks/ADANIPORTS.html'
output_directory='/Users/himalayagahlot/Desktop/stock market prediction/templates/stocks/'
# textfile='/Users/himalayagahlot/Desktop/stock market prediction/namefile.txt'


# with open(template_file','r') as f:
#     template_content=f.read()

# print(textfile)


# for name in textfile:
#     print(name)


stocklist={
    # 'ADANIPORTS',
'ASIAN PAINT',
'AXIS BANK',
'BAJAJ-AUTO',
'BAJAJFINSV',
'BAJAJFINANCE',
'BHARTIART',
'BPCL',
'BRITANNIA',
'CIPLA',
'COALINDIA',
'DRREDDY',
'EICHERMOT',
'GAIL',
'GRASIM',
'HCLTECH',
'HDFC',
'HDFC BANK',
'HERO MOTOCO',
'HINDALCO',
'HINDUNIL',
'ICICI BANK',
'INDUSIND BANK',
'INFRATEL',
'INFY',
'IOC',
'ITC',
'JSWSTEEL',
'KOTAK BANK',
'LT',
'MARUTI',
'MM',
'NESTLE IND',
'NIFTY50',
'NTPC',
'ONGC',
'POWER GRID',
'RELIANCE',
'SBIN',
'SHREE CEMENT',
'SUNPHARMA',
'TATA MOTORS',
'TATA STEEL',
'TCS',
'TECHM',
'TITAN',
'ULTRATECH CEMENT',
'UPL',
'VEDL',
'WIPRO',
'ZEEL'}


for name in stocklist:
    file_name = f'{name}.html'
    code=f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adaniports</title>
    <link rel="stylesheet" href="static/1.css">
    <link rel="stylesheet" href="/static/1.css">

</head>
<div id="blob"></div>
<body>
    <div class="title">{name}</div>
    <form Id="form" action="/c{name}" method="post" class="form" >
        
        <div class="input">
            <input type="text" class="inp" id="prevclose" name="prevclose" placeholder="Prev close" required>
            <input type="text" class="inp" id="open" name="open" placeholder="Open" required>
            <input type="text" class="inp" id="high" name="high" placeholder="High" required>
            <input type="text" class="inp" id="low" name="low" placeholder="Low" required>
            <input type="text" class="inp" id="last" name="last" placeholder="Last Traded Price" required>
            <input type="text" class="inp" id="VWAP" name="VWAP" placeholder="VWAP" required>
        </div>
    <button id="submit">Submit</button>
    </form>
    <div class="featurebox">
        <div class="feature">Prev Close (Previous Close): Prev Close refers to the closing price of a financial instrument (such as a stock or cryptocurrency) on the previous trading day. It is the last price at which the instrument traded before the market closed.</div>
        <div class="feature">Open: Open refers to the price at which a financial instrument starts trading at the beginning of a new trading session or trading day. It is the first price at which the instrument is traded when the market opens.</div>
        <div class="feature">High: High represents the highest price that a financial instrument reaches during a specific trading period, such as a day, week, month, or a specific time interval. It shows the highest point that buyers were willing to pay for the instrument during that period.</div>
        <div class="feature">Low: Low refers to the lowest price that a financial instrument reaches during a specific trading period. It represents the lowest point that sellers were willing to accept for the instrument during that period.</div>
        <div class="feature">Last Traded Price: Last refers to the most recent price at which a financial instrument traded. It is the price at which the instrument was last bought or sold in the market.</div>
        <div class="feature">VWAP (Volume Weighted Average Price): VWAP is a trading indicator that calculates the average price at which a financial instrument has traded throughout a specific period, weighted by the trading volume at each price level. It provides insights into the average price at which traders have bought or sold the instrument relative to the trading volume.</div>
    </div>
    <footer>By Himalaya Gahlot</footer>
    <script src="/static/1.js"></script>
    
   
</body>
</html>
</body>
</html>
    '''
    with open(output_directory + file_name, 'w') as f:
        f.write(code)

