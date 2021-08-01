/* ----- Constantes----- */

// Columnas personalizadas de DataTable
let columnDefs = [
	{
		// Columna Acciones
		targets: [-1],
		visible: true,
		render: (info, type, row, meta) => {
			let editar = '<a href="/personal/editar-empleado/'+row.id+'/" class="btn btn-outline-success sm">Editar</a>'
			let borrar = '<a onclick="borrarUI('+meta.row+')" class="btn btn-outline-danger sm borrar" id="'+row.id+'">Borrar</a>'
			return editar + borrar;
		}
	}
]


/* ----- Funciones ----- */


/* ----- Ejecuciones ----- */