<template>
    <div class="flex flex-col md:flex-row justify-center items-center">
        <div class="w-max md:w-1/2 p-4">
            <div class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md border dark:border-gray-700">
                <expedienteM></expedienteM>
            </div>
        </div>
    </div>





</template>

<script>
import expedienteM from './expedienteMedico.vue'


export default{
    components:{
        expedienteM
    }
}
</script>