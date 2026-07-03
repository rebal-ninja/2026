let person={
    full_name : "tez tanmay",
    age : 17,
    domain : "full stack development",
    cse:"mrv",
    saydomain: function() {
            console.log(this.domain);
    }
    
}
person.saydomain();