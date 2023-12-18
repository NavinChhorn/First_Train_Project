<template>
    <div class=" mt-5  p-5 d-flex justify-content-betweenbg-primary">
        <img :src="task.img" alt="Image" class="rounded-0 w-50" />
        <p class='align-self-center m-5'>
            <h2> 
                Task Title: {{ task.title}}
            </h2>
            <p>
               <b> Description:</b> {{ task.description }}
            </p>
            <p>
                <b> Lable:</b> <span>{{ task.label }}, </span>
            </p>
            <p v-if="task.status">
                <b> Status:</b> You already completed it yet !
            </p>
            <p v-else>
                <b> Status:</b> You didn't complete it yet !
            </p>
        </p>
    </div>
    <div class='d-flex flex-row-reverse m-5'>   
        <RouterLink to="/task" class="text-white">
            <button class="btn bg-primary text-white"> Exit </button>
        </RouterLink>
    </div>
</template>

<script setup>
import { defineProps, toRef } from 'vue'

const props = defineProps({
  task: []
})
const task = toRef(props, 'task');
</script>