function outerfun()
{
    let outervar= "im ouside ";
    function infun(){
        console.log("im in but this guy is out ",outervar);
    }
    infun();
}
outerfun();

