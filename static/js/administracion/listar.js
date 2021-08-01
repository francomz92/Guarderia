/* ----- Constantes----- */


/* ----- Funciones ----- */

function listarUI() {
	fetch(window.location.pathname, {
		method: 'GET',
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
		},
		// body: JSON.stringify({ action: 'listar' }),
	})
	.then((res) => res.json())
	// Preparación del JSON
	.then((data) => {
		// Configuración de las columnas
		if (data.length >= 1) {
			let columns = [];
			for (const key in data[0]) {
				columns.push({ data: key });
			}
			
			// Inicación de DataTable
			$('#table_id').DataTable({
				dom: '<lf<t>Bip>',
				buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
				responsive: true,
				autoWidth: false,
				deferRender: true,
				data: data,
				columns: columns,
				columnDefs: columnDefs,
			});
			return data;
		} else {
			$('#table_id').DataTable({
				dom: '<lf<t>Bip>',
				buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
					responsive: true,
					autoWidth: false,
					deferRender: true,
					data: data,
				});
				return data;
			}
		})
		.catch((err) => console.log(err));
	}
	
	function borrarUI(id) {
		// Alerta al borrar un registro
		$('.borrar').confirm({
			title: 'Borrar',
			theme: 'material',
			type: 'red',
			content: '¿Estás seguro de eliminar este registro?',
			boxWidth: '30%',
		icon: 'fas fa-exclamation-circle fa-spin',
		useBootstrap: false,
		buttons: {
			cofirm: {
				text: 'Cofirmar',
				btnClass: 'btn btn-outline-danger',
				action: function () {
					// fetch(this.$target.attr('data-link'), {
					fetch(window.location.pathname, {
						method: 'POST',
						headers: {
							// 'content-Type': 'application/json',
							'X-Requested-With': 'XMLHttpRequest',
						},
						body: JSON.stringify({
							'action': 'delete',
							'id': this.$target.attr('id')
						})
					})
					// Recarga de DataTable
					// let tabla = $.fn.dataTable.tables({ api: true });
					// tabla.destroy();
					// listarUI();
					let tabla = $('#table_id').DataTable();
					tabla.row(id).remove().draw();
				},
			},
			cancel: {
				text: 'Cancelar',
				btnClass: 'btn btn-outline-dark',
			},
		},
	});
}

/* ----- Ejecuciones ----- */

document.addEventListener('DOMContentLoaded', () => {
	listarUI();
});
