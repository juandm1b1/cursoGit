const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('Está seguro de querer eliminar el registro?')) {
                e.preventDefault();
            }
        });
    });
}

function saludo(){
    alert (btnArray)
}





// const btnDelete = document.querySelectorAll('.btn-delete')
// const btnArray = Array.from(btnDelete)


    
// if(btnArray) {
//     //btnArray =  Array.from(btnDelete);     
//     //  alert("Entra al if")
//     btnArray.forEach((btn) => {
//         btn.addEventlistener('mouseover', (e) => {
//             confirmacion = confirm('¿Está seguro de querer eliminar el contacto?')
//             if(confirmacion == false){
//                 e.preventDefault();
//             }
//         });
//     });
// }







// function dilit(){
//     confirmacion = confirm('¿Está seguro de querer eliminar el contacto?')
//     var confirmado = false

//     if(confirmacion == false){        
//         alert ("Se ha evitado la eliminación del registro");                                      
//     }
//     else {
//         confirmado = true;        
//         alert("Registro eliminado correctamente");
//     }

//     return confirmado
// }

// function saludo(){
//     alert (btnArray)
// }


// function dilit(){
//     confirmacion = confirm('¿Está seguro de querer eliminar el contacto?')

//     if(confirmacion == true){  
//         window.location.href = "/delete/{{contact.0}}"
//         //alert("Registro eliminado correctamente");                      
//     }
//     else {
//         alert("Se ha evitado la eliminación del registro");        
//     }
// }