<template>
    <Dialog v-model:visible="visible" modal header="Add New Task" :style="{ height: '40rem'}" :breakpoints="{ '3000px': '75vw', '575px': '90vw' }" class='bg-white m-5 rounded p-5 shadow-lg border'>
      <input type="text" id="myInput" v-model="form.title" class="form-control mr-2  mt-5" placeholder='Input title here!'/>
      <input type="text" id="myInput" v-model="form.img" class="form-control mr-2  mt-5" placeholder='Input image url here!'/>
      <textarea type="text" id="myInput" v-model="form.description" class="form-control mr-2 mt-5" placeholder='Input description here!'/>
      <div>
        <p class='mt-3'> Task label </p>
        <input type="checkbox" id="1" value="Urgent" class='m-2' v-model="form.labels">
        <label for="1">Urgent</label>

        <input type="checkbox" id="2" value="Important" class='m-2' v-model="form.labels">
        <label for="2">Important</label>

        <input type="checkbox" id="3" value="Not Urgent" class='m-2' v-model="form.labels">
        <label for="3">Not Urgent</label>

        <input type="checkbox" id="4" value="Not Important" class='m-2' v-model="form.labels">
        <label for="4">Not Important</label>
      </div>
      <div class='mt-5 d-flex flex-row-reverse p-2'>
        <button class="btn btn-primary m-2" @click="addTask" v-if='!isEditForm'>Add</button>
        <button class="btn btn-primary m-2" @click="editTask" v-else>Save</button>
        <button class="btn btn-primary m-2" @click="visible = false">Close</button>
      </div>
  </Dialog>
</template>

<script>
import { defineProps } from 'vue'
import Dialog from 'primevue/dialog';

const props = defineProps({
    form: {},
    isEditForm: false, 
})
const form = props.form
const isEditForm = props.isEditForm

</script>