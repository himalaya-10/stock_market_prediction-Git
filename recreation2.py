output_directory='/Users/himalayagahlot/Desktop/stock market prediction/templates/close/'
stocklist={
    # 'ADANIPORTS',
'ASIANPAINT',
'AXISBANK',
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
'HDFCBANK',
'HEROMOTOCO',
'HINDALCO',
'HINDUNIL',
'ICICIBANK',
'INDUSIND BANK',
'INFRATEL',
'INFY',
'IOC',
'ITC',
'JSWSTEEL',
'KOTAKBANK',
'LT',
'MARUTI',
'MM',
'NESTLEIND',
'NIFTY50',
'NTPC',
'ONGC',
'POWERGRID',
'RELIANCE',
'SBIN',
'SHREECEMENT',
'SUNPHARMA',
'TATAMOTORS',
'TATASTEEL',
'TCS',
'TECHM',
'TITAN',
'ULTRATECHCEMENT',
'UPL',
'VEDL',
'WIPRO',
'ZEEL'}


for name in stocklist:
    file_name = f'c{name}.html'
    code=f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>closing price </title>
    <link rel="stylesheet" href="static/2.css">
    <link rel="stylesheet" href="/static/2.css">
</head>
<div id="blob"></div>
<body>
    <div class="p">Prediction</div>
    <div class="close">Trading will Close at</div>
    <div class="prediction_text">{{p{name}}}</div>
    <div class="back"><a href="/">Back to Home Page</a></div>

</body>
<script src="/static/1.js"></script>
</html>
    '''

    with open(output_directory + file_name, 'w') as f:
        f.write(code)