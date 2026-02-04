function outerfun()
{
    let outervar= "im ouside ";
    function infun(){
        console.log(outervar);
    }
    infun();
}
outerfun();

