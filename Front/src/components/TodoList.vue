<template>
  <div>
    <button class="btn btn-primary m-2" @click="emits('allTasks')">All Tasks</button>
    <button class="btn btn-primary m-2" @click="emits('todoTasks')">Todo Tasks</button>
    <button class="btn btn-primary m-2" @click="emits('doneTasks')">Done Tasks</button>
  </div>
  <div>
    <div class="mb-5 mt-5 mx-auto d-flex justify-content-end">
      <button class="btn btn-primary" @click="visible = true">Add</button>
    </div>
    <div
      class="d-flex flex-wrap justify-content-between mx-auto bg-white shadow-lg  border mt-3 p-2 rounded custom-hover-effect"
      v-for="(task, index) in tasks"
      :key="index"
      >
          <div>
            <h5>{{ task.title }}</h5>
            <p>
              {{ task.description }}
            </p>
            <p >
              Task label: <b class='text-warning'> {{ task.label }} </b>
            </p>
            <p>
              Completes Status
              <img src="https://cdn.pixabay.com/photo/2017/03/28/01/46/check-mark-2180770_1280.png" alt="Image" width="20px" class="m-2"  v-if="task.status"/>
              <img src="https://static.vecteezy.com/system/resources/thumbnails/014/313/137/small/red-cross-icon-for-things-that-should-not-be-done-or-forbidden-png.png" alt="Image" width="40px" class="m-2" v-else/>
            </p>
          </div>
          <div class='mt-auto'>
            <router-link :to="'/detail/' + index" class="text-white">
              <button class="btn btn-success">Detail</button>
            </router-link>
            <button class="btn btn-primary m-2" @click="onEdit(index)">Edit</button>
            <button class="btn btn-danger m-2" @click="deleteTask(index,task.id)">Delete</button>
            <button class="btn btn-success m-2" v-if='task.status' @click="updateStatus(index, task.id)">Done</button>
            <button class="btn btn-success m-2" v-else @click="updateStatus(index, task.id)">Make as complete</button>
          </div>
    </div>
  </div>
  <Dialog v-model:visible="visible" modal header="Add New Task" :style="{ height: '40rem'}" :breakpoints="{ '3000px': '75vw', '575px': '90vw' }" class='bg-white m-5 rounded p-5 shadow-lg border'>
      <input type="text" id="myInput" v-model="newTask.title" class="form-control mr-2  mt-5" placeholder='Input title here!'/>
      <input type="text" id="myInput" v-model="newTask.img" class="form-control mr-2  mt-5" placeholder='Input image url here!'/>
      <textarea type="text" id="myInput" v-model="newTask.description" class="form-control mr-2 mt-5" placeholder='Input description here!'/>
      <div>
        <p class='mt-3'> Task label </p>
        <input type="radio" id="1" value="Urgent" class='m-2' v-model="newTask.label">
        <label for="1">Urgent</label>

        <input type="radio" id="2" value="Important" class='m-2' v-model="newTask.label">
        <label for="2">Important</label>

        <input type="radio" id="3" value="Not Urgent" class='m-2' v-model="newTask.label">
        <label for="3">Not Urgent</label>

        <input type="radio" id="4" value="Not Important" class='m-2' v-model="newTask.labe">
        <label for="4">Not Important</label>
      </div>
      <div class='mt-5 d-flex flex-row-reverse p-2'>
        <button class="btn btn-primary m-2" @click="addTask" v-if='!isEdit'>Add</button>
        <button class="btn btn-primary m-2" @click="editTask" v-else>Save</button>
        <button class="btn btn-primary m-2" @click="visible = false" v-if='!isEdit'>Close</button>
      </div>
  </Dialog>

</template>

<script setup>
import { ref, defineProps, watch, defineEmits, toRef } from 'vue';
import Dialog from 'primevue/dialog';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';


const store = useStore();
const router = useRouter();
const isEdit = ref(false);
const taskIndex = ref(null);
const visible = ref(false);
const newTask = ref({
  title:'',
  description:'',
  img:'',
  label:'',
  status: false,
});
const props = defineProps({
  tasks: []
})
const emits = defineEmits(['todoTasks', 'doneTasks', 'allTasks'])
const tasks = toRef(props, 'tasks');

function addTask() {
  if(newTask.value.title!=='' && newTask.value.description!=='' && newTask.value.img!=='') {
    store.dispatch('fetchAddTask', { newTask })
    visible.value = false
  }
}
function deleteTask(index,task_id) {
  store.dispatch('fetchDeleteTask', {"index": index, "task_id": task_id})
}
function onEdit(index) {
  newTask.value = store.getters.taskId({"index": index});
  visible.value = true;
  isEdit.value = true;
  taskIndex.value = index;
}
function editTask() {
  store.dispatch('fetchUpdateTask', { "newTask": newTask, "index": taskIndex })
  isEdit.value = false;
  visible.value = false
}
function updateStatus(index, id) {
  const status = tasks.value[index].status
  store.dispatch('fetchUpdateStatus', { "index":index, "id": id, "status": status })
}
</script>

<style>
.custom-hover-effect:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transform: scale(1.005);
  transition: all 0.3s ease;
}
.p-dialog-header-close-icon path{
  display: none;
}
</style>