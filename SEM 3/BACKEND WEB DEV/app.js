const details = {
    name:"rahul",
    age : 18,
    email : "arunreddy@gmail.com",
    phone= 123474567

}

const printdetails = (obj)=>{
    obj.name = "tez"
    obj.graduation = "btexch"
    return obj 
}

let obj2 = printdetails(details)
console.log(obj2)


