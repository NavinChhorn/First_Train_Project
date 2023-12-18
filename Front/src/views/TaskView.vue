<script setup>
import { ref, onMounted , onBeforeMount, computed} from 'vue';
import TodoList from '../components/TodoList.vue'
import { useStore } from 'vuex'
import axios from 'axios'

const store = useStore()

const tasks = ref(store.getters.allTasks)


async function getAllTodoTasks() {
  store.dispatch('fetchTasks', {'status': false})
}
async function getAllDoneTasks() {
  store.dispatch('fetchTasks', {'status': true})
}
async function getAllTasks() {
  store.dispatch('fetchTasks')
}

const allTasks = computed(()=>store.getters.allTasks)
const allDoneTasks = computed(()=> { store.getters.allTasks.filter(task => task.status)})

onBeforeMount(()=> {
    getAllTasks()
})
onMounted(()=> {
  console.log("in onMounted");
})
</script>
<template>
  <div class="task mt-5 p-5">
    <h2 class='d-flex justify-content-center'>Here is my todo lists:</h2>
    <TodoList
    :tasks='allTasks'
    @todoTasks="getAllTodoTasks"
    @allTasks="getAllTasks"
    @doneTasks="getAllDoneTasks"
    />
  </div>
</template>
