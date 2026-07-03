const input = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("taskList");

addBtn.addEventListener("click", addTask);


function addTask(){

    const taskText = input.value;

    if(taskText === "") return;

    const li = document.createElement("li");

    li.textContent = taskText;

    li.addEventListener("click",function(){
         li.classList.toggle("completed");
    });

    list.appendChild(li);

    input.value = "";
}