/* ----- Constantes----- */

// Columnas personalizadas de DataTable
let columnDefs = [
	{
		// Columna Foto
		targets: [6],
		visible: true,
		render: (info, type, row) => {
			let archivo = '';
			if (row.foto !== '-') {
				archivo = '<a href="'+info+'" title="Documentación de '+row.nombre + ' ' + row.apellido+'" target="_blanck">Archivo</a>';
			}
			else {
				archivo = '-';
			}
			return archivo;
		}
	},
	{
		// Columna Acciones
		targets: [-1],
		visible: true,
		render: (info, type, row, meta) => {
			let editar = '<a href="/alumno-tutor/editar-tutor/'+ row.id +'/" class="btn btn-outline-success sm">Editar</a>'
			let borrar = '<a onclick="borrarUI('+meta.row+')" class="btn btn-outline-danger sm borrar" id="'+row.id+'">Borrar</a>'
			return editar + borrar;
		}
	}
]


/* ----- Funciones ----- */


/* ----- Ejecuciones ----- */