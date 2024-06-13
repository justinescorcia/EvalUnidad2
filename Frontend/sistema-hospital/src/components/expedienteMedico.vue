<template>
    <h1 class="text-2xl font-bold text-gray-800 dark:text-white mb-4">Expediente Medico:</h1>
    <div class="mb-6">
    <div class="grid grid-cols-2 gap-4">
        <div>
            <label for="nombre" class="block text-gray-700 dark:text-white mb-1">Nombre</label>
            <input type="text" id="nombre" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" required>
        </div>
        <div>
            <label for="apellido" class="block text-gray-700 dark:text-white mb-1">Apellido</label>
            <input type="text" id="apellido" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" required>
        </div>
        <div>
            <label for="fechaNacimiento" class="block text-gray-700 dark:text-white mb-1">Fecha de Nacimiento</label>
            <input type="date" id="fechaNacimiento" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" required>
        </div>
        <div>
            <label for="genero" class="block text-gray-700 dark:text-white mb-1">Género</label>
            <select id="genero" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                <option selected>Selecciona tu género</option>
                <option value="Masculino">Masculino</option>
                <option value="Femenino">Femenino</option>
                <option value="Otro">Otro</option>
            </select>
        </div>
        <div>
            <label for="direccion" class="block text-gray-700 dark:text-white mb-1">Dirección</label>
            <input type="text" id="direccion" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
        </div>
        <div>
            <label for="telefonoEmergencia" class="block text-gray-700 dark:text-white mb-1">Teléfono de Emergencia</label>
            <input type="tel" id="telefonoEmergencia" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
        </div>
        <div>
            <label for="tipoSangre" class="block text-gray-700 dark:text-white mb-1">Tipo de Sangre</label>
            <select id="tipoSangre" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                <option selected>Selecciona tu tipo de sangre</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
                <option value="A+">A+</option>
                <option value="A-">A-</option>
                <option value="B+">B+</option>
                <option value="B-">B-</option>
                <option value="AB+">AB+</option>
                <option value="AB-">AB-</option>
            </select>
        </div>
        <div>
            <label for="alergias" class="block text-gray-700 dark:text-white mb-1">Alergias</label>
            <textarea id="alergias" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none"></textarea>
        </div>
        <div>
            <label for="enfermedades" class="block text-gray-700 dark:text-white mb-1">Enfermedades Crónicas</label>
            <textarea id="enfermedades" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none"></textarea>
        </div>
        <div>
            <label for="medicamentosR" class="block text-gray-700 dark:text-white mb-1">Medicamentos Recetados</label>
            <textarea id="medicamentosR" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none"></textarea>
        </div>
    </div>
    <div class="mt-8 flex justify-start">
        <button class="bg-teal-500 text-white px-4 py-2 rounded-lg hover:bg-teal-700 dark:bg-teal-600 dark:text-white dark:hover:bg-teal-900">Guardar Expediente Médico</button>
    </div>
</div>

</template>