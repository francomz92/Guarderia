/* ----- Constantes----- */

// Columnas personalizadas de DataTable
let columnDefs = [
	{
		// Columna Acciones
		targets: [-1],
		visible: true,
		render: (info, type, row) => {
			let editar = '<a href="/alumno-tutor/editar-asistencia/'+ row.id +'/" class="btn btn-outline-success sm">Editar</a>'
			return editar;
		}
	}
]


/* ----- Funciones ----- */


/* ----- Ejecuciones ----- */