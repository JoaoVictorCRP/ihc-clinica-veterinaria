document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.calendar .d-flex');
    const diasMes = 31;
    const consultas = { 
        5: ['<b>14h</b> - Vacinação de <b>Luna</b>', '<b>17h</b> - Vacinação de <b>Max</b>'],
        10: ['<b>11h</b> - Castração de <b>Pou</b>'],
        17:['<b>08:30</b> - Tratamento Dental de <b>Terror</b>'],
        21: ['<b>16h</b> - Tosa de <b>Luna</b>'],
        26:['<b>17:30h</b> - Internação de <b>Cana-Brava</b>'],
        29: ['<b>15:20h</b> - Consulta de <b>Stella</b>'] };

    for (let dia = 1; dia <= diasMes; dia++) {
        const dayElement = document.createElement('div');
        dayElement.classList.add('p-2', 'border', 'w-50', 'text-center', 'mb-2', 'border', 'border-black');
        dayElement.style.flex = "0 0 13.2%"; // Aproximadamente 1/7 para simular 7 dias na semana
        dayElement.innerHTML = `<strong>Dia ${dia}</strong>`;

        if (consultas[dia]) { // Se tem consulas no dia
            const lista = document.createElement('ul');
            consultas[dia].forEach(consulta => {
                const item = document.createElement('li');
                item.innerHTML = consulta;
                lista.appendChild(item);
            });
            dayElement.appendChild(lista);
        }

        container.appendChild(dayElement);
    }
});
