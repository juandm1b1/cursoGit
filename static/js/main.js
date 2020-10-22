const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete) {
    const btnArray =  Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventlistener('click', (e) => {
            if(!confirm('¿Está seguro de querer eliminar el contacto?')){
                e.preventDefault();
            }
        });
    });
}