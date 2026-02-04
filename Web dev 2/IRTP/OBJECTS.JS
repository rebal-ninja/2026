let userinfo = {
    // key : value 
    name : "tez",
    age : 17,
    proffesion: "developer",

    info: function(){
        return `${this.name},age ${this.age},works as ${this.proffesion}`;
    }

}

console.log(userinfo.info());