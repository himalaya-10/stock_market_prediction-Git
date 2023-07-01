const express = require("express")
const fs=require('fs')
const path= require('path')
const app = express()
const port =80
const mongoose=require('mongoose')
// const tex=fs.readFileSync("index.html")
app.use("/static",express.static("static"))

app.set('view engine','pug')

app.set('views',path.join(__dirname,'views'))


mongoose.connect('mongodb://localhost/stockpred')
const bodyparser= require('body-parser')

const closedSchema = new mongoose.Schema({
    trade_company:String,
    prevclose:Number,
    open:Number,
    high:Number,
    low:Number,
    last:Number,
    VWAP:Number
});
const pred_close = mongoose.model('pred_close', closedSchema);
app.engine('pug', require('pug').__express)
app.use(express.urlencoded())

app.get('/',(req,res)=>{
    res.status(200).render('index')
})
app.post('/close',(req,res)=>{
    var mydata= new pred_close(req.body)
    // const filePath = 'input.txt';
    // fs.writeFile(filePath, req.body)
    // console.log(req.body)

    mydata.save().then(()=>{
        console.log("data saved")
    }).catch(()=>{
        res.status(404).send("some error occured")
    })
    res.status(200).render('close.pug')
})

app.listen(port,()=>{
    console.log(`list. to port ${port}`)
})



