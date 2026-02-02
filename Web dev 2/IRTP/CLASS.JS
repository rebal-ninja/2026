// class student{
//     constructor(name,roll_no){
//         this.name = name ;
//         this.roll_no = roll_no;
//     }
//     study(){
//         console.log(this.name,this.roll_no)
//     }
// }

// obj = new student("tez",351)
// obj.study()


class games{
    constructor(type,name){
        this.type = type ;
        this.name = name ;
    }
    game_info(){
        console.log("game type is ", this.type, "game name ",this.name)
    }
}

obj = new games("racing","need for speed")
obj.game_info()