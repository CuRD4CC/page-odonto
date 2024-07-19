function confirmLogout(event) {
    event.preventDefault();
    Swal.fire({
        title: "¿Desea cerrar sesion?",
        text: "Tendra que volver loguearse",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Cerrar sesion!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Hasta luego",
                text: "Ha cerrado sesión",
                icon: "success"
            });
            // Submit the form
            event.target.form.submit();
        }
    });
}
