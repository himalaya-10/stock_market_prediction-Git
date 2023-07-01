
output_directory='/Users/himalayagahlot/Desktop/stock market prediction/app.py'



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
    code=f'''

model{name}=pickle.load(open('pickle/{name}.pkl','rb'))


@app.route('/stocks/{name}.html',methods=['GET'])
def {name}():
    return render_template('/stocks/{name}.html')
@app.route('/c{name}',methods=['POST'])
def p{name}():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model{name}.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/c{name}.html',p{name}='{{}}'.format(output))
'''
    with open(output_directory, 'a') as f:  
        f.write(code)