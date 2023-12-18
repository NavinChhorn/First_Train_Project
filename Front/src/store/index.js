import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state() {
    return {
      count: 0,
      tasks: []
    };
  },
  getters: {
    allTasks: (state) => state.tasks,
    taskId:  (state)=> (params) => {
      return state.tasks[params.index]
    }
  },
  mutations: {
    ADD_TASK: (state, data) =>{
      state.tasks.unshift(data);
    },
    UPDATE_TASK(state, payload) {
      state.tasks[payload.index.value] = payload.newTask.value;
    },
    UPDATE_STATUS(state, taskIndex) {
      state.tasks[taskIndex].status = !state.tasks[taskIndex].status
    },
    GET_TASKS: (state, data) => {
      state.tasks = data
    },
    DELETE_TASK: (state, id) => {
      state.tasks.splice(id, 1);
    }
  },
  actions: {
    fetchTasks({ commit }, params={}) {
      axios.get('http://127.0.0.1:5000/tasks').then((res) => {
        if (res.status === 200){
          let respData = []

          if (!params.hasOwnProperty('status')){
            respData = res.data
          }else{
            respData = res.data.filter(task => task.status == params.status)
          }
          commit('GET_TASKS', respData)
        }else{
          commit('GET_TASKS', [])
        } 
    })},

    fetchAddTask( {commit },payload) {
      axios.post('http://127.0.0.1:5000/tasks', payload.newTask.value).then((res) => {
        commit('ADD_TASK', res.data)
    })},

    fetchDeleteTask({ commit }, payload) {
      axios.delete('http://127.0.0.1:5000/tasks/' + payload.task_id)
        .then((res) => {
          if(res.status === 204) {
            commit('DELETE_TASK', payload.index)
          }
        })
        .catch((error) => {
          console.log(error);
    });},

    fetchUpdateTask({ commit }, payload) {
      axios.put('http://127.0.0.1:5000/tasks', payload.newTask.value)
        .then(() => {
          commit("UPDATE_TASK", payload)
        })
        .catch((error) => {
          console.log(error);
    });},

    fetchUpdateStatus({ commit }, payload) {
      axios.patch('http://127.0.0.1:5000/tasks', { "id": payload.id, "status": !payload.status})
        .then((res) => {
          if(res.status === 200) {
            commit('UPDATE_STATUS', payload.index)
          }
        })
    },
  },
});

export default store;
