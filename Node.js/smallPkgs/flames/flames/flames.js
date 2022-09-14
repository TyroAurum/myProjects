//A module to find FLAMES
const express = require("express");
const flamesrelation = require("flames-relation");
const relation = flamesrelation('namce','namerfr');
console.log(relation);
const app = express();

app.get("/rel",(req,res)=>{
    res.send(relation)
})

app.listen(3000,()=>{console.log("Listening to 3000")})
