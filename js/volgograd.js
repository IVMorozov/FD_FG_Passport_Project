$(document).ready(function() {
	
	
	const data = {
		labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль'],
		datasets: [
			{
				label: 'Продажи',
				data: [65, 59, 80, 81, 56, 55, 40],
				fill: false,
				borderColor: 'rgb(75, 192, 192)',
				tension: 0.1
			},
			{
				label: 'Посещения',
				data: [28, 48, 40, 19, 86, 27, 90],
				fill: false,
				borderColor: 'rgb(255, 99, 132)',
				tension: 0.1
			},
			{
				label: 'Регистрации',
				data: [12, 35, 22, 45, 30, 50, 60],
				fill: false,
				borderColor: 'rgb(54, 162, 235)',
				tension: 0.1
			}
		]
	};

	// Настройки графика
	const config = {
		type: 'line',
		data: data,
		options: {
			scales: {
				y: {
					beginAtZero: true
				}
			}
		}
	};

	// Создание графика
	
	const myChart2 = new Chart(
		document.getElementById('myChart2'),
		config
	);

	
}) // $(document).ready(function()