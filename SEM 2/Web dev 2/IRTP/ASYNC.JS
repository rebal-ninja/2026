async function getdata(){
    try {
        let x = await fetch("https://woringurl.com");
        let data = await x.json();
        console.log(data);
    }
    catch(err) {
        console.log("api failed");
    }
}
getdata()