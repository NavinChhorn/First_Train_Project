<template>
    <TaskDetail :task="task"/>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import { useStore } from 'vuex'
import TaskDetail from '../components/TaskDetail.vue'
import { useRoute } from 'vue-router';

const route = useRoute();
const store = useStore()

const index = route.params.index
const task = ref([])

onBeforeMount(()=> {
  task.value = store.getters.taskId({"index":index})
})
</script>