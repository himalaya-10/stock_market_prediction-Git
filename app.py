from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
modelADANIPORTS=pickle.load(open('pickle/ADANIPORTS.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
# @app.route('/stocks/ADANIPORTS.html',methods=['GET'])
# def adaniports():
#     return render_template('/stocks/ADANIPORTS.html')
# @app.route('/cADANIPORTS',methods=['POST'])
# def predict():
#     int_features=[float(x) for x in request.form.values()]
#     features=[np.array(int_features)]
#     prediction=modelADANIPORTS.predict(features)
#     output=round(prediction[0],2)
#     return render_template('/close/cADANIPORTS.html',pADANIPORTS='{}'.format(output))





modelHEROMOTOCO=pickle.load(open('pickle/HEROMOTOCO.pkl','rb'))


@app.route('/stocks/HEROMOTOCO.html',methods=['GET'])
def HEROMOTOCO():
    return render_template('/stocks/HEROMOTOCO.html')
@app.route('/cHEROMOTOCO',methods=['POST'])
def pHEROMOTOCO():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHEROMOTOCO.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHEROMOTOCO.html',pHEROMOTOCO='{}'.format(output))


modelBPCL=pickle.load(open('pickle/BPCL.pkl','rb'))


@app.route('/stocks/BPCL.html',methods=['GET'])
def BPCL():
    return render_template('/stocks/BPCL.html')
@app.route('/cBPCL',methods=['POST'])
def pBPCL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBPCL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBPCL.html',pBPCL='{}'.format(output))


modelSHREECEMENT=pickle.load(open('pickle/SHREECEMENT.pkl','rb'))


@app.route('/stocks/SHREECEMENT.html',methods=['GET'])
def SHREECEMENT():
    return render_template('/stocks/SHREECEMENT.html')
@app.route('/cSHREECEMENT',methods=['POST'])
def pSHREECEMENT():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelSHREECEMENT.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cSHREECEMENT.html',pSHREECEMENT='{}'.format(output))


modelHINDALCO=pickle.load(open('pickle/HINDALCO.pkl','rb'))


@app.route('/stocks/HINDALCO.html',methods=['GET'])
def HINDALCO():
    return render_template('/stocks/HINDALCO.html')
@app.route('/cHINDALCO',methods=['POST'])
def pHINDALCO():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHINDALCO.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHINDALCO.html',pHINDALCO='{}'.format(output))


modelHINDUNIL=pickle.load(open('pickle/HINDUNIL.pkl','rb'))


@app.route('/stocks/HINDUNIL.html',methods=['GET'])
def HINDUNIL():
    return render_template('/stocks/HINDUNIL.html')
@app.route('/cHINDUNIL',methods=['POST'])
def pHINDUNIL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHINDUNIL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHINDUNIL.html',pHINDUNIL='{}'.format(output))


modelONGC=pickle.load(open('pickle/ONGC.pkl','rb'))


@app.route('/stocks/ONGC.html',methods=['GET'])
def ONGC():
    return render_template('/stocks/ONGC.html')
@app.route('/cONGC',methods=['POST'])
def pONGC():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelONGC.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cONGC.html',pONGC='{}'.format(output))


modelGRASIM=pickle.load(open('pickle/GRASIM.pkl','rb'))


@app.route('/stocks/GRASIM.html',methods=['GET'])
def GRASIM():
    return render_template('/stocks/GRASIM.html')
@app.route('/cGRASIM',methods=['POST'])
def pGRASIM():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelGRASIM.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cGRASIM.html',pGRASIM='{}'.format(output))


modelUPL=pickle.load(open('pickle/UPL.pkl','rb'))


@app.route('/stocks/UPL.html',methods=['GET'])
def UPL():
    return render_template('/stocks/UPL.html')
@app.route('/cUPL',methods=['POST'])
def pUPL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelUPL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cUPL.html',pUPL='{}'.format(output))


modelMM=pickle.load(open('pickle/MM.pkl','rb'))


@app.route('/stocks/MM.html',methods=['GET'])
def MM():
    return render_template('/stocks/MM.html')
@app.route('/cMM',methods=['POST'])
def pMM():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelMM.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cMM.html',pMM='{}'.format(output))


modelKOTAKBANK=pickle.load(open('pickle/KOTAKBANK.pkl','rb'))


@app.route('/stocks/KOTAKBANK.html',methods=['GET'])
def KOTAKBANK():
    return render_template('/stocks/KOTAKBANK.html')
@app.route('/cKOTAKBANK',methods=['POST'])
def pKOTAKBANK():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelKOTAKBANK.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cKOTAKBANK.html',pKOTAKBANK='{}'.format(output))


modelTATAMOTORS=pickle.load(open('pickle/TATAMOTORS.pkl','rb'))


@app.route('/stocks/TATAMOTORS.html',methods=['GET'])
def TATAMOTORS():
    return render_template('/stocks/TATAMOTORS.html')
@app.route('/cTATAMOTORS',methods=['POST'])
def pTATAMOTORS():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelTATAMOTORS.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cTATAMOTORS.html',pTATAMOTORS='{}'.format(output))


modelCOALINDIA=pickle.load(open('pickle/COALINDIA.pkl','rb'))


@app.route('/stocks/COALINDIA.html',methods=['GET'])
def COALINDIA():
    return render_template('/stocks/COALINDIA.html')
@app.route('/cCOALINDIA',methods=['POST'])
def pCOALINDIA():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelCOALINDIA.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cCOALINDIA.html',pCOALINDIA='{}'.format(output))


modelJSWSTEEL=pickle.load(open('pickle/JSWSTEEL.pkl','rb'))


@app.route('/stocks/JSWSTEEL.html',methods=['GET'])
def JSWSTEEL():
    return render_template('/stocks/JSWSTEEL.html')
@app.route('/cJSWSTEEL',methods=['POST'])
def pJSWSTEEL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelJSWSTEEL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cJSWSTEEL.html',pJSWSTEEL='{}'.format(output))


modelSUNPHARMA=pickle.load(open('pickle/SUNPHARMA.pkl','rb'))


@app.route('/stocks/SUNPHARMA.html',methods=['GET'])
def SUNPHARMA():
    return render_template('/stocks/SUNPHARMA.html')
@app.route('/cSUNPHARMA',methods=['POST'])
def pSUNPHARMA():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelSUNPHARMA.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cSUNPHARMA.html',pSUNPHARMA='{}'.format(output))


modelEICHERMOT=pickle.load(open('pickle/EICHERMOT.pkl','rb'))


@app.route('/stocks/EICHERMOT.html',methods=['GET'])
def EICHERMOT():
    return render_template('/stocks/EICHERMOT.html')
@app.route('/cEICHERMOT',methods=['POST'])
def pEICHERMOT():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelEICHERMOT.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cEICHERMOT.html',pEICHERMOT='{}'.format(output))


# modelINFRATEL=pickle.load(open('pickle/INFRATEL.pkl','rb'))


# @app.route('/stocks/INFRATEL.html',methods=['GET'])
# def INFRATEL():
#     return render_template('/stocks/INFRATEL.html')
# @app.route('/cINFRATEL',methods=['POST'])
# def pINFRATEL():
#     int_features=[float(x) for x in request.form.values()]
#     features=[np.array(int_features)]
#     prediction=modelINFRATEL.predict(features)
#     output=round(prediction[0],2)
#     return render_template('/close/cINFRATEL.html',pINFRATEL='{}'.format(output))


modelZEEL=pickle.load(open('pickle/ZEEL.pkl','rb'))


@app.route('/stocks/ZEEL.html',methods=['GET'])
def ZEEL():
    return render_template('/stocks/ZEEL.html')
@app.route('/cZEEL',methods=['POST'])
def pZEEL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelZEEL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cZEEL.html',pZEEL='{}'.format(output))


modelASIANPAINT=pickle.load(open('pickle/ASIANPAINT.pkl','rb'))


@app.route('/stocks/ASIANPAINT.html',methods=['GET'])
def ASIANPAINT():
    return render_template('/stocks/ASIANPAINT.html')
@app.route('/cASIANPAINT',methods=['POST'])
def pASIANPAINT():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelASIANPAINT.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cASIANPAINT.html',pASIANPAINT='{}'.format(output))


modelICICIBANK=pickle.load(open('pickle/ICICIBANK.pkl','rb'))


@app.route('/stocks/ICICIBANK.html',methods=['GET'])
def ICICIBANK():
    return render_template('/stocks/ICICIBANK.html')
@app.route('/cICICIBANK',methods=['POST'])
def pICICIBANK():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelICICIBANK.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cICICIBANK.html',pICICIBANK='{}'.format(output))


modelITC=pickle.load(open('pickle/ITC.pkl','rb'))


@app.route('/stocks/ITC.html',methods=['GET'])
def ITC():
    return render_template('/stocks/ITC.html')
@app.route('/cITC',methods=['POST'])
def pITC():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelITC.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cITC.html',pITC='{}'.format(output))


modelTITAN=pickle.load(open('pickle/TITAN.pkl','rb'))


@app.route('/stocks/TITAN.html',methods=['GET'])
def TITAN():
    return render_template('/stocks/TITAN.html')
@app.route('/cTITAN',methods=['POST'])
def pTITAN():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelTITAN.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cTITAN.html',pTITAN='{}'.format(output))


modelWIPRO=pickle.load(open('pickle/WIPRO.pkl','rb'))


@app.route('/stocks/WIPRO.html',methods=['GET'])
def WIPRO():
    return render_template('/stocks/WIPRO.html')
@app.route('/cWIPRO',methods=['POST'])
def pWIPRO():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelWIPRO.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cWIPRO.html',pWIPRO='{}'.format(output))


modelAXISBANK=pickle.load(open('pickle/AXISBANK.pkl','rb'))


@app.route('/stocks/AXISBANK.html',methods=['GET'])
def AXISBANK():
    return render_template('/stocks/AXISBANK.html')
@app.route('/cAXISBANK',methods=['POST'])
def pAXISBANK():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelAXISBANK.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cAXISBANK.html',pAXISBANK='{}'.format(output))


modelHDFCBANK=pickle.load(open('pickle/HDFCBANK.pkl','rb'))


@app.route('/stocks/HDFCBANK.html',methods=['GET'])
def HDFCBANK():
    return render_template('/stocks/HDFCBANK.html')
@app.route('/cHDFCBANK',methods=['POST'])
def pHDFCBANK():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHDFCBANK.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHDFCBANK.html',pHDFCBANK='{}'.format(output))


modelBAJAJFINSV=pickle.load(open('pickle/BAJAJFINSV.pkl','rb'))


@app.route('/stocks/BAJAJFINSV.html',methods=['GET'])
def BAJAJFINSV():
    return render_template('/stocks/BAJAJFINSV.html')
@app.route('/cBAJAJFINSV',methods=['POST'])
def pBAJAJFINSV():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBAJAJFINSV.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBAJAJFINSV.html',pBAJAJFINSV='{}'.format(output))


modelBAJAJAUTO=pickle.load(open('pickle/BAJAJ-AUTO.pkl','rb'))


@app.route('/stocks/BAJAJ-AUTO.html',methods=['GET'])
def BAJAJAUTO():
    return render_template('/stocks/BAJAJ-AUTO.html')
@app.route('/cBAJAJ-AUTO',methods=['POST'])
def pBAJAJAUTO():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBAJAJAUTO.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBAJAJ-AUTO.html',pBAJAJAUTO='{}'.format(output))


modelPOWERGRID=pickle.load(open('pickle/POWERGRID.pkl','rb'))


@app.route('/stocks/POWERGRID.html',methods=['GET'])
def POWERGRID():
    return render_template('/stocks/POWERGRID.html')
@app.route('/cPOWERGRID',methods=['POST'])
def pPOWERGRID():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelPOWERGRID.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cPOWERGRID.html',pPOWERGRID='{}'.format(output))


modelNIFTY50=pickle.load(open('pickle/NIFTY50.pkl','rb'))


@app.route('/stocks/NIFTY50.html',methods=['GET'])
def NIFTY50():
    return render_template('/stocks/NIFTY50.html')
@app.route('/cNIFTY50',methods=['POST'])
def pNIFTY50():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelNIFTY50.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cNIFTY50.html',pNIFTY50='{}'.format(output))


modelTATASTEEL=pickle.load(open('pickle/TATASTEEL.pkl','rb'))


@app.route('/stocks/TATASTEEL.html',methods=['GET'])
def TATASTEEL():
    return render_template('/stocks/TATASTEEL.html')
@app.route('/cTATASTEEL',methods=['POST'])
def pTATASTEEL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelTATASTEEL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cTATASTEEL.html',pTATASTEEL='{}'.format(output))


modelBRITANNIA=pickle.load(open('pickle/BRITANNIA.pkl','rb'))


@app.route('/stocks/BRITANNIA.html',methods=['GET'])
def BRITANNIA():
    return render_template('/stocks/BRITANNIA.html')
@app.route('/cBRITANNIA',methods=['POST'])
def pBRITANNIA():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBRITANNIA.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBRITANNIA.html',pBRITANNIA='{}'.format(output))


modelULTRATECHCEMENT=pickle.load(open('pickle/ULTRATECHCEMENT.pkl','rb'))


@app.route('/stocks/ULTRATECHCEMENT.html',methods=['GET'])
def ULTRATECHCEMENT():
    return render_template('/stocks/ULTRATECHCEMENT.html')
@app.route('/cULTRATECHCEMENT',methods=['POST'])
def pULTRATECHCEMENT():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelULTRATECHCEMENT.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cULTRATECHCEMENT.html',pULTRATECHCEMENT='{}'.format(output))


modelINFY=pickle.load(open('pickle/INFY.pkl','rb'))


@app.route('/stocks/INFY.html',methods=['GET'])
def INFY():
    return render_template('/stocks/INFY.html')
@app.route('/cINFY',methods=['POST'])
def pINFY():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelINFY.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cINFY.html',pINFY='{}'.format(output))


modelGAIL=pickle.load(open('pickle/GAIL.pkl','rb'))


@app.route('/stocks/GAIL.html',methods=['GET'])
def GAIL():
    return render_template('/stocks/GAIL.html')
@app.route('/cGAIL',methods=['POST'])
def pGAIL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelGAIL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cGAIL.html',pGAIL='{}'.format(output))


modelIOC=pickle.load(open('pickle/IOC.pkl','rb'))


@app.route('/stocks/IOC.html',methods=['GET'])
def IOC():
    return render_template('/stocks/IOC.html')
@app.route('/cIOC',methods=['POST'])
def pIOC():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelIOC.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cIOC.html',pIOC='{}'.format(output))


modelVEDL=pickle.load(open('pickle/VEDL.pkl','rb'))


@app.route('/stocks/VEDL.html',methods=['GET'])
def VEDL():
    return render_template('/stocks/VEDL.html')
@app.route('/cVEDL',methods=['POST'])
def pVEDL():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelVEDL.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cVEDL.html',pVEDL='{}'.format(output))


modelBHARTIART=pickle.load(open('pickle/BHARTIART.pkl','rb'))


@app.route('/stocks/BHARTIART.html',methods=['GET'])
def BHARTIART():
    return render_template('/stocks/BHARTIART.html')
@app.route('/cBHARTIART',methods=['POST'])
def pBHARTIART():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBHARTIART.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBHARTIART.html',pBHARTIART='{}'.format(output))


modelSBIN=pickle.load(open('pickle/SBIN.pkl','rb'))


@app.route('/stocks/SBIN.html',methods=['GET'])
def SBIN():
    return render_template('/stocks/SBIN.html')
@app.route('/cSBIN',methods=['POST'])
def pSBIN():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelSBIN.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cSBIN.html',pSBIN='{}'.format(output))


modelNESTLEIND=pickle.load(open('pickle/NESTLEIND.pkl','rb'))


@app.route('/stocks/NESTLEIND.html',methods=['GET'])
def NESTLEIND():
    return render_template('/stocks/NESTLEIND.html')
@app.route('/cNESTLEIND',methods=['POST'])
def pNESTLEIND():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelNESTLEIND.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cNESTLEIND.html',pNESTLEIND='{}'.format(output))


modelHCLTECH=pickle.load(open('pickle/HCLTECH.pkl','rb'))


@app.route('/stocks/HCLTECH.html',methods=['GET'])
def HCLTECH():
    return render_template('/stocks/HCLTECH.html')
@app.route('/cHCLTECH',methods=['POST'])
def pHCLTECH():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHCLTECH.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHCLTECH.html',pHCLTECH='{}'.format(output))


modelBAJAJFINANCE=pickle.load(open('pickle/BAJAJFINANCE.pkl','rb'))


@app.route('/stocks/BAJAJFINANCE.html',methods=['GET'])
def BAJAJFINANCE():
    return render_template('/stocks/BAJAJFINANCE.html')
@app.route('/cBAJAJFINANCE',methods=['POST'])
def pBAJAJFINANCE():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelBAJAJFINANCE.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cBAJAJFINANCE.html',pBAJAJFINANCE='{}'.format(output))


modelTCS=pickle.load(open('pickle/TCS.pkl','rb'))


@app.route('/stocks/TCS.html',methods=['GET'])
def TCS():
    return render_template('/stocks/TCS.html')
@app.route('/cTCS',methods=['POST'])
def pTCS():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelTCS.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cTCS.html',pTCS='{}'.format(output))


modelDRREDDY=pickle.load(open('pickle/DRREDDY.pkl','rb'))


@app.route('/stocks/DRREDDY.html',methods=['GET'])
def DRREDDY():
    return render_template('/stocks/DRREDDY.html')
@app.route('/cDRREDDY',methods=['POST'])
def pDRREDDY():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelDRREDDY.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cDRREDDY.html',pDRREDDY='{}'.format(output))


modelINDUSINDBANK=pickle.load(open('pickle/INDUSIND BANK.pkl','rb'))


@app.route('/stocks/INDUSIND BANK.html',methods=['GET'])
def INDUSINDBANK():
    return render_template('/stocks/INDUSIND BANK.html')
@app.route('/cINDUSIND BANK',methods=['POST'])
def pINDUSINDBANK():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelINDUSINDBANK.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cINDUSIND BANK.html',pINDUSINDBANK='{}'.format(output))


modelMARUTI=pickle.load(open('pickle/MARUTI.pkl','rb'))


@app.route('/stocks/MARUTI.html',methods=['GET'])
def MARUTI():
    return render_template('/stocks/MARUTI.html')
@app.route('/cMARUTI',methods=['POST'])
def pMARUTI():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelMARUTI.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cMARUTI.html',pMARUTI='{}'.format(output))


modelHDFC=pickle.load(open('pickle/HDFC.pkl','rb'))


@app.route('/stocks/HDFC.html',methods=['GET'])
def HDFC():
    return render_template('/stocks/HDFC.html')
@app.route('/cHDFC',methods=['POST'])
def pHDFC():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelHDFC.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cHDFC.html',pHDFC='{}'.format(output))


modelNTPC=pickle.load(open('pickle/NTPC.pkl','rb'))


@app.route('/stocks/NTPC.html',methods=['GET'])
def NTPC():
    return render_template('/stocks/NTPC.html')
@app.route('/cNTPC',methods=['POST'])
def pNTPC():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelNTPC.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cNTPC.html',pNTPC='{}'.format(output))


modelRELIANCE=pickle.load(open('pickle/RELIANCE.pkl','rb'))


@app.route('/stocks/RELIANCE.html',methods=['GET'])
def RELIANCE():
    return render_template('/stocks/RELIANCE.html')
@app.route('/cRELIANCE',methods=['POST'])
def pRELIANCE():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelRELIANCE.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cRELIANCE.html',pRELIANCE='{}'.format(output))


modelLT=pickle.load(open('pickle/LT.pkl','rb'))


@app.route('/stocks/LT.html',methods=['GET'])
def LT():
    return render_template('/stocks/LT.html')
@app.route('/cLT',methods=['POST'])
def pLT():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelLT.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cLT.html',pLT='{}'.format(output))


modelTECHM=pickle.load(open('pickle/TECHM.pkl','rb'))


@app.route('/stocks/TECHM.html',methods=['GET'])
def TECHM():
    return render_template('/stocks/TECHM.html')
@app.route('/cTECHM',methods=['POST'])
def pTECHM():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelTECHM.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cTECHM.html',pTECHM='{}'.format(output))


modelCIPLA=pickle.load(open('pickle/CIPLA.pkl','rb'))


@app.route('/stocks/CIPLA.html',methods=['GET'])
def CIPLA():
    return render_template('/stocks/CIPLA.html')
@app.route('/cCIPLA',methods=['POST'])
def pCIPLA():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=modelCIPLA.predict(features)
    output=round(prediction[0],2)
    return render_template('/close/cCIPLA.html',pCIPLA='{}'.format(output))


if __name__=='__main__':
   app.run()
