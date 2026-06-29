const express = require("express");
// creatinga varible express and importing express 

const app = express()
// to use express 

app.get("/",(req,res)=>{
    res.send("send succesfully")
});

app.listen(3000,()=>{
    console.log("sever running at 3000")
});

// listen makes sure that port runs in loocalhost 3000