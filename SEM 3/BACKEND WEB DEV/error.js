// function checkage(age){
//     if (age<18){
//         throw new Error ("age must be above 18 ");
//     }

//     console.log("eligible")
// }
// try {
//     checkage(16);
// }catch(err){
//     console.log(err.message)
// }

promise.reject("Something went wrong")
    .catch(err => {
        console.log(err);
    });